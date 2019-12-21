import re
import sys


MODULE_REGEX = r'^[_a-zA-Z][_a-zA-Z0-9]+$'

module_name = '{{ cookiecutter.name }}'
project_slug = '{{ cookiecutter.project_slug }}'

print("\n\nCreating the {} package".format(project_slug))

if not re.match(MODULE_REGEX, module_name):
    print("ERROR: '%s' is not a valid Python module name ! \n" % module_name)
    # exits with status 1 to indicate failure
    sys.exit(1)
else:
    print("The name provided ({}) seems correct".format(module_name))


if project_slug != "sequana_" + module_name:
    print("In the project_slug choice, just press enter. Do not overwrite the default value")
    sys.exit(1)


