def average_valid_measurements(values):
    """Return the average of numeric measurements, ignoring None or non-numeric values.

    - `values` must be an iterable (list). Raise TypeError if not a list.
    - Skip None and any entries that cannot be converted to float.
    - If there are no valid measurements, return 0.
    """
    if not isinstance(values, list):
        raise TypeError("values must be a list")

    total = 0.0
    count = 0

    for v in values:
        if v is None:
            continue
        try:
            total += float(v)
            count += 1
        except (TypeError, ValueError):
            # skip non-numeric values
            continue

    if count == 0:
        return 0

    return total / count
