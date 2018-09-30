#! /bin/python

import argparse
from quake import Quake

if __name__ == "__main__":
    args = None
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "window_class",
        nargs='?',
        default="Code",
        type=str,
        help="options: 'Window class targeted (Case sensitive) (Must be "
             "floated)'. Default: 'Code'"
    )
    parser.add_argument(
        'launcher_name',
        nargs='?',
        default='default',
        type=str,
        help="options: 'Launcher name targeted (Case sensitive) Must be"
        "floated)' . Default: 'Window class name (in lower case)'"
    )
    args = parser.parse_args()
    if args.launcher_name == 'default':
        args.launcher_name = args.window_class.lower()

    if args.window_class == '':
        print(f'Quaking {args.window_class} window')
    else:
        print(f'Quaking {args.window_class} window')
        Quake(args.window_class, args.launcher_name)
