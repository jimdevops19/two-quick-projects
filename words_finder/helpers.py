import os

colors = {
    'red' : "\033[91m",
    'green' : "\033[92m",
    'yellow' : "\033[93m",
    'base': "\033[0m"
}

def get_files_path(extension='.txt'):
    files_path = os.path.join(os.curdir, 'words_directory')

    files_full_path = [os.path.join(files_path, f) for f in os.listdir(files_path) if f.endswith(extension)]

    return files_full_path

def find_word_in_files(str_to_find):
    all_files = get_files_path()
    for file in all_files:
        with open(file, 'r') as f:
            lines = f.readlines()
            for line in lines:
                if str_to_find in line:
                    matched_line_prettified = line.replace(
                        str_to_find, f"{colors['green']}{str_to_find}{colors['base']}"
                    )
                    print(f"{file}:{matched_line_prettified}")