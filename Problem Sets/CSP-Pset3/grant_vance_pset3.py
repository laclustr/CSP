from grade_helper import grade_helper as gh
from images_csp import images_csp as img

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

#Problem 4
#Problem 5
#Problem 6
#Problem 7

gscale_img = img.load_grayscale("images_csp/cat.jpg")

#Problem 8
def threshold(image, threshold):
	new_img = []
	for row in image:
		new_row = []
		for px in row:
			if px > threshold:
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

img.show_image(adj_brightness(gscale_img, 100))











