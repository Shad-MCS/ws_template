# pylint:disable=C0114
import os
from typing import Dict, AnyStr, Any, Optional
import yaml


def load_credentials(
    path_to_creds: Optional[None | AnyStr] = None,
) -> Dict[AnyStr, Any]:
    """Loads credentials from `path_to_creds`, if given. Otherwise, it loads
    credentials from local configs.yaml file.

    Args:
        path_to_creds (None | str, optional): The relative or absolute path to
        credentials file. This is just boilerplate code; change as necessary.
        Defaults to None, and thus reads from local config file.

    Returns:
        Dict[AnyStr, Any]: The credentials as a dictionary.
    """
    if not path_to_creds:
        here = os.path.dirname(os.path.realpath(__file__))
        path_to_creds = f"{here}/config.yaml"

    with open(path_to_creds, "r", encoding="utf-8") as f:
        credentials = yaml.load(f, yaml.FullLoader)

    return credentials["database"]
