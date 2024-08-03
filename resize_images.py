from PIL import Image
import os
from tqdm import tqdm


def report_image_sizes(directory):
    sizes = {}
    for filename in os.listdir(directory):
        filepath = os.path.join(directory, filename)
        if os.path.isfile(filepath):
            try:
                with Image.open(filepath) as img:
                    sizes[filename] = img.size
            except Exception as e:
                print(f"Could not process {filename}: {e}")
    return sizes


def resize_images_in_directory(directory, size):
    filenames = os.listdir(directory)
    for filename in tqdm(filenames, desc="Resizing images", unit="file"):
        filepath = os.path.join(directory, filename)
        if os.path.isfile(filepath):
            try:
                with Image.open(filepath) as img:
                    resized_img = img.resize(size)
                    resized_img.save(filepath)
            except Exception as e:
                print(f"Could not resize {filename}: {e}")


if __name__ == "__main__":
    directory = input("Enter the directory path containing images: ")
    width = int(input("Enter the desired width: "))
    height = int(input("Enter the desired height: "))
    size = (width, height)

    print("\nOriginal Image Sizes:")
    original_sizes = report_image_sizes(directory)
    for filename, img_size in original_sizes.items():
        print(f"{filename}: {img_size}")

    resize_images_in_directory(directory, size)

    
    print(f"\nAll images have been resized to {width}x{height}.")
