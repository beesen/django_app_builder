import yaml
from yaml import SafeLoader


def read_yaml_file():
    YAML_FILE = "apps.yaml"
    # Open the file and load the file
    with open(YAML_FILE) as f:
        data = yaml.load(f, Loader=SafeLoader)
    return data

def create_app_model(app_name, model):
    fields = model['fields']
    meta = model['meta']
    str = model['str']
    return

def create_app_files(app):
    app_name = app['app_name']
    model = app['model']
    create_app_model(app_name, model)
    # create models.py
    # create views.py
    # create serializers.py
    return