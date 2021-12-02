def arr_to_str(arr: [], sep):
    ret_val = ""
    for i, item in enumerate(arr):
        ret_val += f"{sep}{item}{sep}," if i < len(arr) - 1 else f"{sep}{item}{sep}"
    return ret_val


def fields_with_values(fields, values):
    fields.remove("id")
    ret_val = ""
    for i, v in enumerate(values):
        ret_val += f"`{fields[i]}`='{v}'," if i < len(values) - 1 else f"`{fields[i]}`='{v}'"
    return ret_val
