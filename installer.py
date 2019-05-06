import os
import re

slack_dir = os.path.join(os.path.expanduser('~'), 'AppData', 'Local', 'slack')
slack_folders = [f.name for f in os.scandir(slack_dir) if f.is_dir()]

r = re.compile('app-.+')
try:
    app_dir = next(x for x in slack_folders if r.match(x))
except StopIteration:
    print('Slack app directory not found in ' + slack_dir)
    quit()

static_dir = os.path.join(
    slack_dir, app_dir, 'resources', 'app.asar.unpacked', 'src', 'static'
)

with open('black_theme.txt') as f:
    black_theme = f.read()

for file in ['index.js', 'ssb-interop.js']:
    with open(os.path.join(static_dir, file), 'a') as f:
        f.write('\n\n' + black_theme)

print('Successfully added black theme to Slack app files')
