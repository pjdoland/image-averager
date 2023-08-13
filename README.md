# image-averager
This script processes all images in a specified directory, resizing them to a common average size and then creating a composite image by either taking the median or mean of pixel values. The inspiration for this utility came from Jason Salavon's "Every Playboy Centerfold" art project.

## Requirements

- Python 3
- NumPy
- Pillow (PIL)

You can install the required packages using:

`pip install numpy Pillow`

## Configuration

Before running the script, set the desired configuration parameters at the beginning:

- `DIR_PATH`: The directory path containing the images to process.
- `USE_MEDIAN`: Set to `True` for creating a composite using the median of pixel values, and `False` for the mean.

## Usage

Run the script in your terminal:
python3 image-averager.py

The resulting composite image will be saved in the specified directory (`DIR_PATH`), with its filename indicating the method used (median or mean).

## Notes

This script is optimized for memory efficiency, making use of temporary files to handle large collections of images without consuming excessive memory.
