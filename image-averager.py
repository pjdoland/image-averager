import os
import numpy as np
from PIL import Image
import tempfile

# Configuration settings
DIR_PATH = "/path/to/your/project"
USE_MEDIAN = False  # Set to True for median, False for mean

def average_images_in_directory(directory_path):
    file_list = [f for f in os.listdir(directory_path) if os.path.isfile(os.path.join(directory_path, f))]
    image_files = [f for f in file_list if f.lower().endswith(('png', 'jpg', 'jpeg', 'bmp', 'tif', 'tiff'))]

    widths = []
    heights = []
    for image_file in image_files:
        with Image.open(os.path.join(directory_path, image_file)) as img:
            w, h = img.size
            widths.append(w)
            heights.append(h)
    avg_width = int(np.mean(widths))
    avg_height = int(np.mean(heights))

    # Use a temporary file for intermediate storage
    with tempfile.TemporaryFile() as tempf:
        for image_file in image_files:
            with Image.open(os.path.join(directory_path, image_file)) as img:
                img_resized = img.resize((avg_width, avg_height))
                np.save(tempf, np.array(img_resized))
        
        if USE_MEDIAN:
            # Load the arrays back and compute median
            pixel_values = []
            tempf.seek(0)
            for _ in image_files:
                pixel_values.append(np.load(tempf))
            combined_image_data = np.median(pixel_values, axis=0)
        else:
            # Load the arrays back and compute mean
            sum_array = np.zeros((avg_height, avg_width, 3), dtype=np.float64)
            tempf.seek(0)
            for _ in image_files:
                sum_array += np.load(tempf)
            combined_image_data = sum_array / len(image_files)
        
        combined_image_data = combined_image_data.astype(np.uint8)
        combined_image = Image.fromarray(combined_image_data)

    return combined_image

# Using the function
combined_image = average_images_in_directory(DIR_PATH)
filename = "median_image.png" if USE_MEDIAN else "mean_image.png"
combined_image.save(os.path.join(DIR_PATH, filename))

print(f"{filename} saved in the directory.")
