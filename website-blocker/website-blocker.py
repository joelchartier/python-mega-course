import time
from datetime import datetime as dt

hosts_path="/etc/hosts"
redirect="127.0.0.1"
website_list=["www.facebook.com","www.twitter.com"]

STARTING_HOUR=8
ENDING_HOUR=17

while True:
    now = dt.now()

    with open(hosts_path, "r+") as file:

        if dt(now.year, now.month, now.day, STARTING_HOUR) < now < dt(now.year, now.month, now.day, ENDING_HOUR):
            print("Working hours")
            
            content=file.read()

            for website in website_list:
                if website in content:
                    print("Webiste [" + website + "] is already blocked")
                    pass

                else:
                    print("Blocking Webiste [" + website + "]")
                    file.write(redirect + " " + website + "\n")

        else:
            print("Fun time")
            content=file.readlines()
            file.seek(0)
        
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)

            file.truncate()
    
    time.sleep(300)