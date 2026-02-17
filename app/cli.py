import argparse
import os
import time

from app.ui.display import render_display


def parse_args(args=None) -> argparse.Namespace: #  args=None is there purely to allow for testing.
    parser = argparse.ArgumentParser(prog="monitor")
    parser.add_argument(
        "--refresh-interval",
        "--ri",
        type=int,
        default=1,
        help="Refresh interval in seconds (default: 1)"
    )
    return parser.parse_args(args)


def main():
    #  Clear the screen before starting to clean the display.
    os.system("cls")
    args = parse_args()
    while True:
        try:
            #  Move cursor to the top-left corner so that text gets overwritten on each pass. 
            #  This prevents the flickering that happens when using os.system("cls").
            print("\033[H", end="")  

            #  Main display rendering function 
            render_display()

            #  Go to sleep to avoid excessive resource usage.
            time.sleep(args.refresh_interval)
        except KeyboardInterrupt:
            #  Clear the screen before exiting to leave a clean terminal.
            os.system("cls")
            break
