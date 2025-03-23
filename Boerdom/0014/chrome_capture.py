import Quartz
import AppKit

def get_chrome_bounds():
    chrome_windows = []
    windows = Quartz.CGWindowListCopyWindowInfo(Quartz.kCGWindowListOptionOnScreenOnly, Quartz.kCGNullWindowID)

    for window in windows:
        owner_name = window.get("kCGWindowOwnerName", "")
        if "Google Chrome" in owner_name:  # Filter Chrome windows
            bounds = window.get("kCGWindowBounds", {})
            chrome_windows.append(bounds)

    if chrome_windows:
        return chrome_windows[0]  # Get the first Chrome window found
    return None