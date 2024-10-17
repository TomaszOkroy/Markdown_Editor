
formatters = ["plain", "bold", "italic", "header", "link", "inline-code", "new-line", "unordered-list", "ordered-list"]

options = ["!help", "!done"]
HELP_OPTION = "!help"
DONE_OPTION = "!done"

formatted_text = []

def save_to_file():
    name_file = open('output.md', 'w', encoding='utf-8')
    # print(formatted_text)
    # write the names on separate lines
    for line in formatted_text:

        name_file.write(line)
    name_file.close()


def append_to_formatted_text(text, format_type):
    if format_type == "header" or format_type == "unordered-list" or format_type == "ordered-list":
        formatted_text.append(text)
    elif format_type == "link" or format_type == "plain" or format_type == "new-line" or format_type == "bold" or format_type == "italic" or format_type == "inline-code":
        if len(formatted_text) == 0:
            formatted_text.append(text)
        else:
            formatted_text[-1] = formatted_text[-1] + text


def print_formatted_text():
    for text in formatted_text:
        print(text)


def apply_header(header_text, header_level):
    header_text = ("#" * header_level + " " + header_text) + "\n"
    return header_text


def apply_plain(plain_text):
    return plain_text


def apply_bold(bold_text):
    bold_text = "**" + bold_text + "**"
    return bold_text


def apply_italic(italic_text):
    italic_text = "*" + italic_text + "*"
    return italic_text


def apply_link(label, url):
    link = f"[{label}]({url})"
    return link


def apply_newline():
    return "\n"


def apply_inline_code(code):
    code = "`" + code + "`"
    return code


def apply_unordered_list(text_row):
    return f"* {text_row}\n"


def apply_ordered_list(text_row, row_index):
    return f"{row_index}. {text_row}\n"


def help_option():
    print(f"Available formatters: {' '.join(formatters)}")
    print(f"Special commands: {' '.join(options)}")


def done_option():
    save_to_file()


def read_user_input(text):
    return input(text)


def create_header():
    level_chosen = False
    while not level_chosen:
        level = int(read_user_input("Level: "))
        if 0 < level <= 6:
            text = read_user_input("Text: ")
            text = apply_header(text, level)
            append_to_formatted_text(text, "header")
            print_formatted_text()
            level_chosen = True
        else:
            print("The level should be within the range of 1 to 6")


def create_bold_text():
    text = read_user_input("Text: ")
    text = apply_bold(text)
    append_to_formatted_text(text, "bold")
    print_formatted_text()


def create_italic_text():
    text = read_user_input("Text: ")
    text = apply_italic(text)
    append_to_formatted_text(text, "italic")
    print_formatted_text()


def create_link():
    label = read_user_input("Label: ")
    url = read_user_input("URL: ")
    text = apply_link(label, url)
    append_to_formatted_text(text, "link")
    print_formatted_text()


def create_plain_text():
    text = read_user_input("Text: ")
    text = apply_plain(text)
    append_to_formatted_text(text, "plain")
    print_formatted_text()


def create_new_line():
    text = apply_newline()
    append_to_formatted_text(text, "new-line")
    print_formatted_text()


def create_inline_code():
    text = read_user_input("Text: ")
    text = apply_inline_code(text)
    append_to_formatted_text(text, "inline-code")
    print_formatted_text()


def create_list(list_type):
    number_of_rows_chosen = False
    while not number_of_rows_chosen:
        number_of_rows = int(read_user_input("Number of rows: "))
        if number_of_rows <= 0:
            print("The number of rows should be greater than zero")
        else:
            number_of_rows_chosen = True
            text = ""
            for row_index in range(number_of_rows):
                row_from_user = read_user_input(f"Row #{row_index + 1}: ")
                if list_type == "unordered-list":
                    text += apply_unordered_list(row_from_user)
                else:
                    text += apply_ordered_list(row_from_user, row_index + 1)
            append_to_formatted_text(text, "unordered-list")
    print_formatted_text()


def main_loop():
    exit_loop = False
    while not exit_loop:
        # print("Choose a formatter:")
        user_option = read_user_input("Choose a formatter: ")
        if user_option in options or user_option in formatters:
            if user_option == HELP_OPTION:
                help_option()
            elif user_option == DONE_OPTION:
                done_option()
                exit_loop = True
            elif user_option == "header":
                create_header()

            elif user_option == "bold":
                create_bold_text()

            elif user_option == "italic":
                create_italic_text()

            elif user_option == "link":
                create_link()

            elif user_option == "plain":
                create_plain_text()

            elif user_option == "new-line":
                create_new_line()

            elif user_option == "inline-code":
                create_inline_code()

            elif user_option == "unordered-list":
                create_list("unordered-list")

            elif user_option == "ordered-list":
                create_list("ordered-list")

        else:
            print("Unknown formatting type or command")


main_loop()
