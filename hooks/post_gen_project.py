import re
import sys





# THIS SHOULD REMAINS PURE PYTHON


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

print(colors.purple("Your pipeline layout is now ready in sequana_{{cookiecutter.name}}/ directory"))
print(colors.purple("Thanks for using sequana_start_pipeline / sequana_pipeline_template cookiecutter"))
print(colors.purple("Any suggestions welcome on https://github.com/sequana/sequana project"))

