import os
import shutil

# Source and Destination folders
source_folder = "source_images"
destination_folder = "moved_images"

# Create destination folder if it doesn't exist
os.makedirs(destination_folder, exist_ok=True)

# Move all JPG files
count = 0
for file in os.listdir(source_folder):
    if file.lower().endswith(".jpg"):
        source_path = os.path.join(source_folder, file)
        destination_path = os.path.join(destination_folder, file)

        shutil.move(source_path, destination_path)
        print(f"Moved: {file}")
        count += 1

print(f"\nTotal JPG files moved: {count}")
