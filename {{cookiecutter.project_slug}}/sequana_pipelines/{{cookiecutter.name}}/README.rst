:Overview: TODO 
:Input: TODO
:Output: TODO

Usage
~~~~~

::

    sequana_pipelines_{{cookiecutter.name}} --help
    sequana_pipelines_{{cookiecutter.name}} --fastq-directory DATAPATH --run-mode local
    sequana_pipelines_{{cookiecutter.name}} --fastq-directory DATAPATH --run-mode slurm

This creates a directory **fastq**. You just need to execute the pipeline::

    cd {{cookiecutter.name}}
    sh {{cookiecutter.name}}.sh  # for a local run

This launch a snakemake pipeline. If you are familiar with snakemake, you can retrieve the pipeline itself and its configuration files and then execute the pipeline yourself with specific parameters::

    snakemake -s {{cookiecutter.name}}.rules -c config.yaml --cores 4 --stats stats.txt

Or use `sequanix <https://sequana.readthedocs.io/en/master/sequanix.html>`_ interface.

Requirements
~~~~~~~~~~~~

This pipelines requires:

- TODO
- TODO
- snakemake

.. include:: ../requirements.txt

.. image:: https://raw.githubusercontent.com/sequana/sequana_{{cookiecutter.name}}/master/sequana_pipelines/{{cookiecutter.name}}/dag.png


Details
~~~~~~~~~

This pipeline runs {{cookiecutter.name}} in parallel on the input fastq files (paired or not)
and then execute multiqc. A brief sequana summary report is also produced.


Rules and configuration details
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Here is a documented configuration file :download:`../sequana_pipelines/{{cookiecutter.name}}/config.yaml` to be used with the pipeline. Each rule used in the pipeline may have a section in the
configuration file. 


RULENAME_TODO
^^^^^^^^^^^^^^
.. .. snakemakerule:: TODO_RULE_NAME


