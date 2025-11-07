import sys
import os

temp_path = os.path.abspath("../temp_dir")

print("Before modification:")
for path in sys.path:
    print(path)


try:
    import test_file_1
    print("Imported 'text' successfully.")
    print("test_file_1.print_text()", test_file_1.print_text())
except ModuleNotFoundError:
    print("Could not import 'text'.")


# To add temp_path to sys.path
if temp_path not in sys.path:
    sys.path.insert(0, temp_path)

print("After modification:")
for path in sys.path:
    print(path)

try:
    import test_file_1
    print("Imported 'text' successfully.")
    print("test_file_1.print_text()", test_file_1.print_text())
except ModuleNotFoundError:
    print("Could not import 'text'.")
