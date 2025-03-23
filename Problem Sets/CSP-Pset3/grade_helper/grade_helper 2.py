import csv

def grade_loader(filepath):
	grades = []
	with open(filepath, "r") as f:
		reader = csv.reader(f)
		for row in reader:
			grades.append(row)
	return (grades[0], grades[1:])

if __name__ == "__main__":
	all_grades = grade_loader("grades_data.csv")
	solution = all_grades[0]
	student_data = all_grades[1]

	print(solution)
	print(student_data)