def read_text_file(file_path):
    """Read text content from a file."""
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()


def write_text_file(file_path, content):
    """Write text content to a file."""
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(content)


def append_text_file(file_path, content):
    """Append text content to a file."""
    with open(file_path, "a", encoding="utf-8") as file:
        file.write(content)
