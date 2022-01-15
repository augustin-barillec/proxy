import time
import yaml
from basenames import build_localtunnel_basename, build_index_basename


def get_url(port):
    localtunnel_basename = build_localtunnel_basename(port)
    url = None
    while url is None:
        try:
            with open(localtunnel_basename) as f:
                url = yaml.safe_load(f)['your url is']
        except (FileNotFoundError, TypeError):
            time.sleep(1)
    return url


def get_port_to_url(ports):
    return {p: get_url(p) for p in ports}


def create_index_js(port_to_url):
    index_content = "const get_app = require('./get-app.js');\n"
    for p in sorted(port_to_url):
        url = port_to_url[p]
        index_content += f"exports.proxy_{p} = get_app.getApp('{url}')\n"
    index_basename = build_index_basename()
    with open(index_basename, "w") as text_file:
        text_file.write(index_content)
