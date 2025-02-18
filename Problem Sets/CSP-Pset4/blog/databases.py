import csv
import datetime

def load_database(users_path, posts_path, follows_path):
	data = []

	users = {}
	with open(users_path, "r") as f:
		reader = csv.DictReader(f)
		for row in reader:
			users[row["username"]] = row["password"]	
	data.append(users)

	posts = []
	with open(posts_path, "r") as f:
		reader = csv.DictReader(f)
		for row in reader:
			posts.append(row)	
	data.append(posts)

	follows = {}
	with open(follows_path, "r") as f:
		reader = csv.DictReader(f)
		for row in reader:
			if row["follower"] not in follows:
				follows[row["follower"]] = [row["following"]]
			else:
				follows[row["follower"]].append(row["following"])
	data.append(follows)

	return data

def login(users):
	while True:
		username = input("Enter a Username: ").strip()
		if username not in users.keys():
			print("Invalid Username!")
			continue

		passwd = input("Enter a Password: ")
		if passwd != users[username]:
			print("Invalid Password!")
			continue

		return username

def register(users, users_path):
	print("\"exit()\" to exit")
	while True:
		new_user = input("Enter a New Username (NO SPACES!): ").strip()
		if new_user == "exit()":
			break
		if new_user in users.keys():
			print("User Already Exists!")
			continue
		new_passwd = input("Enter a New Password: ").strip()

		users[new_user] = new_passwd
		with open(users_path, "a", newline="") as f:
			csvwrit = csv.writer(f, quoting=csv.QUOTE_ALL)
			csvwrit.writerow([new_user, new_passwd])

def make_post(active_user, posts, posts_path):
	print("\"exit()\" to exit")
	post = {}

	post["user"] = active_user

	title = input("Enter a Post Title: ").strip()
	if title == "exit()":
		return
	else:
		post["title"] = title

	content = input("Enter Post Content: ").strip()
	if content == "exit()":
		return
	else:
		post["content"] = content

	post["timestamp"] = datetime.datetime.now().strftime("%Y-%m-%d at %H:%M")

	posts.append(post)
	with open(posts_path, "a", newline="") as f:
			csvwrit = csv.writer(f, quoting=csv.QUOTE_ALL)
			csvwrit.writerow([post["user"], post["timestamp"], post["title"], post["content"]])










if __name__ == "__main__":
	pass