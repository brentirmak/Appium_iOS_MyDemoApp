import time

def retry_action(action, retries=3, delay=1):
    for attempt in range(1, retries + 1):
        try:
            return action()
        except Exception as e:
            print(f"Retry {attempt}/{retries} failed: {e}")
            if attempt == retries:
                raise
            time.sleep(delay)
