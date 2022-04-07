def encode(text_):
    return text_.replace("&", "\\&")


def format_text(text):
    text = text.strip("\n")
    if "Config Vars" in text:
        text = text.split("Config Vars\n")[1]
    text = text.split("\nEdit Delete\nKEY")[0]

    components = text.split("\nEdit Delete")
    split_components = [component.split("\n") for component in components if component]
    split_components_clean = [
        [var_name, encode(value)] for (var_name, value) in split_components
    ]
    commands = [
        f"export {var_name}={value}" for (var_name, value) in split_components_clean
    ]
    return "\n".join(commands) + "\n"
