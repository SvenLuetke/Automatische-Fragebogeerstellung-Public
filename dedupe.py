from table_extraction_word import extract_all_tables_data


def _tupleize(obj):
    if isinstance(obj, list):
        return tuple(_tupleize(x) for x in obj)
    return obj


def remove_duplicates_nested(lst):

    if not isinstance(lst, list):
        return lst

    # First process children recursively
    processed = [remove_duplicates_nested(x) for x in lst]

    seen = set()
    result = []
    for item in processed:
        key = _tupleize(item)
        if key not in seen:
            seen.add(key)
            result.append(item)

    return result



