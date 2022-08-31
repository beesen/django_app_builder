import yaml
from yaml import SafeLoader


def read_yaml_file():
    YAML_FILE = "apps.yaml"
    # Open the file and load the file
    with open(YAML_FILE) as f:
        data = yaml.load(f, Loader=SafeLoader)
    return data

def create_app_model(app_name, model):
    # create models.py
    fields = model['fields']
    meta = model['meta']
    str = model['str']
    return

def create_app_view(app_name, model):
    # create views.py
    fields = model['fields']
    meta = model['meta']
    str = model['str']
    return

def create_app_serializerview(app_name, model):
    # create views.py
    fields = model['fields']
    meta = model['meta']
    str = model['str']
    return

def create_app_serializer(app_name, model):
    # create serializers.py
    fields = model['fields']
    meta = model['meta']
    str = model['str']
    return

def create_app_templates(app_name, model):
    # create urls.py
    fields = model['fields']
    meta = model['meta']
    str = model['str']
    return

def create_app_url(app_name, model):
    # create urls.py
    fields = model['fields']
    meta = model['meta']
    str = model['str']
    return

def create_app_admin(app_name, model):
    # create urls.py
    fields = model['fields']
    meta = model['meta']
    str = model['str']
    return

def create_app_files(app, rest):
    app_name = app['app_name']
    model = app['model']
    serializer = True
    create_app_model(app_name, model)
    if rest:
        create_app_serializerview(app_name, model)
        create_app_serializer(app_name, model)
    else:
        create_app_view(app_name, model)
        create_app_templates(app_name, model)
    create_app_serializer(app_name, model)
    create_app_url(app_name, model)
    create_app_admin(app_name, model)
    return