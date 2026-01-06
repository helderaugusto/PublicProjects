import os
import shutil

# Source folder
source_folder = 'Source_Folder'

# Destination folder organized by file type
dest_folder = 'Final_Folder'

# Create destination folder if it doesn't exist
if not os.path.exists(dest_folder):
    os.mkdir(dest_folder)

# Loop through files in the source folder
for filename in os.listdir(source_folder):
    # Skip if it's not a file
    if not os.path.isfile(os.path.join(source_folder, filename)):
        continue

    # Example: separate files by extension
    ext = filename.split('.')[-1]
    folder_path = os.path.join(dest_folder, ext)
    if not os.path.exists(folder_path):
        os.mkdir(folder_path)

    # Rename files to a consistent pattern
    new_name = f"{ext}_{filename}"
    shutil.copy(os.path.join(source_folder, filename), os.path.join(folder_path, new_name))

print("Files organized successfully!")