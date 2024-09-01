# Snowflake Proxy Log Parser

Creates a network usage graph from Snowflake Proxy logs.

## Install

### Using Nix

```shell
nix-shell
```

### Using Python virtual environment

1. [Create and activate a virtual environment](https://docs.python.org/3/library/venv.html)
2. Install dependencies

    ```shell
    pip3 install -r requirements.txt
    ```

## Usage

Provide the path to a log file as the first argument

```shell
python3 snowflake_proxy_log_parser.py /path/to/logs.txt
```

