# cli-resource-monitor

A lightweight terminal resource monitor written in Python.

## Installation

### Requirements

- Python 3.9+
- NVIDIA GPU with nvidia-smi installed

### Using pipx (recommended)

Install pipx:

```bash
python -m pip install pipx
python -m pipx ensurepath
```

Then: 

```bash
pipx install git+https://github.com/ashley-oc/cli-resource-monitor.git
```


## Usage 

Run the app from command prompt or powershell using:

```bash
resource-monitor
```

## Args

Examples:

```bash
resource-monitor # Uses all defaults in the table below
resource-monitor --ri 5
resource-monitor --refresh-interval 2
```

| Arg | Short | Description | Required | Default |
|--------|--------|------------|----------|----------|
| `--refresh-interval` | `--ri` | Refresh interval in seconds | No | `1` |

------------------------------------------------------------------------

## License

MIT
