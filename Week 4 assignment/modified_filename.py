def read_and_modify_file(filename):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
        
        # Modify the content (example: make all text uppercase)
        modified_lines = [line.upper() for line in lines]

        new_filename = "modified_" + filename
        with open(new_filename, 'w') as new_file:
            new_file.writelines(modified_lines)
        
        print(f"✅ Modified file saved as '{new_filename}'.")

    except FileNotFoundError:
        print("❌ Error: The file does not exist.")
    except IOError:
        print("❌ Error: Could not read or write the file.")
    except Exception as e:
        print(f"❌ An unexpected error occurred: {e}")

# Ask user for the file name
user_file = input("Enter the filename to read and modify: ")
read_and_modify_file(user_file)
