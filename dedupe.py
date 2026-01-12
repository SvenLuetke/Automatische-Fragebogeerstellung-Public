# If a Word table has merged cells, the extracted data may contain duplicate rows or columns.
# This module provides functionality to remove such duplicates from nested lists. 

from table_extraction_word import extract_all_tables_data


def _tupleize(obj):
    if isinstance(obj, list):
        return tuple(_tupleize(x) for x in obj)
    return obj


def remove_duplicates_nested(lst):

    if not isinstance(lst, list):
        return lst

    
    processed = [remove_duplicates_nested(x) for x in lst]

    seen = set()
    result = []
    for item in processed:
        key = _tupleize(item)
        if key not in seen:
            seen.add(key)
            result.append(item)

    return result



