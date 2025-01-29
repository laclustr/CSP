images_csp.py is a Python module used to simplify working with images and the underlying 2D lists of pixel values. It contains the following four functions:

load_grayscale(image_path: str)                      -> 2D list
load_rgb(image_path: str)                            -> 3D list
show_image(image_list: 2D/3D list)                   -> void
save_image(image_list: 2D/3D list, output_path: str) -> void

The homework assignment will ask you to perform manipulations on images. You will load the images into your Python file by first importing images_csp and then using the provided functions as images_csp.show_image(image). See example.py to see how to load, view, and save an example image. You'll notice that img_gray is a 2D list and img_rgb is a 3D list of pixel values.

The first time you run your file it will have to install some dependencies. It will create a folder called "assets". If you change computers, do not take this assets folder with you. If you are getting weird errors about PIL or Image, delete the "assets" folder and try again.