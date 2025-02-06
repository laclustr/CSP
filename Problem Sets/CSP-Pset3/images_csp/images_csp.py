import sys
import os
import subprocess
from PIL import Image
import numpy as np

VALID_IMG_EXTENSIONS = ["bmp", "jpg", "jpeg", "gif", "png", "jfif", "tif"]

def is_image(image):
  ext = os.path.splitext(image)[1][1:].lower()
  return ext in VALID_IMG_EXTENSIONS

def load_grayscale(image):
  """ Takes a file and returns a 2D list of grayscale pixel values """
  if not is_image(image):
    raise Exception(f"{image} is not a valid image type.")
  
  try:
    return np.array(Image.open(image).convert("L")).tolist()

  except FileNotFoundError:
    raise Exception(f"{image} was not found.")

def load_rgb(image):
  """ Takes a file and returns a 3D list of RGB pixel values """
  if not is_image(image):
    raise Exception(f"{image} is not a valid image type.")
  
  try:
    return np.array(Image.open(image)).tolist()

  except FileNotFoundError:
    raise Exception(f"{image} was not found.")

def show_image(image):
  """ Takes a 2D or 3D list of values and shows an image """
  try:
    Image.fromarray(np.array(image, dtype="uint8")).show()

  except:
    raise Exception(f"Must pass a 2D list of integers as a parameter to show_image.")

def save_image(image, path):
  """ Takes a 2D or 3D list of values and saves an image at path """
  try:
    Image.fromarray(np.array(image, dtype="uint8")).save(path)

  except:
    raise Exception(f"Something went wrong saving to {path}. Check that the image parameter is a 2D list of integers and that the path parameter is a valid path.")

if __name__ == "__main__":
  cat_gray = load_grayscale("cat.jpg")
  cat_rgb  = load_rgb("cat.jpg")
  
  show_image(cat_gray)
  show_image(cat_rgb)

  save_image(cat_gray, "cat_gray.jpg")
  save_image(cat_rgb, "cat_rgb.jpg")