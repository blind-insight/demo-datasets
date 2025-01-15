def collect(items, field_name):
    """
    Return the values for `field_name` for each item in `items`.
    """

    valid = filter(lambda item: bool(item['data'][field_name]), items)
    return [v['data'][field_name] for v in valid]
