def add_numbers(a, b):
    return a + b

def format_result(a, b, result):

    return f"{a} + {b} = {result}"

def validate_input(value):

    try:
        return float(value)
    except ValueError:
        return None