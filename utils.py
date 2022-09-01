import os.path

import yaml
from jinja2 import Environment, FileSystemLoader
from yaml import SafeLoader


def read_apps_yaml_file():
    YAML_FILE = "apps.yaml"
    # Open the file and load the file
    with open(YAML_FILE) as f:
        # return data as dictionary
        data = yaml.load(f, Loader=SafeLoader)
    return data

def check_path(path, silent=False):
    if os.path.isdir(path):
        if not silent:
            print(f"{path} exists...")
    else:
        os.mkdir(path)
        if not silent:
            print(f"{path} created...")


def create_simple(app, environment, project_path, unit):
    # create {{units}}.py
    template_name = f"{unit}.txt"
    template = environment.get_template(template_name)
    content = template.render(app)

    app_path = project_path + app['app_name'] + '/'
    check_path(app_path)
    file_name = f"{app_path}{unit}.py"
    with open(file_name, mode="w", encoding="utf-8") as file:
        file.write(content)
        print(f"... created {file_name}")
    return
def create_model(app, environment, project_path):
    # create models.py
    create_simple(app, environment, project_path, 'models')
    return


def create_serializer(app, environment, project_path):
    # create serializers.py
    create_simple(app, environment, project_path, 'serializers')
    return


def create_views(app, environment, project_path):
    # create views.py
    create_simple(app, environment, project_path, 'views')
    return


def create_templates(app, environment, template_name):
    # create urls.py
    template = environment.get_template(template_name)
    content = template.render(app)
    print(content)
    return


def create_urls(app, environment, template_name):
    # create urls.py
    template = environment.get_template(template_name)
    content = template.render(app)
    print(content)
    return


def create_serializer_views(app, environment, project_path):
    # create views.py
    create_simple(app, environment, project_path, 'views')
    return


def create_serializer_urls(app, environment, project_path):
    # create urls.py
    create_simple(app, environment, project_path, 'urls')
    return


def create_admin(app, environment, project_path):
    # create admin.py
    create_simple(app, environment, project_path, 'admin')
    return


def create_app_files(rest, app, environment, project_path):
    create_model(app, environment, project_path)
    if rest:
        create_serializer(app, environment, project_path)
        create_serializer_views(app, environment, project_path)
        create_serializer_urls(app, environment, project_path)
    # else:
    #     create_templates(app_name, model)
    #     create_views(app_name, model)
    #     create_urls(app_name, model)
    create_admin(app, environment, project_path)
    return


def create_project(project):
    project_path = project['PATH']
    check_path(project_path)

    # define yaml's environment and template
    environment = Environment(
        loader=FileSystemLoader("templates/"),
        trim_blocks=True,
        lstrip_blocks=True
    )
    apps = project['APPS']
    rest = project['REST']
    for app in apps:
        create_app_files(rest, app, environment, project_path)
    return
