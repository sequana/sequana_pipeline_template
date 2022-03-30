import re
import sys


MODULE_REGEX = r'^[_a-zA-Z][_a-zA-Z0-9]+$'

module_name = '{{ cookiecutter.name }}'
project_slug = '{{ cookiecutter.project_slug }}'



# THIS SHOUL REMAINS PURE PYTHON


class Colors:
    """

    ::

        color = Colors()
        print(color.failed("msg"))

    """
    PURPLE = "\033[95m"
    BLUE = "\033[94m"
    GREEN = "\033[92m"
    WARNING = "\033[93m"
    FAIL = "\033[91m"
    ENDC = "\033[0m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"

    def failed(self, msg):
        return self.FAIL + msg + self.ENDC

    def bold(self, msg):
        return self.BOLD + msg + self.ENDC

    def purple(self, msg):
        return self.PURPLE + msg + self.ENDC

    def underlined(self, msg):
        return self.UNDERLINE + msg + self.ENDC

    def fail(self, msg):
        return self.FAIL + msg + self.ENDC

    def error(self, msg):
        return self.FAIL + msg + self.ENDC

    def warning(self, msg):
        return self.WARNING + msg + self.ENDC

    def green(self, msg):
        return self.GREEN + msg + self.ENDC

    def blue(self, msg):
        return self.BLUE + msg + self.ENDC


colors = Colors()
print(colors.purple("\n\nCreating the {} package.".format(project_slug)))

if not re.match(MODULE_REGEX, module_name):
    print(colors.failed("ERROR: '%s' is not a valid Python module name ! \n" % module_name))
    # exits with status 1 to indicate failure
    sys.exit(1)


if project_slug != "sequana_" + module_name:
    print(colors.error("The project name must start with sequana_"))
    sys.exit(1)
print(colors.purple("The name provided ({}) seems correct. Congratulations !".format(module_name)))
print(colors.purple("In the project_slug choice, just press enter. Do not overwrite the default value"))
