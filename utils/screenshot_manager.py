
import re
from datetime import datetime
from pathlib import Path


def capture_screenshot(driver, test_name, output_dir="screenshots"):
    """
    Capture an Appium screenshot and save it as a PNG.

    Returns the screenshot path, or None if capture fails.
    """

    if driver is None:
        print("[Screenshot] No Appium driver available.")
        return None

    try:
        screenshot_dir = Path(output_dir)
        screenshot_dir.mkdir(parents=True, exist_ok=True)

        safe_name = re.sub(r"[^A-Za-z0-9_.-]+", "_", test_name)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S_%f")

        screenshot_path = (
            screenshot_dir / f"{timestamp}_{safe_name}.png"
        )

        success = driver.get_screenshot_as_file(str(screenshot_path))

        if success and screenshot_path.exists():
            print(f"[Screenshot] Saved: {screenshot_path}")
            return str(screenshot_path)

        print("[Screenshot] Appium did not save the screenshot.")
        return None

    except Exception as exc:
        print(f"[Screenshot] Capture failed: {exc}")
        return None
