
def format_string(input):
    if input>10000:
        return "{:.2e}".format(input)
    else:
        return "{:.2f}".format(input)