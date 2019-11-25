=========================
Sequana Pipeline Template
=========================

:version: 1.0

This repository is a Cookiecutter template to build new Sequana pipeline.


Quickstart
----------

Install the latest Cookiecutter if you haven't installed it yet (this requires
Cookiecutter 1.4.0 or higher)::

    pip install -U cookiecutter

Generate a new Sequana pipeline project as follows::

    cookiecutter https://github.com/sequana/sequana_pipeline_template.git

you will be asked some questions in particular the name of the package. Just
answer to the first question, which is the name of the pipeline. The name of the
directory should be named after the name of the project. For instance, if your
project is **varseq**, then your directory name must be **sequana_varseq**. 
Give a name for a pipeline that is not already
used in the https://github.com/sequana/ organisation. You will be asked for a
short description and keywords. Future version of this cookiecutter may ask for
other questions. The goal is to automatically fill various filess so that you
can already install the pipeline in a few minutes.

If you define the name of the pipeline as ***varseq***, it will create a directory 
called *sequana_varseq* with a structure
similar to ::

    ├── doc
    │   ├── conf.py
    │   ├── index.rst
    │   └── Makefile
    ├── README.rst
    ├── requirements.txt
    ├── sequana_pipelines
    │   └── varseq
    │       ├── config.yaml
    │       ├── varseq.rules
    │       ├── README.rst
    │       ├── requirements.txt
    │       └── schema.yaml
    ├── setup.cfg
    └── setup.py

You can install this new pipeline as follows::


    cd sequana_varseq
    python setup.py

You can build the documentation as follows::

    cd sequana_varseq/doc
    make html  # under linux

Or test it::

    cd sequana_varseq
    pytest  # this tool (pytest) must be install first (pip install pytest)


Of course, you now need to work a little bit by replacing the content of some
files with your code and/or documentation and tests.

The most important is to edit the *config.yaml* and *varseq.rules* in the
sequana_pipelines/varseq directory with your own
snakemake pipeline and configuration file. The remaining files do not need to be
edited at first. However, to be complete, you will need to edit the test files in the *test/* directory, the documentation (*index.rst*) in the *./doc* directory and so on. 

This is not perfect and we will most probably edit this template in the future
to make it more robust and possibly add such features (help needed):

* Create a repo and put it there.
* Add the repo to your Travis-CI_ account.
* Install the dev requirements into a virtualenv. (``pip install -r requirements_dev.txt``)
* Register_ your project with PyPI.
* Run the Travis CLI command `travis encrypt --add deploy.password` to encrypt your PyPI password in Travis config
  and activate automated deployment on PyPI when you push a new tag to master branch.
* Add the repo to your ReadTheDocs_ account + turn on the ReadTheDocs service hook.
* Release your package by pushing a new tag to master.
* Add a `requirements.txt` file that specifies the packages you will need for
  your project and their versions. For more info see the `pip docs for requirements files`_.
* Activate your project on `pyup.io`_.

.. _`pip docs for requirements files`: https://pip.pypa.io/en/stable/user_guide/#requirements-files
.. _Register: https://packaging.python.org/tutorials/packaging-projects/#uploading-the-distribution-archives
