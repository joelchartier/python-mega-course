import cv2, time, pandas
from datetime import datetime

class FrameLogger:

    FILE_NAME_PREFIX = "frame_logs_"
    FILE_NAME_SUFFIX = ".csv"

    def __init__(self, columns):
        self.columns = columns
        self.frames = pandas.DataFrame(columns=columns)

    def log(self, start_time, end_time):
        frame_to_append = {
            self.columns[0]: start_time,
            self.columns[1]: end_time
        }

        self.frames = self.frames.append(frame_to_append, ignore_index=True)

    def save(self):
        timestamp = datetime.now().strftime("%Y-%m-%dT%H:%M:%S")
        self.frames.to_csv(self.FILE_NAME_PREFIX + timestamp + self.FILE_NAME_SUFFIX)

class CameraManager:

    SECOND_PER_FRAME = 1
    OBJECT_BOUNDING_COLOR = (0, 255, 0)

    def __init__(self):
        self.frame_logs = []
        self.video = cv2.VideoCapture(0)
        self._wait_for_camera_init()

    def _wait_for_camera_init(self):
        time.sleep(2)

    def _stop(self):
        self.video.release()
        cv2.destroyAllWindows

    def _extract_gray_frame(self, colored_frame):
        gray_frame = cv2.cvtColor(colored_frame, cv2.COLOR_BGR2GRAY)
        return cv2.GaussianBlur(gray_frame, (21, 21), 0)

    def _extract_contours(self, first_frame, gray_frame):
        delta_frame = cv2.absdiff(first_frame, gray_frame)

        thresh_frame = cv2.threshold(delta_frame, 30, 255, cv2.THRESH_BINARY)[1]
        thresh_frame = cv2.dilate(thresh_frame, None, iterations=2)

        (_, cnts, _) = cv2.findContours(thresh_frame.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        return cnts

    def _draw_founded_object(self, frame, contour):
        (position_x, position_y, width, height) = cv2.boundingRect(contour)

        upper_right_point = (position_x, position_y)
        lower_left_point = (position_x + width, position_y + height)

        cv2.rectangle(frame, upper_right_point, lower_left_point, self.OBJECT_BOUNDING_COLOR, 3)

    def process(self):

        first_frame = None
        last_frame_contains_object = False
        current_frame_contains_object = False
        self.frame_logs = []

        while True:

            object_found_in_frame = False

            check, current_frame = self.video.read()
            gray_frame = self._extract_gray_frame(current_frame)

            if first_frame is None:
                first_frame = gray_frame
                continue

            cnts = self._extract_contours(first_frame, gray_frame)

            for contour in cnts:
                if cv2.contourArea(contour) < 10000:
                    continue
                object_found_in_frame = True

                self._draw_founded_object(current_frame, contour)

            last_frame_contains_object = current_frame_contains_object
            current_frame_contains_object = object_found_in_frame

            if last_frame_contains_object != current_frame_contains_object:
                self.frame_logs.append(datetime.now())

            cv2.imshow("Color Frame", current_frame)

            key = cv2.waitKey(self.SECOND_PER_FRAME)

            if key == ord('q'):
                if current_frame_contains_object:
                    self.frame_logs.append(datetime.now())
                break

        self._stop()

camera_manager = CameraManager()
camera_manager.process()

frame_logger = FrameLogger(["Start", "End"])

for i in range(0, len(camera_manager.frame_logs), 2):
    frame_logger.log(camera_manager.frame_logs[i], camera_manager.frame_logs[i + 1])

frame_logger.save()
