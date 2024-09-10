#Run this to run the whole code
import time

import appImmobilizer
import threading

#list of app to terminate (if open)
list_to_Immobilize = ["Instagram", "League of Legends", "Valorant", "Facebook", "Roblox", "Steam"]
immobilizer = appImmobilizer.ImmobilizeApp(list_to_Immobilize)


def check_current_windows():
    print("Checking current windows")
    immobilizer.get_current_windows()

    time.sleep(5)


def get_on_clicked_windows():
    immobilizer.get_current_opened_window()



def main():
    while True:
        thread_on_current_check = threading.Thread(target=check_current_windows())
        thread_on_clicked_windows = threading.Thread(target=get_on_clicked_windows())

        thread_on_current_check.start()
        thread_on_clicked_windows.start()

        thread_on_current_check.join()
        thread_on_clicked_windows.join()


if __name__ == "__main__":
    main()
