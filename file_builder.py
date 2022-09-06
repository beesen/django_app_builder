import os.path
import shutil

from jinja2 import Environment, FileSystemLoader

from utils import check_path, remove_path


def build_arguments_as_list(field):
    arguments = []
    # Loop over all keys in field dict
    for k, v in field.items():
        # Skip "name" and "type"
        if k == 'name' or k == 'type' or k == 'to' or k == 'app_name':
            pass
        else:
            if v == 'none':
                v = 'None'
            if k == 'upload_to' or k == 'related_name' :
                arguments.append(f"{k}='{v}'")
            else:
                arguments.append(f"{k}={v}")

    arguments_as_string = ', '.join(arguments)
    return arguments_as_string


def build_field_names_as_list(fields):
    field_names = []
    # Loop over all fields
    for field in fields:
        field_names.append(field['name'])

    return field_names


def get_app_name(model, apps):
    """
    Return app_name for model
    :param model:
    :type model:
    :return:
    :rtype:
    """
    for app in apps:
        if app['model']['name'] == model:
            help = app['app_name']
            return app['app_name']
    return '?'

def create_file(app, environment, project_path, unit, apps):
    # create {{units}}.py
    template_name = f"{unit}.txt"
    template = environment.get_template(template_name)
    fields= app['model']['fields']
    if unit == 'models':
        # Loop over all fields of this model
        for field in fields:
            if field['type'] == 'ForeignKey':
                field['app_name'] = get_app_name(field['to'], apps)
            field['arguments'] = build_arguments_as_list(field)
    if unit == 'serializers':
        app['model']['all_fields'] = build_field_names_as_list(fields)
    content = template.render(app)

    app_path = project_path + app['app_name'] + '/'
    check_path(app_path)
    file_name = f"{app_path}{unit}.py"
    with open(file_name, mode="w", encoding="utf-8") as file:
        file.write(content)
        print(f"... created {file_name}")
    migrations_path = project_path + app['app_name'] + '/migrations/'
    check_path(migrations_path, create_init=True)


# def create_templates(app, environment, template_name):
#     # create urls.py
#     template = environment.get_template(template_name)
#     content = template.render(app)
#     print(content)
#
#
# def create_views(app, environment, project_path):
#     # create views.py
#     create_file(app, environment, project_path, 'views')
#
#
# def create_urls(app, environment, template_name):
#     # create urls.py
#     template = environment.get_template(template_name)
#     content = template.render(app)
#     print(content)


def create_app_files(rest, app, environment, project_path, apps):
    create_file(app, environment, project_path, 'models', apps)
    if rest:
        create_file(app, environment, project_path, 'serializers', apps)
        create_file(app, environment, project_path, 'views', apps)
        create_file(app, environment, project_path, 'urls', apps)
    # else:
    #     create_templates(app_name, model)
    #     create_views(app_name, model)
    #     create_urls(app_name, model)
    create_file(app, environment, project_path, 'admin', apps)


def remove_app_files(app, project_path):
    app_path = project_path + app['app_name'] + '/'
    if os.path.isdir(app_path):
        shutil.rmtree(app_path)
        print(f"{app_path} removed...")


def create_django_files(project):
    project_path = project['PROJECT_PATH']
    check_path(project_path, create_init=False)

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
            create_app_files(rest, app, environment, project_path, apps)
        else:
            if project['REMOVE_UNUSED']:
                # remove path
                app_path = project_path + app['app_name'] + '/'
                remove_path(app_path)
    # for settings.py
    print("for settings.py")
    for app in apps:
        print(f"'{app['app_name']}',")
    print("")
    print("for urls.py")
    for app in apps:
        print(f"from {app['app_name']}.views import {app['model']['name']}ViewSet")
    print("")
    for app in apps:
        print(f"router.register(r'{app['app_name']}', {app['model']['name']}ViewSet),")
