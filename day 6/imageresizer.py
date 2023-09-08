from PIL import Image
import os

def resize_images(directory, new_width, new_height):
    try:
        for filename in os.listdir(directory):
            if filename.endswith(('.jpg', '.jpeg', '.png', '.gif')):
                img_path = os.path.join(directory, filename)
                img = Image.open(img_path)
                img.thumbnail((new_width, new_height))
                img.save(os.path.join(directory, f'resized_{filename}'))
        print("Images resized successfully!")
    except Exception as e:
        print(f"Error resizing images: {e}")

def main():
    print("Image Resizer")
    
    directory = input("Choose a directory containing images: ")
    new_width = int(input("Enter the new width: "))
    new_height = int(input("Enter the new height: "))
    
    resize_images(directory, new_width, new_height)

if __name__ == "__main__":
    main()
