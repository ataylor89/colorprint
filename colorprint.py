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
    parser.add_argument('-fg', '--foreground-color', default=defaults['foreground_color'])
    parser.add_argument('-bg', '--background-color', default=defaults['background_color'])
    parser.add_argument('-b', '--bold', action='store_true', default=defaults['bold'])
    parser.add_argument('-u', '--underline', action='store_true', default=defaults['underline'])
    args = parser.parse_args()

    message = args.message.replace('\\n', '\n')

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
