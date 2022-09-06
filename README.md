# django_app_builder
Same as django startapp but more :-)
With the use of a YAML file the following files are created:
admin.py, models.py, serializers.py, urls.py, vieuws.py

See https://www.django-rest-framework.org/api-guide/relations/#nested-relationships
for "Nested relationships"


TODO:
Additional informatie is found in settings.py


### Field options
The following options are available to all field types. All are optional.
#### null
1. null
2. blank
3. choices
4. default
5. editable
6. help_text
7. unique
8. verbose_name

```yaml
PROJECT: test
PROJECT_PATH: test/
REST: true
REMOVE_UNUSED: true
APPS:
  #---------------------------------------------------------------------------------------
  # 1 projects
  #
  - app_name: projects
    use: true
    model:
      name: Test
      fields:
        - name: name_1
          type: BooleanField
          default: false
        - name: name_2
          type: CharField
          max_length: 10
        - name: name_3
          type: DateField
          auto_now: true
          auto_now_add: true
        - name: name_4
          type: DateTimeField
          auto_now: true
          auto_now_add: true
        - name: name_5
          type: DecimalField
          max_digits: 10
          max_decimal_places: 2
        - name: name_6
          type: EmailField
          max_length: 10
        - name: name_7
          type: FileField
          upload_to: path
          storage: none
          max_length: 100
        - name: name_8
          type: ImageField
          upload_to: path
          height_field: none
          width_field: none
          max_length: 100
        - name: name_9
          type: IntegerField
        - name: name_10
          type: TextField
        - name: name_11
          type: URLField
          max_length: 200
        - name: name_12
          type: UUIDField
        - name: name_13
          type: ForeignKey
          to: name_13
          on_delete: models.CASCADE
          related_name: related_name
          blank: true
          'null': true
        - name: name_14
          type: ManyToManyField
          to: field
          on_delete: models.CASCADE
          blank: true
          'null': true
        - name: name_15
          type: OneToOneField
          to: field
          on_delete: models.CASCADE
          parent_link: false
      meta:
        db_table: tests
```