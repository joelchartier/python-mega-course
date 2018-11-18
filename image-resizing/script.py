import cv2

img=cv2.imread("jojo.png", 0)
print(img)

# cv2.imshow("Jojo", img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

resized_img = cv2.resize(img, (int(img.shape[1]/2), int(img.shape[0]/2)))
cv2.imwrite("resized-jojo.png", resized_img)
cv2.imshow("Jojo", resized_img)
cv2.waitKey(2000)
cv2.destroyAllWindows()