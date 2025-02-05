from grade_helper import grade_helper as gh
from images_csp import images_csp as img
from games import connect_four, minesweeper, sudoku, hitori

#Problem 1
def get_grades(dataP, solutionP):
	num_corr = []
	for test in range(len(dataP)):
		CCounter = 0
		for answer in range(len(dataP[test])):
			if dataP[test][answer] == solutionP[answer]:
				CCounter += 1
		num_corr.append(CCounter)
	return num_corr

#Problem 2
def get_question_counts(dataP, solutionP):
	corr_questions = []
	for question in range(len(dataP[0])):
		CCounter = 0
		for response in range(len(dataP)):
			if dataP[response][question] == solutionP[question]:
				CCounter += 1
		corr_questions.append(CCounter)
	return corr_questions

#Problem 3
def get_score_statistics(dataP, solutionP):
	CQuestions = get_grades(dataP, solutionP)
	high = CQuestions[0]
	low = CQuestions[0]
	avg_total = 0
	for score in CQuestions:
		if score > high:
			high = score
		if score < low:
			low = score
		avg_total += score
	return (high, low, avg_total / len(CQuestions))

"""
In games.py, imported to this file if needed
#Problem 4
#Problem 5
#Problem 6
#Problem 7
"""

#Problem 8
def threshold(image, threshold):
	new_img = []
	for row in image:
		new_row = []
		for px in row:
			if px >= threshold:
				new_row += [255]
			else:
				new_row += [0]
		new_img.append(new_row)
	return new_img
#End Problem 8

def limit_255(image):
	lim_img = []
	for row in image:
		new_row = []
		for px in row:
			new_row += [255] if px >= 255 else [px]
		lim_img.append(new_row)
	return lim_img

#Problem 9
def adj_brightness(image, adjustment):
	new_img = []
	for row in image:
		new_row = []
		for px in row:
			new_row.append(px + adjustment)
		new_img.append(new_row)
	return limit_255(new_img)

#Problem 10
def flip_vertical(image):
	new_img = []
	for row in range(len(image) - 1, -1, -1):
		new_img += [image[row]]
	return new_img

#Problem 11
def flip_horizontal(image):
	new_img = []
	for row in range(len(image)):
		new_row = []
		for px in range(len(image[row]) - 1, -1, -1):
			new_row += [image[row][px]]
		new_img.append(new_row)
	return new_img

#Problem 12
def invert_img(image):
	new_img = []
	for row in range(len(image)):
		new_row = []
		for px in range(len(image[row])):
			new_val = abs(image[row][px] - 255)
			new_row += [new_val]
		new_img.append(new_row)
	return new_img

#Problem 13
def crop_img(image, TLtuple, BRtuple):
	new_img = []
	for row in range(TLtuple[0], BRtuple[0]):
		new_row = []
		for px in range(TLtuple[1], BRtuple[1]):
			new_row += [image[row][px]]
		new_img.append(new_row)
	return new_img

#Problem 14
def rotate90ccw(image):
	new_img = []
	for col in range(len(image[0])):
		new_row = []
		for row in range(len(image)):
			new_row += [image[row][col]]
		new_img.append(new_row)
	return new_img

#Problem 15
def rotate90cw(image):
	new_img = []
	for col in range(len(image[0])):
		new_row = []
		for row in range(len(image) - 1, -1, -1):
			new_row += [image[row][col]]
		new_img.append(new_row)
	return new_img
#End Problem 15

#Used for testing, delete before submit
def gen_mask(gscale_img):
	maske_img = []
	for row in range(len(gscale_img)):
		new_row = []
		for px in range(len(gscale_img[row])):
			if gscale_img[row][px] > 150.5:
				new_row += [0]
			else:
				new_row += [1]
		maske_img.append(new_row)
	return maske_img

#Problem 16
def mask_img(image, mask):
	new_img = []
	for row in range(len(image)):
		new_row = []
		for px in range(len(image[row])):
			if mask[row][px]:
				new_row += [image[row][px]]
			else:
				new_row += [0]
		new_img.append(new_row)
	return new_img

#Problem 17
def cvt_grayscale(image):
	new_img = []
	for row in range(len(image)):
		new_row = []
		for px in range(len(image[row])):
			total = 0
			for px_val in image[row][px]:
				total += px_val
			new_row += [total // len(image[row][px])]
		new_img += [new_row]
	return new_img
#End Problem 17

def limit_255_rgb(image):
	lim_img = []
	for row in image:
		new_row = []
		for px_rgb in row:
			new_px = []
			for px in px_rgb:
				px = px // 1
				if px >= 255:
					new_px += [255]
				elif px <= 0:
					new_px += [0]
				else:
					new_px += [px]
			new_row.append(new_px)
		lim_img.append(new_row)
	return lim_img

#Problem 18
def filter_sunset(image, adjustment):
	new_img = []
	for row in range(len(image)):
		new_row = []
		for px_rgb in range(len(image[row])):
			new_px = []
			for i in range(len(image[row][px_rgb])):
				if not i:
					new_px += [image[row][px_rgb][i] + adjustment]
				else:
					new_px += [image[row][px_rgb][i]]
			new_row += [new_px]
		new_img += [new_row]
	return limit_255_rgb(new_img)

#Problem 19
def filter_sepia(image):
	new_img = []
	for row in range(len(image)):
		new_row = []
		for px_rgb in range(len(image[row])):
			new_px_rgb = []

			r_val = image[row][px_rgb][0]
			g_val = image[row][px_rgb][1]
			b_val = image[row][px_rgb][2]

			new_px_rgb += [.393 * r_val + .769 * g_val + .189 * b_val]
			new_px_rgb += [.349 * r_val + .686 * g_val + .168 * b_val]
			new_px_rgb += [.272 * r_val + .534 * g_val + .131 * b_val]

			new_row += [new_px_rgb]
		new_img += [new_row]
	return limit_255_rgb(new_img)
#End Problem 19

def combine_2pics(image1, image2):
	new_img = []
	for row in range(len(image1)):
		new_img += [image1[row] + image2[row]]
	return new_img

def make_1_color(image, color):
	new_img = []
	for row in range(len(image)):
		new_row = []
		for px_rgb in range(len(image[row])):
			if color == "red":
				new_px_rgb = [image[row][px_rgb][0], 0, 0]
			elif color == "green":
				new_px_rgb = [0, image[row][px_rgb][1], 0]
			elif color == "blue":
				new_px_rgb = [0, 0, image[row][px_rgb][2]]
			new_row.append(new_px_rgb)
		new_img.append(new_row)
	return new_img

#Problem 20
def warhol_effect(image):
	TL = []
	TR = make_1_color(image, "red")
	BL = make_1_color(image, "blue")
	BR = make_1_color(image, "green")

	for row in range(len(image)):
		new_row = []
		for px_rgb in range(len(image[row])):
			new_px_rgb = [0, image[row][px_rgb][1], image[row][px_rgb][2]]
			new_row.append(new_px_rgb)
		TL.append(new_row)

	top = combine_2pics(TL, TR)
	btm = combine_2pics(BL, BR)
	top.extend(btm)

	return top
#End Problem 20

def avg_adjacent_px(img, col, row, rgb_idx):
	total = 0
	num_vals = 1
	total += img[row][col][rgb_idx]

	if row > 0:
		total += img[row - 1][col][rgb_idx]
		num_vals += 1
		if col > 0:
			total += img[row - 1][col - 1][rgb_idx]
			num_vals += 1
		if col < len(img[0]) - 1:
			total += img[row - 1][col + 1][rgb_idx]
			num_vals += 1
	if col > 0:
		total += img[row][col - 1][rgb_idx]
		num_vals += 1
	if col < len(img[0]) - 1:
		total += img[row][col + 1][rgb_idx]
		num_vals += 1
	if row < len(img) - 1:
		total += img[row + 1][col][rgb_idx]
		num_vals += 1
		if col > 0:
			total += img[row + 1][col - 1][rgb_idx]
			num_vals += 1
		if col < len(img[0]) - 1:
			total += img[row + 1][col + 1][rgb_idx]
			num_vals += 1
	return total // num_vals

#Problem 21
def filter_boxblur(image):
	new_img = []
	for row in range(len(image)):
		new_row = []
		for col in range(len(image[0])):
			new_px = []
			for px in range(len(image[row][col])):
				new_px += [avg_adjacent_px(image, col, row, px)]
			new_row += [new_px]
		new_img += [new_row]
	return new_img
#End Problem 21

def get_gx_kernel(img, row, col):
	new_px = []
	for rgb_idx in range(len(img[row][col])):
		total = 0
		if row > 0 and col > 0:
			total += img[row - 1][col - 1][rgb_idx] * -1
		if row > 0 and col < len(img[0]) - 1:
			total += img[row - 1][col + 1][rgb_idx] * 1
		if col > 0:
			total += img[row][col - 1][rgb_idx] * -2
		if col < len(img[0]) - 1:
			total += img[row][col + 1][rgb_idx] * 2
		if row < len(img) - 1 and col > 0:
			total += img[row + 1][col - 1][rgb_idx] * -1
		if row < len(img) - 1 and col < len(img[0]) - 1:
			total += img[row + 1][col + 1][rgb_idx] * 1
		new_px += [total]
	return new_px

def get_gy_kernel(img, row, col):
	new_px = []
	for rgb_idx in range(len(img[row][col])):
		total = 0
		if row > 0:
			total += img[row - 1][col][rgb_idx] * -2 
		if row > 0 and col > 0:
			total += img[row - 1][col - 1][rgb_idx] * -1
		if row > 0 and col < len(img[0]) - 1:
			total += img[row - 1][col + 1][rgb_idx] * -1
		if row < len(img) - 1:
			total += img[row + 1][col][rgb_idx] * 2
		if row < len(img) - 1 and col > 0:
			total += img[row + 1][col - 1][rgb_idx] * 1
		if row < len(img) - 1 and col < len(img[0]) - 1:
			total += img[row + 1][col + 1][rgb_idx] * 1
		new_px += [total]
	return new_px

#Problem 22
def find_edges(image):
	new_img = []
	for row in range(len(image)):
		new_row = []
		for col in range(len(image[0])):
			new_px = []
			gx = get_gx_kernel(image, row, col)
			gy = get_gy_kernel(image, row, col)
			for item in range(len(gx)):
				new_px += [((gx[item] ** 2) + (gy[item] ** 2)) ** 0.5]
			new_row += [new_px]
		new_img += [new_row]
	return limit_255_rgb(new_img)