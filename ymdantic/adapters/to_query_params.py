from typing import Any


def bools_to_str(x: Any) -> Any:
    """
    Recursively convert all boolean values in the input to their string representations.

    :param x: Input data which can be a boolean, dictionary, list, tuple.
    :return: Data with all boolean values converted to strings.
    """
    if isinstance(x, bool):
        return str(x).lower()
    if isinstance(x, dict):
        return {k: bools_to_str(v) for k, v in x.items()}
    if isinstance(x, list):
        return [bools_to_str(v) for v in x]
    if isinstance(x, tuple):
        return [bools_to_str(v) for v in x]
    return x
