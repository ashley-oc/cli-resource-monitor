import argparse
import os
import time

from app.ui.display import render_display
from .app import run


def parse_args():
    #  To do
    #  Will add optional args here in the future.
    pass


def main():
    os.system("cls")
    while True:
        print("\033[H", end="")
        render_display()
        time.sleep(1)
