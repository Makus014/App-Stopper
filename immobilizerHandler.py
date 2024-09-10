import win32process
import win32gui


class immobilizerHandler:
    def __init__(self):
        self.pid_to_hwnd = {}
        self.windows = []
        self.current_app = []

    def enum_window_callback(self, hwnd, _):
        if win32gui.IsWindowVisible(hwnd) and win32gui.GetWindowText(hwnd):
            _, found_pid = win32process.GetWindowThreadProcessId(hwnd)
            if found_pid in self.pid_to_hwnd:
                window_title = win32gui.GetWindowText(hwnd)
                self.windows.append(window_title)

    def get_windows(self):
        win32gui.EnumWindows(self.enum_window_callback, None)
        return self.windows