# slack-black-theme-installer

Basic installer for [slack-black-theme](https://github.com/Nockiro/slack-black-theme) for easier reinstallation when Slack updates and erases custom themes. Requires Python 3.5+.

## Usage
Create a file `black-theme.txt` (see slack-black-theme or use the included example) and run `installer.py`

## Todo
- Handle multiple app directories and use newest (potential old installs)
- Custom Slack install directories (currently assumes `%homepath%\AppData\Local\slack`)