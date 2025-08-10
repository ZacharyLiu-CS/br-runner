import yaml
import os

def get_topology_path(config_path):
    with open(config_path, 'r') as f:
        config = yaml.safe_load(f)
    return config.get('topology_file')

def get_hosts_from_topology(topology_path):
    with open(topology_path, 'r') as f:
        topo = yaml.safe_load(f)
    tikv_hosts = [s['host'] for s in topo.get('tikv_servers', [])]
    pd_hosts = [s['host'] for s in topo.get('pd_servers', [])]
    return tikv_hosts, pd_hosts

if __name__ == "__main__":
    config_path = os.path.join(os.path.dirname(__file__), 'conf/br_config.yaml')
    topology_path = get_topology_path(config_path)
    tikv_hosts, pd_hosts = get_hosts_from_topology(topology_path)
    print("TiKV hosts:", tikv_hosts)
    print("PD hosts:", pd_hosts)
