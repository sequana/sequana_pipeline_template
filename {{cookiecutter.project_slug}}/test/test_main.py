import easydev
import os
import tempfile
import subprocess
import sys
from sequana_pipetools.pipelines_common import get_pipeline_location as getpath

sharedir = getpath('{{cookiecutter.name}}')


def test_standalone_subprocess():
    directory = tempfile.TemporaryDirectory()
    cmd = """sequana_pipelines_{{cookiecutter.name}} --input-directory {} 
            --working-directory {} --force""".format(sharedir, directory.name)
    subprocess.call(cmd.split())


def test_standalone_script():
    directory = tempfile.TemporaryDirectory()
    import sequana_pipelines.{{cookiecutter.name}}.main as m
    sys.argv = ["test", "--input-directory", sharedir, 
            "--working-directory", directory.name, "--force"]
    m.main()

def test_full():

    with tempfile.TemporaryDirectory() as directory:
        print(directory)
        wk = directory

        cmd = "sequana_pipelines_{{cookiecutter.name}} --input-directory {} "
        cmd += "--working-directory {}  --force"
        cmd = cmd.format(sharedir, wk)
        subprocess.call(cmd.split())

        stat = subprocess.call("sh {{cookiecutter.name}}.sh".split(), cwd=wk)

        assert os.path.exists(wk + "/multi_summary.html")

def test_version():
    cmd = "sequana_pipelines_{{cookiecutter.name}} --version"
    subprocess.call(cmd.split())

