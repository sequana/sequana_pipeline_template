from setuptools import setup, find_namespace_packages
from setuptools.command.develop import develop
from setuptools.command.install import install
import subprocess


# handle sequana git link
with open("requirements.txt", encoding='utf-8') as fh:
    requirements = [req.rstrip() if not req.startswith("git+") else req.rstrip().split("egg=")[-1] for req in fh]


_MAJOR               = 0
_MINOR               = 8
_MICRO               = 0
version = f"{_MAJOR}.{_MINOR}.{_MICRO}"
release = f"{_MAJOR}.{_MINOR}"


metainfo = {
    'authors': {"main": ("thomas cokelaer", "thomas.cokelaer@pasteur.fr")},
    'version': version,
    'license' : 'new BSD',
    'url' : "https://github.com/sequana/",
    'description': "{{cookiecutter.description}}" ,
    'platforms' : ['Linux', 'Unix', 'MacOsX', 'Windows'],
    'keywords' : ['{{cookiecutter.keywords}}'],
    'classifiers' : [
          'Development Status :: 4 - Beta',
          #'Development Status :: 5 - Production/Stable',
          'Intended Audience :: Education',
          'Intended Audience :: End Users/Desktop',
          'Intended Audience :: Developers',
          'Intended Audience :: Science/Research',
          'License :: OSI Approved :: BSD License',
          'Operating System :: OS Independent',
          'Programming Language :: Python :: 3.7',
          'Programming Language :: Python :: 3.8',
          'Programming Language :: Python :: 3.9',
          'Topic :: Software Development :: Libraries :: Python Modules',
          'Topic :: Scientific/Engineering :: Bio-Informatics',
          'Topic :: Scientific/Engineering :: Information Analysis',
          'Topic :: Scientific/Engineering :: Mathematics',
          'Topic :: Scientific/Engineering :: Physics']
    }

NAME = "{{cookiecutter.name}}"

class Install(install):
    def run(self):
        cmd = "sequana_completion --name {} --force ".format(NAME)
        try: subprocess.run(cmd.split())
        except:pass
        install.run(self)

class Develop(develop):
    def run(self):
        cmd = "sequana_completion --name {} --force ".format(NAME)
        try:subprocess.run(cmd.split())
        except:pass
        develop.run(self)

setup(
    name             = "sequana_{}".format(NAME),
    version          = version,
    maintainer       = metainfo['authors']['main'][0],
    maintainer_email = metainfo['authors']['main'][1],
    author           = metainfo['authors']['main'][0],
    author_email     = metainfo['authors']['main'][1],
    long_description = open("README.rst").read(),
    keywords         = metainfo['keywords'],
    description      = metainfo['description'],
    license          = metainfo['license'],
    long_description_content_type = "text/x-rst",
    platforms        = metainfo['platforms'],
    url              = metainfo['url'],
    classifiers      = metainfo['classifiers'],

    # package installation
    packages = ["sequana_pipelines.{{cookiecutter.name}}"],

    install_requires = requirements,
    extras_require={
        "testing": [
            "pytest",
            "pytest-cov",
            "pytest-xdist",
            "pytest-mock",
            "pytest-timeout",
            "pytest-runner",
            "coveralls",
        ],
    },
    # This is recursive include of data files
    exclude_package_data = {"": ["__pycache__"]},
    package_data = {
        '': ['*.yaml', "*.rules", "*.json", "requirements.txt", "*png", "*yml", "*smk"]
        },

    zip_safe=False,

    entry_points = {'console_scripts':[
        'sequana_{{cookiecutter.name}}=sequana_pipelines.{{cookiecutter.name}}.main:main']
    }

)
