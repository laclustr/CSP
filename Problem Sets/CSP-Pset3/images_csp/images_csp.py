import sys
import os
import subprocess

if not os.path.exists("assets"):
  os.mkdir("assets")
  
sys.path.append("assets")

dependencies = ["Pillow", "numpy"]

def is_package_installed(package_name, target_folder):
  """ Check if package_name is installed to a specific target_folder """
  if package_name == "Pillow":
    package_name = "PIL"
  
  package_folder = os.path.join(target_folder, package_name)

  return os.path.exists(package_folder)

def install_package_to_folder(package_name, target_folder):
  """ Installs package_name to target_folder using pip/pip3 """
  if not is_package_installed(package_name, target_folder):
    print(f"Installing: {package_name}...")
    try:
        with open(os.devnull, "w") as devnull:
          try:
            if os.name == "nt":
              subprocess.check_call(['pip', 'install', '--target', target_folder, package_name], stdout=devnull, stderr=devnull)
            else:
              subprocess.check_call(['pip3', 'install', '--target', target_folder, package_name], stdout=devnull, stderr=devnull)
          except subprocess.CalledProcessError:
            raise Exception(f"pip must be installed, and you must have an internet connection. Verify with pip --version or pip3 --version on mac/Linux")

    except subprocess.CalledProcessError:
      raise Exception(f"Error installing {package_name}")

for d in dependencies:
  install_package_to_folder(d, "assets")


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