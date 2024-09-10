import psutil
import pygetwindow as gw
import time
import win32gui
import win32process
import immobilizerHandler
import os


class ImmobilizeApp:
    def __init__(self, listToImmobilize: list):
        self.listToImmobilize = listToImmobilize
        self.current_app = []
        self.windows = gw.getAllWindows()


    # It will show all the current applications that are openned.
    def get_current_opened_window(self):
        open_window = self._get_open_windows()
        current_open_windows = self._get_open_windows()
        new_windows = [window for window in current_open_windows if window not in open_window]
        if new_windows and new_windows[0][0] != '':
            self._get_new_window(new_windows)

        closed_windows = [window for window in open_window if window not in current_open_windows]
        if closed_windows and closed_windows[0][0] != '':
            self._get_closed_windows(closed_windows)

        open_window = self._get_open_windows()


    #getting the current windows that are open
    def get_current_windows(self):
        current_windows = self._get_open_windows()
        print(current_windows)
        self.immobilize_on_Start()
        # self.immobilize_List_Windows(current_windows)


    def immobilize_on_Start(self):
        current_windows = self._get_open_windows()
        for window in current_windows:
            for apps in self.listToImmobilize:
                if window[0] == apps:
                    os.system(f'taskkill /PID {window[1]} /F ')
                    print(window[0], "TERMINATED")





    def immobilize_List_Windows(self, processName):
        print(processName[0][0])
        for apps in self.listToImmobilize:
            if apps == processName[0][0]:
                os.system(f'taskkill /PID {processName[0][1]} /F ')
                print("NAME: ", processName[0][0], "PID:", processName[0][1], " terminated!")

    #This will get all the current windows that are open
    def _get_open_windows(self): #Private getter
        windows = gw.getAllWindows()
        window_Info = []

        for window in windows:
            hwnd = window._hWnd
            _, pid = win32process.GetWindowThreadProcessId(hwnd)
            window_Info.append((window.title, pid))
        return window_Info


    def _get_new_window(self, new_window):
        print("window Open!!", new_window)
        self.immobilize_List_Windows(new_window)


    def _get_closed_windows(self, closed_window):
        print("window Closed!!", closed_window)
        # self.immobilize_List_Windows(closed_window)