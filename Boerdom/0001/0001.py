import os

base_dir = "."
file_extension = ".py"

def get_next_numbered_name(existing_dirs):
    max_number = max(int(name) for name in existing_dirs if name.isdigit()) if existing_dirs else 0
    return f"{max_number + 1:04d}"

existing_dirs = [name for name in os.listdir(base_dir) if os.path.isdir(name) and name.isdigit()]
next_dir_name = get_next_numbered_name(existing_dirs)

while True:
    if next_dir_name in existing_dirs:
        existing_dirs.remove(next_dir_name)
        next_dir_name = get_next_numbered_name(existing_dirs)
    else:
        os.mkdir(next_dir_name)
        with open(os.path.join(next_dir_name, f"{next_dir_name}{file_extension}"), "w") as file:
            file.write("")
        break
