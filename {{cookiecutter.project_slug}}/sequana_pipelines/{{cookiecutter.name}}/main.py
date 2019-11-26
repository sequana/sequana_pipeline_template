import sys
import os
import argparse
import shutil

from sequana.pipelines_common import SlurmOptions, Colors, SnakemakeOptions
from sequana.pipelines_common import PipelineManager

col = Colors()


class Options(argparse.ArgumentParser):
    def __init__(self, prog="{{cookiecutter.name}}"):
        usage = col.purple(
            """This script prepares the sequana pipeline {{cookiecutter.name}} layout to
            include the Snakemake pipeline and its configuration file ready to
            use.

            In practice, it copies the config file and the pipeline into a
            directory ({{cookiecutter.name}}) together with an executable script

            For a local run, use :

                sequana_pipelines_{{cookiecutter.name}} --fastq-directory PATH_TO_DATA --run-mode local

            For a run on a SLURM cluster:

                sequana_pipelines_{{cookiecutter.name}} --fastq-directory PATH_TO_DATA --run-mode slurm

        """
        )
        super(Options, self).__init__(usage=usage, prog=prog, description="")

        # add a new group of options to the parser
        so = SlurmOptions()
        so.add_options(self)

        # add a snakemake group of options to the parser
        so = SnakemakeOptions()
        so.add_options(self)

        self.add_argument(
            "--run-mode",
            dest="run_mode",
            required=True,
            choices=['local', 'slurm'],
            help="""run_mode can be either 'local' or 'slurm'. Use local to run
                the pipeline locally, otherwise use 'slurm' to run on a cluster
                with SLURM scheduler"""
        )

        pipeline_group = self.add_argument_group("pipeline")

        pipeline_group.add_argument("--TODO", dest="TODO", default=4, type=int)
        

def main(args=None):
    NAME = "{{cookiecutter.name}}"

    if args is None:
        args = sys.argv

    options = Options(NAME).parse_args(args[1:])

    manager = PipelineManager(options, NAME)

    # create the beginning of the command and the working directory
    manager.setup()

    # fill the config file with input parameters
    cfg = manager.config.config
    # EXAMPLE TOREPLACE WITH YOUR NEEDS
    cfg.TODO = os.path.abspath(options.working_directory)
    cfg.YOURSECTION.TODO = options.TODO

    # finalise the command and save it; copy the snakemake. update the config
    # file and save it.
    manager.teardown()


if __name__ == "__main__":
    main()