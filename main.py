from threading import main_thread
from pip import main
from plyer import notification
import time

def notifyUser(title, message):
    notification.notify(
        # Health icon source : https://www.flaticon.com/free-icons/medical
        title = title, message = message, app_icon = "C:\\Python\\Eye-remainder\\img\\health_sign.ico", timeout = 5,
    )

if __name__ == '__main__':
    while True:
        notifyUser("20 Minute has passed", "Please take a break for 20 second and look somewhere 20 ft (6 m) away")

        # Sleep for 1200 second / 20 minute
        time.sleep(1200)    
    