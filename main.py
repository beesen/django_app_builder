from file_builder import create_django_files
from utils import read_apps_yaml_file


def do_it():
    project = read_apps_yaml_file()
    print(f"... creating files for project {project['PROJECT']}")
    create_django_files(project)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    do_it()
