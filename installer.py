from os import path, scandir
import re

slack_dir = path.join(
    path.expanduser('~'), 'AppData', 'Local', 'slack'
)
slack_folders = [f.name for f in scandir(slack_dir) if f.is_dir()]

r = re.compile('app-.+')
try:
    app_dir = next(x for x in slack_folders if r.match(x))
except StopIteration:
    print('Slack app directory not found in ' + slack_dir)
    quit()

static_dir = path.join(
    slack_dir, app_dir, 'resources', 'app.asar.unpacked', 'src', 'static'
)

try:
    with open('black_theme.txt') as f:
        black_theme = f.read()
except FileNotFoundError:
    print('black_theme.txt not found, add to working directory for install to run')
    quit()

for file in ['index.js', 'ssb-interop.js']:
    try:
        with open(path.join(static_dir, file), 'r+') as f:
            f.seek(0)
            if black_theme in f.read():
                print('Black theme already present in ' + file + ', skipping')
            else:
                f.write('\n\n' + black_theme)
                print('Wrote black theme to ' + file)
    except FileNotFoundError:
        print(file + ' not found, skipping')

print('Successfully added black theme to Slack app files')
