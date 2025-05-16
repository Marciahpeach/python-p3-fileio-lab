from pathlib import Path

def write_file(file_name, file_content):
    """Writes file_content to a .txt file (overwrites if file exists)."""
    full_path = file_name.with_suffix('.txt')
    with open(full_path, 'w') as file:
        file.write(file_content)


def append_file(file_name, append_content):
    """Appends append_content to a .txt file (creates file if it doesn't exist)."""
    full_path = file_name.with_suffix('.txt')
    with open(full_path, 'a') as file:
        file.write(append_content)


def read_file(file_name):
    """Reads and returns the content of the specified .txt file."""
    full_path = file_name.with_suffix('.txt')
    with open(full_path, 'r') as file:
        return file.read()
