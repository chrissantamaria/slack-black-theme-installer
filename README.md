# slack-black-theme-installer

Basic installer for [slack-black-theme](https://github.com/Nockiro/slack-black-theme) for easier reinstallation when Slack updates and erases custom themes. Requires Python 3.5+.

## Notice

Slack 4.x includes a massive overhaul in how the app is bundled and, unfortunately, breaks this install method. For info on how to manually install in 4.x, see [this repo](https://github.com/leoandreotti/slack-dark-theme).

## Usage

Create a file `black-theme.txt` (see slack-black-theme or use the included example) and run `installer.py`

## Todo

- Custom Slack install directories (currently assumes `%homepath%\AppData\Local\slack`)
