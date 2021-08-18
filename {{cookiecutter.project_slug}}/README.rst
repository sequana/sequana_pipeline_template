
.. image:: https://badge.fury.io/py/sequana-{{cookiecutter.name}}.svg
     :target: https://pypi.python.org/pypi/sequana_{{cookiecutter.name}}

.. image:: http://joss.theoj.org/papers/10.21105/joss.00352/status.svg
    :target: http://joss.theoj.org/papers/10.21105/joss.00352
    :alt: JOSS (journal of open source software) DOI

.. image:: https://github.com/sequana/{{cookiecutter.name}}/actions/workflows/main.yml/badge.svg
   :target: https://github.com/sequana/{{cookiecutter.name}}/actions/workflows    




This is is the **{{cookiecutter.name}}** pipeline from the `Sequana <https://sequana.readthedocs.org>`_ project

:Overview: TODO 
:Input: TODO
:Output: TODO
:Status: draft
:Citation: Cokelaer et al, (2017), ‘Sequana’: a Set of Snakemake NGS pipelines, Journal of Open Source Software, 2(16), 352, JOSS DOI doi:10.21105/joss.00352


Installation
~~~~~~~~~~~~

You must install Sequana first::

    pip install sequana

Then, just install this package::

    pip install sequana_{{cookiecutter.name}}


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

Or use `sequanix <https://sequana.readthedocs.io/en/master/sequanix.html>`_ interface.

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


