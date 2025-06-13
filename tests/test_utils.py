import os
import tempfile

import pytest
import yaml

from app.utils import load_config


def test_load_config_success():
    # create a temporary valid YAML file
    config_data = {"topics": ["Technology", "Soccer"]}
    with tempfile.NamedTemporaryFile(mode="w+", delete=False) as tmp:
        yaml.dump(config_data, tmp)
        tmp_path = tmp.name

    try:
        loaded = load_config(tmp_path)
        assert loaded == config_data
    finally:
        os.remove(tmp_path)


def test_load_config_file_not_found():
    with pytest.raises(FileNotFoundError) as exc_info:
        load_config("non_existent_file.yaml")

    assert "Config file not found" in str(exc_info.value)


def test_load_config_invalid_yaml():
    # create a temporary file with invalid YAML (missing colon)
    invalid_yaml = "topics: [Technology, Soccer"
    with tempfile.NamedTemporaryFile(mode="w+", delete=False) as tmp:
        tmp.write(invalid_yaml)
        tmp_path = tmp.name

    try:
        with pytest.raises(yaml.YAMLError) as exc_info:
            load_config(tmp_path)
        assert "Error parsing YAML" in str(exc_info.value)
    finally:
        os.remove(tmp_path)
