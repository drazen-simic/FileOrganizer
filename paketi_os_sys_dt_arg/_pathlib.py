from pathlib import Path

#Create Path object from a string
path = Path("folder1/folder2/file.txt")
print(path.absolute().exists())

# Create Path object from a relative or absolute path
absolute_path = Path("/home/user/folder1")
relative_path = Path("folder1/subfolder")

path = Path("folder1") / "folder2" / "file.txt"
print(path)  # Output: folder1/folder2/file.txt


path = Path("folder1/folder2/file.txt")

print(path.parent)  # Output: folder1/folder2
print(path.name)  # Output: file.txt
print(path.stem)  # Output: file (without extension)
print(path.suffix)  # Output: .txt


path = Path("main_with_config.py")
print(path.exists())  # Returns True if the path exists


print(path.is_file())  # Returns True if the path is a file
print(path.is_dir())  # Returns True if the path is a directory



path = Path("paketi_os_sys_dt_arg")
for file in path.iterdir():
    print(file)


path = Path(".")
for file in path.rglob("*.txt"):  # All `.txt` files
    print(file)


path = Path("new_folder")
path.mkdir(parents=True, exist_ok=True)  # Creates 'new_folder', including parent folders if necessary


old_path = Path("old_name.txt")
new_path = Path("new_name.txt")
old_path.rename(new_path)



path = Path("file_to_delete.txt")
path.unlink()  # Deletes the file
