import os.path
import shutil

from jinja2 import Environment, FileSystemLoader

from utils import check_path, remove_path


def build_arguments_as_list(field):
    arguments = []
    # Loop over all keys in field dict
    for k, v in field.items():
        # Skip "name" and "type"
        if k == 'name' or k == 'type' or k == 'to' or k == 'app':
            pass
        else:
            if v == 'none':
                v = 'None'
            if k == 'upload_to' or k == 'related_name':
                arguments.append(f"{k}='{v}'")
            else:
                arguments.append(f"{k}={v}")

    arguments_as_string = ', '.join(arguments)
    return arguments_as_string


def build_fields_as_list(fields):
    field_names = []
    # Loop over all fields
    for field in fields:
        field_names.append(field['name'])
    return field_names


def get_app_name_for_model(model, apps):
    """
    Return app_name for model
    :param model:
    :type model:
    :return:
    :rtype:
    """
    for app in apps:
        if app['model']['name'] == model:
            return app['app']
    return '?'


def create_file(rest, app, environment, project_path, unit, apps):
    # create {{units}}.py
    template_name = f"{unit}.txt"
    template = environment.get_template(template_name)
    fields = app['model']['fields']
    if unit == 'models':
        # Loop over all fields of this model
        for field in fields:
            if field['type'] == 'ForeignKey':
                field['app'] = get_app_name_for_model(field['to'], apps)
            field['arguments'] = build_arguments_as_list(field)
        ordering = app['model']['meta'].get('ordering')
        if ordering:
            ordering_fields_as_list = build_fields_as_list(ordering['fields'])
            app['model']['meta']['ordering']['fields_as_list'] = ordering_fields_as_list
    if unit == 'serializers':
        fields_list = build_fields_as_list(fields)
        # append id to list of fields
        fields_list.append('id')
        app['model']['fields_as_list'] = fields_list
    app['rest'] = rest
    content = template.render(app)

    app_path = project_path + app['app'] + '/'
    check_path(app_path)
    file_name = f"{app_path}{unit}.py"
    with open(file_name, mode="w", encoding="utf-8") as file:
        file.write(content)
        print(f"... created {file_name}")
    migrations_path = project_path + app['app'] + '/migrations/'
    check_path(migrations_path, create_init=True)


def create_app_templates(app, environment, project_path):
    # create the following templates
    # jinja_templates = ['model_confirm_delete.html', 'model_form.html', 'model_list.html']
    jinja_templates = ['model_list.html']
    model = app['model']['name'].lower()
    app_name = app['app']
    app_templates_path = project_path + app['app'] + '/templates/' + app_name
    # loop over templates to create one by one
    for jinja_template in jinja_templates:
        template_name = 'templates/' + jinja_template
        template = environment.get_template(template_name)
        content = template.render(app)
        app_template = app_templates_path + jinja_template.replace('model', model)
        j = 1


def create_app_files(rest, app, environment, project_path, apps):
    create_file(rest, app, environment, project_path, 'models', apps)
    create_file(rest, app, environment, project_path, 'admin', apps)
    if rest:
        create_file(rest, app, environment, project_path, 'serializers', apps)
    else:
        create_app_templates(app, environment, project_path)
    create_file(rest, app, environment, project_path, 'views', apps)
    create_file(rest, app, environment, project_path, 'urls', apps)


def remove_app_files(app, project_path):
    app_path = project_path + app['app'] + '/'
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
                app_path = project_path + app['app'] + '/'
                remove_path(app_path)
    # for settings.py
    print("for settings.py")
    for app in apps:
        print(f"'{app['app']}',")
    print("")
    print("for urls.py")
    for app in apps:
        print(f"from {app['app']}.views import {app['model']['name']}ViewSet")
    print("")
    for app in apps:
        print(f"router.register(r'{app['app']}', {app['model']['name']}ViewSet),")
