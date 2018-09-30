#! /bin/python

import argparse
from quake import Quake

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "window_class",
        nargs='?',
        default="code",
        type=str,
        help="options: 'Window class targeted (Case sensitive) (Must be "
             "floated)'. Default: 'code'"
    )
    args = parser.parse_args()
    if args.window_class == '':
        print(f'Quaking {args.window_class} window')
    else:
        print(f'Quaking {args.window_class} window')
        Quake(args.window_class)
        # Quake('slack')

