filename = input("Enter the filename: ")

try:
    with open(filename, 'r') as file:
        content = file.read()
        print("File opened successfully!")
        print("File content:")
        print(content)

except FileNotFoundError:
    print("Error: The file does not exist.")

except PermissionError:
    print("Error: You don't have permission to read this file.")

except Exception as e:
    print(f"Unexpected error: {e}")