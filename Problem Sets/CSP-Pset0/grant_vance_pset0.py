#Problem 1
def rect_area(length, width):
	return length * width

#Problem 2
def circ_area(radius):
	return (2 * 3.14) * radius

#Problem 3
def cylinder_area(radius, height):
	return (2 * 3.14 * radius * height) + (2 * 3.14 * (radius ** 2))

#Problem 4
def sphere_surface_area(radius):
	return 4 * 3.14 * (radius ** 2)

#Problem 5
def sum_double(a, b):
	if a == b:
		return (a + b) * 2
	else:
		return (a + b)

#Problem 6
def in_range(num1, num2):
	if (num1 >= 20 and num1 <= 30) and (num2 >= 20 and num2 <= 30):
		return True
	elif (num1 >= 90 and num1 <= 100) and (num2 >= 90 and num2 <= 100):
		return True
	else:
		return False

#Problem 7
def distance(x, y):
	return ((x ** 2) + (y ** 2)) ** (1 / 2)

#Problem 8
def open_gate(workday, gate_activated, gate_up):
	if workday == True and gate_activated == True and gate_up == False:
		return True
	else:
		return False

#Problem 9
def has_discount(age, had_accident):
	if age >= 24 and had_accident == False:
		return True
	else:
		return False

#Problem 10
def should_apply(gpa, act_score):
	if gpa >= 3.9 and act_score > 31:
		return True
	elif gpa >= 4.25 or act_score >= 34:
		return True
	else:
		return False

#Problem 11
def oil_light(miles, days):
	if miles > 10000 or days > 365:
		return True
	else:
		return False

#Problem 12
def abs_val(x):
	if x < 0:
		return 0 - x
	else:
		return x
#End Problem 12

def min_num(a, b):
	if a < b:
		return a
	else:
		return b

#Problem 13
def closest_tens(a, b):
	a_rem = min_num(a % 10, 10 - (a % 10))
	b_rem = min_num(b % 10, 10 - (b % 10))

	if a_rem < b_rem:
		return a
	elif a_rem > b_rem:
		return b
	else:
		return a

#Problem 14
def get_ticket_price(price, flying_soon, open_seat_pct):
	if flying_soon == False:
		if open_seat_pct < 0.25:
			return 1.25 * price
		else:
			return price
	else:
		if open_seat_pct < 0.10:
			return price * 1.40
		elif open_seat_pct >= 0.50:
			return 0.85 * price
		else:
			return price

#Problem 15
def is_special(num):
	if (num % 10) == 2:
		return True
	elif (num % 10) == 4:
		return True
	elif (num % 10) == 8:
		return True
	else:
		return False

#Problem 16
def rev_num(n):
	return int((n / 100) + ((int(n / 10) % 10) * 10) + ((n % 10) * 100))

#Problem 17
def is_leap_year(year):
	if ((year / 4) == (int(year / 4))) and ((year / 100) != (int(year / 100))):
		return True
	if ((year / 100) == (int(year / 100))):
		if ((year / 400) == (int(year / 400))):
			return True
		else:
			return False
	return False

#Problem 18
def first_day(year):
	Y = (year % 100) - 1
	C = int(year / 100)

	dayNum = ((29 - (2 * C) + Y) + int(Y / 4) + int(C / 4)) % 7

	if dayNum == 0:
		day = "Sunday"
	elif dayNum == 1:
		day = "Monday"
	elif dayNum == 2:
		day = "Tuesday"
	elif dayNum == 3:
		day = "Wednesday"
	elif dayNum == 4:
		day = "Thursday"
	elif dayNum == 5:
		day = "Friday"
	elif dayNum == 6:
		day = "Saturday"
	return day

#Problem 19
def day_of_year(month, day, year):
	daysBefore = 0

	if month > 1:
		daysBefore += 31
	if month > 2:
		if is_leap_year(year) == True:
			daysBefore += 29
		else:
			daysBefore += 28
	if month > 3:
		daysBefore += 31
	if month > 4:
		daysBefore += 30
	if month > 5:
		daysBefore += 31
	if month > 6:
		daysBefore += 30
	if month > 7:
		daysBefore += 31
	if month > 8:
		daysBefore += 31
	if month > 9:
		daysBefore += 30
	if month > 10:
		daysBefore += 31
	if month > 11:
		daysBefore += 30

	return daysBefore + day

#End Problem 19
def first_day_num(year):
	Y = (year % 100) - 1
	C = int(year / 100)

	dayNum = ((29 - (2 * C)) + Y) + (Y // 4) + (C // 4) % 7
	return dayNum

#Problem 20
def day_of_week(month, day, year):
	firstDay = first_day_num(year)
	dayOfYear = day_of_year(month, day, year)
	dayNum = (firstDay + (dayOfYear - 1)) % 7

	if dayNum == 0:
		return "Sunday"
	elif dayNum == 1:
		return "Monday"
	elif dayNum == 2:
		return "Tuesday"
	elif dayNum == 3:
		return "Wednesday"
	elif dayNum == 4:
		return "Thursday"
	elif dayNum == 5:
		return "Friday"
	elif dayNum == 6:
		return "Saturday"