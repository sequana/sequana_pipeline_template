import re
import sys


MODULE_REGEX = r'^[_a-zA-Z][_a-zA-Z0-9]+$'

module_name = '{{ cookiecutter.name }}'

print("hello")

if not re.match(MODULE_REGEX, module_name):
    print('ERROR: %s is not a valid Python module name!' % module_name)

    # exits with status 1 to indicate failure
    sys.exit(1)
else:
    print("""Welcome to sequana_pipeline_template

        You will be asked 3 questions.

        - The first question: the name of your new pipeline (the prefix sequana_
          will be added automatically)
        - The second question: a short description
        - The third question: a list of keywords separated by commas

        """)

