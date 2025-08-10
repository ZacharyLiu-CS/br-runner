# TiKV Server Configuration Tool

A Python-based tool for managing TiKV and PD server configurations. This tool reads server configurations from YAML files and provides easy access to host information for TiKV and PD servers.

## Features

- Read configuration from YAML files
- Extract host information for TiKV and PD servers
- Configurable topology file path through `br_config.yaml`
- Python virtual environment support

## Prerequisites

- Python 3.x
- Make (for using Makefile commands)

## Installation

1. Clone the repository:
   ```bash
   git clone git@github.com:ZacharyLiu-CS/br-runner.git
   cd br-runner
   ```

2. Build the environment:
   ```bash
   make build
   ```
   This will:
   - Create a Python virtual environment (if not exists)
   - Install required dependencies from `requirements.txt`

## Usage

1. Configure your topology file path in `conf/br_config.yaml`:
   ```yaml
   topology_file: "/path/to/your/topology.yaml"
   ```

2. Run the tool:
   ```bash
   make run
   ```

## Project Structure

```
.
├── conf/
│   └── br_config.yaml      # Configuration file for topology path
├── get_hosts.py           # Main script
├── requirements.txt       # Python dependencies
├── topology.yaml         # TiKV/PD server topology configuration
└── Makefile             # Build and run commands
```

## Configuration Files

### br_config.yaml
Specifies the path to your topology configuration file:
```yaml
topology_file: "/path/to/topology.yaml"
```

### topology.yaml
Contains the configuration for TiKV and PD servers:
```yaml
pd_servers:
  - host: 192.168.x.x
    ...
tikv_servers:
  - host: 192.168.x.x
    ...
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
