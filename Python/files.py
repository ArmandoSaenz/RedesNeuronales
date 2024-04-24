from pathlib import Path
url = ""
file = Path(url)
print(file.is_dir())
print(file.is_file())
print(file.is_symlink())
