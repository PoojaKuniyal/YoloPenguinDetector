import os

# Define the folder containing your YOLO files
folder_path = r"C:\Users\Lenovo\OIDv4_ToolKit\OID\Dataset\labels\train"

# Loop through all .txt files
for filename in os.listdir(folder_path):
    if filename.endswith(".txt"):  
        file_path = os.path.join(folder_path, filename)
        
        # Read file contents
        with open(file_path, "r") as file:
            lines = file.readlines()
        
        # Replace 'Penguin' with '0'
        new_lines = [line.replace("Penguin", "0") for line in lines]
        
        # Write back the modified content
        with open(file_path, "w") as file:
            file.writelines(new_lines)

print("Replacement completed for train!")


# Define the folder containing your YOLO files
folder_path = r"C:\Users\Lenovo\OIDv4_ToolKit\OID\Dataset\labels\validation"

# Loop through all .txt files
for filename in os.listdir(folder_path):
    if filename.endswith(".txt"):  
        file_path = os.path.join(folder_path, filename)
        
        # Read file contents
        with open(file_path, "r") as file:
            lines = file.readlines()
        
        # Replace 'Penguin' with '0'
        new_lines = [line.replace("Penguin", "0") for line in lines]
        
        # Write back the modified content
        with open(file_path, "w") as file:
            file.writelines(new_lines)

print("Replacement completed for validation!")



