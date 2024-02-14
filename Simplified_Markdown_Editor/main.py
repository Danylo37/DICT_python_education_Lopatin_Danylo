"""Simplified markdown editor project"""
import simplified_markdown_editor as editor

available_formatters = ["plain", "bold", "italic", "inline-code", "link",
                        "header", "unordered-list", "ordered-list", "new-line"]
special_commands = ["!help", "!done"]
result = ""

while True:
    user_formatter = input("Choose a formatter: > ")
    if user_formatter == "plain":
        result += editor.add_plain_text()

    elif user_formatter == "bold":
        result += editor.add_bold_text()

    elif user_formatter == "italic":
        result += editor.add_italic_text()

    elif user_formatter == "inline-code":
        result += editor.add_inline_code()

    elif user_formatter == "link":
        result += editor.add_link()

    elif user_formatter == "header":
        result += editor.add_header()

    elif user_formatter == "unordered-list":
        result += editor.add_list(is_ordered=False)

    elif user_formatter == "ordered-list":
        result += editor.add_list(is_ordered=True)

    elif user_formatter == "new-line":
        result += editor.add_new_line()

    elif user_formatter == "!help":
        print("Available formatters: ", *available_formatters)
        print("Special commands: ", *special_commands)
        continue

    elif user_formatter == "!done":
        with open("output.md", "w", encoding="utf-8") as result_file:
            result_file.write(result)
        break

    else:
        print("Unknown formatting type or command")
        continue

    print(result)
