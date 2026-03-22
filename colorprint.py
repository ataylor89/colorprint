#!/usr/bin/env python3

from ansi import ansi
from settings import defaults
import argparse

def main():
    parser = argparse.ArgumentParser(
        prog='colorprint',
        description='Prints beautiful text messages to stdout',
        epilog='Software by Andrew Taylor')
    parser.add_argument('message')
    parser.add_argument('-fg', '--foreground-color')
    parser.add_argument('-bg', '--background-color')
    parser.add_argument('-b', '--bold', action='store_true')
    parser.add_argument('-u', '--underline', action='store_true')
    parser.add_argument('-d', '--use-defaults', action='store_true')
    args = parser.parse_args()

    message = args.message.replace('\\n', '\n')

    if args.use_defaults:
        foreground_color = defaults['foreground_color']
        background_color = defaults['background_color']
        bold = defaults['bold']
        underline = defaults['underline']
    else:
        foreground_color = args.foreground_color
        background_color = args.background_color
        bold = args.bold
        underline = args.underline

    formatted_message = ''

    if foreground_color:
        formatted_message += f'{ansi["foreground_colors"][foreground_color]}'
    if background_color:
        formatted_message += f'{ansi["background_colors"][background_color]}'
    if bold:
        formatted_message += f'{ansi["bold"]}'
    if underline:
        formatted_message += f'{ansi["underline"]}'
    formatted_message += f'{message}{ansi["reset"]}'

    print(formatted_message)

if __name__ == '__main__':
    main()
