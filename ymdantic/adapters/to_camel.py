def to_camel(string: str) -> str:
    """
    Convert snake_case string to camelCase.

    This function takes a string in snake_case format as input, splits it
    into words by the underscore character, and then joins them back
    together in camelCase format. The first word is left as it is, and each
    subsequent word is capitalized.

    :param string: The snake_case string to convert.
    :return: The input string converted to camelCase.
    """
    words = string.split("_")
    return words[0] + "".join(word.capitalize() for word in words[1:])
