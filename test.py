import os

def tree(dir_path, prefix=""):
    """Print a visual tree structure of dir_path."""
    entries = sorted(os.listdir(dir_path))
    entries_count = len(entries)
    for idx, entry in enumerate(entries):
        path = os.path.join(dir_path, entry)
        connector = "├── " if idx < entries_count - 1 else "└── "
        print(prefix + connector + entry)
        if os.path.isdir(path):
            extension = "│   " if idx < entries_count - 1 else "    "
            tree(path, prefix + extension)

if __name__ == "__main__":
    # Change '.' to your desired directory path
    print(".")
    tree(".")
