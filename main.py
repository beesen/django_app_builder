# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from utils import read_apps_yaml_file, create_app_files


def do_it():
    data = read_apps_yaml_file()
    apps = data['APPS']
    rest = data['REST']
    for app in apps:
        create_app_files(app, rest)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    do_it()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
