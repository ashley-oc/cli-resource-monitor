import time


def run(interval: int, verbose: bool):
    while True:
        print(f"Monitoring... (interval={interval})")
        time.sleep(interval)
