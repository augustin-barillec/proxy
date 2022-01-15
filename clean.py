import glob
from utils import kill_processes, delete_file, delete_files
from basenames import build_localtunnel_basename, build_index_basename, \
    build_deploy_basename


def kill_localtunnel():
    kill_processes(contains='npm exec localtunnel')


def kill_deploy():
    kill_processes(contains='functions deploy')


def delete_localtunnel_outfiles():
    basenames = glob.glob(build_localtunnel_basename('*'))
    delete_files(basenames)


def delete_index_file():
    basename = build_index_basename()
    delete_file(basename)


def delete_deploy_outfiles():
    basenames = glob.glob(build_deploy_basename('*'))
    delete_files(basenames)


def clean_localtunnel():
    kill_localtunnel()
    delete_localtunnel_outfiles()
    delete_index_file()


def clean_deploy():
    kill_deploy()
    delete_deploy_outfiles()


def clean_localtunnel_deploy():
    clean_localtunnel()
    clean_deploy()
