import os.path
import shutil

from jinja2 import Environment, FileSystemLoader

from utils import check_path, remove_path


def create_file(app, environment, project_path, unit):
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


def create_templates(app, environment, template_name):
    # create urls.py
    template = environment.get_template(template_name)
    content = template.render(app)
    print(content)


def create_views(app, environment, project_path):
    # create views.py
    create_file(app, environment, project_path, 'views')


def create_urls(app, environment, template_name):
    # create urls.py
    template = environment.get_template(template_name)
    content = template.render(app)
    print(content)


def create_app_files(rest, app, environment, project_path):
    create_file(app, environment, project_path, 'models')
    if rest:
        create_file(app, environment, project_path, 'serializers')
        create_file(app, environment, project_path, 'views')
        create_file(app, environment, project_path, 'urls')
    # else:
    #     create_templates(app_name, model)
    #     create_views(app_name, model)
    #     create_urls(app_name, model)
    create_file(app, environment, project_path, 'admin')


def remove_app_files(app, project_path):
    app_path = project_path + app['app_name'] + '/'
    if os.path.isdir(app_path):
        shutil.rmtree(app_path)
        print(f"{app_path} removed...")


def create_django_files(project):
    project_path = project['PROJECT_PATH']
    check_path(project_path)

    # Define yaml's environment and templates dir
    environment = Environment(
        loader=FileSystemLoader("templates/"),
        trim_blocks=True,
        lstrip_blocks=True
    )
    apps = project['APPS']
    rest = project['REST']
    # Loop over all apps, only build apps "use"
    for app in apps:
        if app['use']:
            create_app_files(rest, app, environment, project_path)
        else:
            if project['REMOVE_UNUSED']:
                # remove path
                app_path = project_path + app['app_name'] + '/'
                remove_path(app_path)
