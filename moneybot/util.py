def format_int(integer):
    if integer == 100:
        return ":100:"
    else:
        return "{:,}".format(integer)
