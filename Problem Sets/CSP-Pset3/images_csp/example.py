import images_csp

cat_gray = load_grayscale("cat.jpg")
cat_rgb  = load_rgb("cat.jpg")

show_image(cat_gray)
show_image(cat_rgb)

save_image(cat_gray, "cat_gray.jpg")
save_image(cat_rgb, "cat_rgb.jpg")