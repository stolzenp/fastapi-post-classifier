import yaml


def load_config(config_path: str):
    """
    Reads the YAML file at the specified path and returns its contents
    as a Python dictionary.

    Args:
        config_path (str): The file path to the YAML config file.

    Returns:
        dict: Parsed YAML content as a Python dictionary.

    Raises:
        FileNotFoundError: If the file does not exist.
        yaml.YAMLError: If the YAML is invalid.
    """
    try:
        with open(config_path) as f:
            return yaml.safe_load(f)
    except FileNotFoundError:
        raise FileNotFoundError(f"Config file not found: {config_path}") from None
    except yaml.YAMLError as e:
        raise yaml.YAMLError(f"Error parsing YAML: {e}") from e
