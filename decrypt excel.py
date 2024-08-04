

from openpyxl import load_workbook
import itertools
import string

def brute_force_excel(file_path, max_length):
    # Define the character set to use for brute-force
    character_set = string.ascii_letters + string.digits + string.punctuation

    for length in range(1, max_length + 1):
        # Generate all possible combinations of characters of the given length
        combinations = itertools.product(character_set, repeat=length)
        
        for combination in combinations:
            password = ''.join(combination)
            try:
                workbook = load_workbook(filename=file_path, read_only=False, keep_vba=False, data_only=False, keep_links=False, password=password)
                workbook.save(file_path)
                print("Password found:", password)
                print("File decrypted successfully!")
                return
            except Exception as e:
                # Password was incorrect, try the next one
                pass

    print("Password not found within the specified length limit.")

# Example usage
file_path = r"C:\Users\20323801\Downloads\New Folder\book1.xlsx"
max_length = 6  # Maximum length of password to try
brute_force_excel(file_path, max_length)
