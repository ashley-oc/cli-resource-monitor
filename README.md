# cli-resource-monitor

A lightweight terminal resource monitor written in Python.

## Installation

This app was written in Python 3.14.2, so you should consider this the official minimum version, but it should be fine running it with slightly older Python 3 versions back to 3.9.

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

You can also include the following optional arguments to configure the app to your liking:

## Args

Examples:

```bash
resource-monitor
resource-monitor --ri 5
resource-monitor --refresh-interval 2
```

| Arg | Short | Description | Required | Default |
|--------|--------|------------|----------|----------|
| `--refresh-interval` | `--ri` | Refresh interval in seconds | No | `1` |

------------------------------------------------------------------------

## License

MIT
