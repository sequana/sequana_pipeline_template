
.. image:: https://badge.fury.io/py/sequana-{{cookiecutter.name}}.svg
     :target: https://pypi.python.org/pypi/sequana_{{cookiecutter.name}}

.. image:: http://joss.theoj.org/papers/10.21105/joss.00352/status.svg
    :target: http://joss.theoj.org/papers/10.21105/joss.00352
    :alt: JOSS (journal of open source software) DOI

.. image:: https://github.com/sequana/{{cookiecutter.name}}/actions/workflows/main.yml/badge.svg
   :target: https://github.com/sequana/{{cookiecutter.name}}/actions/workflows    

.. image:: http://joss.theoj.org/papers/10.21105/joss.00352/status.svg
   :target: http://joss.theoj.org/papers/10.21105/joss.00352
   :alt: JOSS (journal of open source software) DOI

.. image:: https://img.shields.io/badge/python-3.8%20%7C%203.9%20%7C3.10-blue.svg
    :target: https://pypi.python.org/pypi/sequana/{{cookiecutter.name}}
    :alt: Python 3.8 | 3.9 | 3.10



This is is the **{{cookiecutter.name}}** pipeline from the `Sequana <https://sequana.readthedocs.org>`_ project

:Overview: TODO 
:Input: TODO
:Output: TODO
:Status: draft
:Citation: Cokelaer et al, (2017), ‘Sequana’: a Set of Snakemake NGS pipelines, Journal of Open Source Software, 2(16), 352, JOSS DOI doi:10.21105/joss.00352


Installation
~~~~~~~~~~~~

If you already have all requirements, you can install the packages using pip::

    pip install sequana_{{cookiecutter.name}} --upgrade

Otherwise, you can create a *sequana_{{cookiecutter.name}}* conda environment executing::

    conda env create -f environment.yml

and later activate the environment::

  conda activate sequana_{{cookiecutter.name}}

A third option is to install the pipeline with pip method (see above) and use apptainer / singularity as explained afterwards.


Usage
~~~~~

::

    sequana_pipelines_{{cookiecutter.name}} --help
    sequana_pipelines_{{cookiecutter.name}} --input-directory DATAPATH 

This creates a directory with the pipeline and configuration file. You will then need 
to execute the pipeline::

    cd {{cookiecutter.name}}
    sh {{cookiecutter.name}}.sh  # for a local run

This launch a snakemake pipeline. If you are familiar with snakemake, you can 
retrieve the pipeline itself and its configuration files and then execute the pipeline yourself with specific parameters::

    snakemake -s {{cookiecutter.name}}.rules -c config.yaml --cores 4 --stats stats.txt

Or use `sequanix <https://sequana.readthedocs.io/en/main/sequanix.html>`_ interface.


Usage with apptainer / singularity::
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

With Apptainer, initiate the working directory as follows::

    sequana_{{cookiecutter.name}} --use-apptainer

Images are downloaded in the working directory but you can store then in a directory globally (e.g.)::

    sequana_{{cookiecutter.name}} --use-apptainer --apptainer-prefix ~/.sequana/apptainers

and then::

    cd {{cookiecutter.name}}
    sh {{cookiecutter.name}}.sh

if you decide to use snakemake manually, do not forget to add apptainer options::

    snakemake -s {{cookiecutter.name}}.rules -c config.yaml --cores 4 --stats stats.txt --use-apptainer --apptainer-prefix ~/.sequana/apptainers --apptainer-args "-B /home:/home"

By default, the home is already set for you. Additional binding path can be set using environment variables e.g.::

    export APPTAINER_BINDPATH=" -B /pasteur"

Requirements
~~~~~~~~~~~~

This pipelines requires the following executable(s):

- TODO

.. image:: https://raw.githubusercontent.com/sequana/sequana_{{cookiecutter.name}}/master/sequana_pipelines/{{cookiecutter.name}}/dag.png


Details
~~~~~~~~~

This pipeline runs **{{cookiecutter.name}}** in parallel on the input fastq files (paired or not). 
A brief sequana summary report is also produced.


Rules and configuration details
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Here is the `latest documented configuration file <https://raw.githubusercontent.com/sequana/sequana_{{cookiecutter.name}}/master/sequana_pipelines/{{cookiecutter.name}}/config.yaml>`_
to be used with the pipeline. Each rule used in the pipeline may have a section in the configuration file. 

Changelog
~~~~~~~~~

========= ====================================================================
Version   Description
========= ====================================================================
0.0.1     **First release.**
========= ====================================================================


