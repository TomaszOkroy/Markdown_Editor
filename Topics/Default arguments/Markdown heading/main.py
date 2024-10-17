def heading(text, header_value=1):
    if header_value < 1:
        return "# " + text
    elif header_value > 6:
        return "#" * 6 + " " + text
    else:
        return "#" * header_value + " " + text