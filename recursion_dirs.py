from pathlib import Path
import sys

folder_path = Path(sys.argv[1])

def parse_folder(path):
    for elements in path.iterdir():
        if elements.is_dir():
            print(f"This is folder - {elements.name}")
            parse_folder(elements)
        if elements.is_file():
            print(f"This is file - {elements.name}")


if __name__ == '__main__':
    parse_folder(folder_path)
