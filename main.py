import argparse
import clean
import localtunnel_run
import localtunnel_infos
import deploy


def main_localtunnel(ports):
    clean.clean_localtunnel()
    for p in ports:
        localtunnel_run.run(p)
    port_to_url = localtunnel_infos.get_port_to_url(ports)
    localtunnel_infos.create_index_js(port_to_url)


def main_deploy(ports, project_id, region):
    clean.clean_deploy()
    for p in ports:
        deploy.deploy(p, project_id, region)


parser = argparse.ArgumentParser()
parser.add_argument('action', type=str)
parser.add_argument('--ports', nargs='+', type=int, required=True)
parser.add_argument('--project_id')
parser.add_argument('--region')
args = parser.parse_args()
assert len(args.ports) <= 10
assert args.action in ('localtunnel', 'deploy', 'localtunnel_deploy')
if 'deploy' in args.action:
    assert args.project_id is not None
    assert args.region is not None
if args.action == 'localtunnel':
    main_localtunnel(args.ports)
elif args.action == 'deploy':
    main_deploy(args.ports, args.project_id, args.region)
elif args.action == 'localtunnel_deploy':
    main_localtunnel(args.ports)
    main_deploy(args.ports, args.project_id, args.region)
