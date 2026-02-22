import re


def validate_package_name(name: str):
    if not re.match(r"^[a-z_][a-z0-9_]*$", name):
        raise ValueError(
            "Invalid package name. Use lowercase letters, numbers and underscores only."
        )