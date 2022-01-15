import subprocess
from basenames import build_localtunnel_basename


def run(port):
    localtunnel_basename = build_localtunnel_basename(port)
    command = f'npx localtunnel --port {port} > {localtunnel_basename} 2>&1 &'
    subprocess.run(command, shell=True)
