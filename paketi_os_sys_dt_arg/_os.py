import os

# Current working directory operations
print("Current directory:", os.getcwd())
os.chdir('../')  # Change directory
print("After changing directory:", os.getcwd())

# List directory contents
print("\nDirectory contents:", os.listdir())
print("Directory contents with path:", os.listdir('.'))

# Path operations
file_path = "example.txt"
print("\nPath operations:")
print("Absolute path:", os.path.abspath(file_path))
print("Base name:", os.path.basename(file_path))
print("Directory name:", os.path.dirname(os.path.abspath(file_path)))

# Check file/directory existence and type
print("\nFile/Directory checks:")
print("Is path exists?", os.path.exists(file_path))
print("Is it a file?", os.path.isfile(file_path))
print("Is it a directory?", os.path.isdir('.'))

# Create and remove directories
try:
    os.mkdir("new_directory")  # Create single directory
    os.makedirs("nested/directories")  # Create nested directories
    os.rmdir("new_directory")  # Remove single directory
    os.removedirs("nested/directories")  # Remove nested directories
except FileExistsError:
    print("Directory already exists")

# File operations
if not os.path.exists("test.txt"):
    with open("test.txt", "w") as f:
        f.write("Test content")
    
    # Get file information
    print("\nFile information:")
    print("File size:", os.path.getsize("test.txt"))
    print("Last modified:", os.path.getmtime("test.txt"))
    
    # Remove file
    os.remove("test.txt")

# Environment variables
print("\nEnvironment variables:")
print("HOME:", os.environ.get('HOME'))
print("PATH:", os.environ.get('PATH'))

# System name
print("\nSystem information:")
print("Operating system:", os.name)

# Path joining operations
print("\nPath joining:")
path_parts = ['home', 'user', 'documents', 'file.txt']
joined_path = os.path.join(*path_parts)
print("Joined path:", joined_path)

# Join with different separators
base_dir = 'c:\\users'
sub_dir = 'documents'
filename = 'test.txt'
full_path = os.path.join(base_dir, sub_dir, filename)
print("Full path:", full_path)