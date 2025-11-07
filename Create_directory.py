import os

# Create the directory for the modules
new_dir = "my_dir"
os.makedirs(new_dir, exist_ok=True)

# Create module_1.py
with open(os.path.join(new_dir, "module_1.py"), "w") as f:
    f.write("""def count_words(text):
    \"\"\"Counts the number of words in the given text.\"\"\"
    words = text.split()  # Split the string by spaces to get words
    return len(words)  # Return the number of words
""")

    # Create module_2.py
    with open(os.path.join(new_dir, "module_2.py"), "w") as f:
        f.write("""def count_letters(text):""")

    # Create main_script.py inside the directory
    with open(os.path.join(new_dir, "main_data.py"), "w") as f:
        f.write("""def count_letters(text):""")
