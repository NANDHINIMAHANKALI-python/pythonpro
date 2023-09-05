import os
import shutil

def organize_files(directory):
    
    file_categories = {
        "Images": (".jpg", ".jpeg", ".png", ".gif", ".bmp"),
        "Documents": (".pdf", ".doc", ".docx", ".txt", ".ppt", ".xlsx"),
        "Videos": (".mp4", ".avi", ".mkv", ".mov", ".flv"),
    }
    

    for category in file_categories:
        category_dir = os.path.join(directory, category)
        if not os.path.exists(category_dir):
            os.makedirs(category_dir)
    
    
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        
        
        if os.path.isdir(file_path):
            continue
        

        category = "Others"
        for cat, extensions in file_categories.items():
            if any(filename.lower().endswith(ext) for ext in extensions):
                category = cat
                break
        
        
        destination_dir = os.path.join(directory, category)
        destination_path = os.path.join(destination_dir, filename)
        shutil.move(file_path, destination_path)
    
    print("Files organized into subdirectories:")
    for category in file_categories:
        print(f"- {category}")


directory_to_organize = input("Choose a directory to organize: ")

if os.path.exists(directory_to_organize):
    print("Organizing files...")
    organize_files(directory_to_organize)
    print("Files organized successfully!")
else:
    print("Directory not found.")
