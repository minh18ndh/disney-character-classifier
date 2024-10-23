import os

folder_path = r'C:\Users\minhn\Downloads\DIP project\disney-dataset\test\minion'
prefix = 'min'
#prefix = 'gif'

# List all files in the folder
files = os.listdir(folder_path)

# Filter out non-image files (adjust the list of valid extensions if needed)
valid_extensions = ['.jpg', '.jpeg', '.png']
#valid_extensions = ['.gif']

image_files = [file for file in files if any(file.lower().endswith(ext) for ext in valid_extensions)]

# Sort the image files
image_files.sort()

# Rename the files
for i, old_name in enumerate(image_files, start = 1):
    extension = os.path.splitext(old_name)[1]
    new_name = f'{prefix}{i}{extension}'
    
    # Construct full paths
    old_path = os.path.join(folder_path, old_name)
    new_path = os.path.join(folder_path, new_name)
    
    # Rename the file
    os.rename(old_path, new_path)

print("Images have been successfully renamed.")
