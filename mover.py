import os, shutil

SORTED_BASE = "/MagicFolder/Outbox"

def move_and_rename(src_path, category):
    # Ensure category folder exists
    dest_folder = os.path.join(SORTED_BASE, category.capitalize())
    os.makedirs(dest_folder, exist_ok=True)
    
    filename = os.path.basename(src_path)
    # Optionally, build a new filename
    new_name = filename  # default to original name
    # Example: prefix the category to the filename
    new_name = f"{category.capitalize()}_{filename}"
    # Could add more logic here (e.g., parse date or add timestamp to avoid dupes)
    
    dest_path = os.path.join(dest_folder, new_name)
    # If a file with the new_name already exists, might want to handle that (e.g., add a number suffix).
    if os.path.exists(dest_path):
        # avoid overwrite by adding a suffix
        base, ext = os.path.splitext(new_name)
        dest_path = os.path.join(dest_folder, f"{base}_1{ext}")
    
    shutil.move(src_path, dest_path)
    print(f"Moved file to {dest_path}")
