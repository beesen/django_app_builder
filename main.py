from file_builder import create_django_files
from utils import read_yaml_file

APPS_YAML_FILE = "apps.yaml"
SETUP_YAML_FILE = "setup.yaml"


def do_it():
    setup = read_yaml_file(SETUP_YAML_FILE)
    project = read_yaml_file(APPS_YAML_FILE)
    print(f"... creating files for project {project['PROJECT']}")
    create_django_files(project, setup)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    do_it()
