#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os
import sys

from expox import expox

def main():
    expox.main()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nInterrupted")
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)