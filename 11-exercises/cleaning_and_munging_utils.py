def try_or_none(func):
    def func_or_none(x):
        try: return func(x)
        except: return None
    return func_or_none

def parse_row(input_row, parsers):
    return [
        parser(value) if parser is not None else value
        for value, parser
        in zip(input_row, parsers)
    ]

def parse_rows_with(reader, parsers):
    for row in reader:
        yield parse_row(row, parsers)

