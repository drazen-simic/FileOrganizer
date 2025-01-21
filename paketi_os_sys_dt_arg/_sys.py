import sys

# 1. Command Line Arguments
print("\n--- Command Line Arguments ---")
print(f"Script name: {sys.argv[0]}")
print(f"Arguments passed: {sys.argv[1:]}")

# 2. Python Version Information
print("\n--- Python Version ---")
print(f"Python Version: {sys.version}")
print(f"Version Info: {sys.version_info}")

# 3. Path Information
print("\n--- Path Information ---")
print("Python Module Search Paths:")
for path in sys.path:
    print(f"- {path}")

# 4. Platform Information
print("\n--- Platform Information ---")
print(f"Platform: {sys.platform}")

# 5. Standard Input/Output/Error
print("\n--- Standard Streams ---")
print("Writing to stdout...", file=sys.stdout)
print("Writing to stderr...", file=sys.stderr)

try:
    # Some operation that might raise an exception
    x = 1 / 0
except ZeroDivisionError as e:
    print(f"Error occurred: {e}", file=sys.stderr)
    
# 6. Module Management
print("\n--- Module Management ---")
print(f"Loaded modules: {len(sys.modules)}")

# 7. Memory Management
print("\n--- Memory Management ---")
print(f"Reference count for 5: {sys.getrefcount(5)}")

# 8. Exit the program (commented out for demonstration)
# sys.exit(0)  # Exit with success status

# 9. Object Size Information
print("\n--- Object Size Information ---")
print(f"Size of integer 42: {sys.getsizeof(42)} bytes")
print(f"Size of empty string: {sys.getsizeof('')} bytes")
print(f"Size of empty list: {sys.getsizeof([])} bytes")

# 10. Command Line Arguments Extended
print("\n--- Command Line Arguments Extended ---")
print(f"Number of arguments: {len(sys.argv)}")
if len(sys.argv) > 1:
    print("Arguments with index:")
    for i, arg in enumerate(sys.argv):
        print(f"Argument {i}: {arg}")
else:
    print("No command line arguments provided")