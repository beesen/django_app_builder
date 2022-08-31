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


def create_model(app, environment, template_name):
    # create models.py
    template = environment.get_template(template_name)
    rend = template.render(app)
    print(rend)
    return


def create_views(app, environment, template_name):
    # create views.py
    template = environment.get_template(template_name)
    rend = template.render(app)
    print(rend)
    return


def create_templates(app, environment, template_name):
    # create urls.py
    template = environment.get_template(template_name)
    rend = template.render(app)
    print(rend)
    return


def create_urls(app, environment, template_name):
    # create urls.py
    template = environment.get_template(template_name)
    rend = template.render(app)
    print(rend)
    return


def create_serializer(app, environment, template_name):
    # create serializers.py
    template = environment.get_template(template_name)
    rend = template.render(app)
    print(rend)
    return


def create_serializer_views(app, environment, template_name):
    # create views.py
    template = environment.get_template(template_name)
    rend = template.render(app)
    print(rend)
    return


def create_serializer_urls(app, environment, template_name):
    # create urls.py
    template = environment.get_template(template_name)
    rend = template.render(app)
    print(rend)
    return


def create_admin(app, environment, template_name):
    # create urls.py
    template = environment.get_template(template_name)
    rend = template.render(app)
    print(rend)
    return


def create_app_files(app, rest):
    environment = Environment(
        loader=FileSystemLoader("templates/"),
        trim_blocks=True,
        lstrip_blocks=True
    )
    create_model(app, environment, "models.txt")
    # if rest:
    # create_serializer(app_name, model)
    # create_serializer_views(app_name, model)
    # create_serializer_urls(app_name, model)
    # else:
    #     create_templates(app_name, model)
    #     create_views(app_name, model)
    #     create_urls(app_name, model)
    # create_admin(app_name, model)
    return
