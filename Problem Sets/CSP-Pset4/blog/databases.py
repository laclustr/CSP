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

		passwd = input("Enter a Password: ").strip()
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

def follow_user(active_user, follows, follows_path, users):
	print("\"exit()\" to exit")

	followed_user = input("Enter a User to Follow: ").strip()

	if (followed_user == "exit()" or 
		followed_user not in users.keys() or 
		followed_user == active_user):
		return

	if follows.get(active_user):
		follows[active_user].append(followed_user)
	else:
		follows[active_user] = [followed_user]

	with open(follows_path, "a", newline="") as f:
		csvwrit = csv.writer(f, quoting=csv.QUOTE_ALL)
		csvwrit.writerow([active_user, followed_user])

def fetch_user_posts(user, posts, posts_path):
	usr_posts = []
	for post in posts:
		if post["user"] == user:
			usr_posts.append(post)

	return sorted(usr_posts, key=lambda x: x["timestamp"], reverse=False)

def fetch_followed_posts(follow_list, posts, posts_path):
	followed_posts = []
	for user in follow_list:
		for post in posts:
			if post["user"] == user:
				followed_posts.append(post)

	return sorted(followed_posts, key=lambda x: x["timestamp"], reverse=False)

def fetch_other_user_posts(posts, posts_path, users):
	while True:
		user = input("Enter a User: ").strip()
		if user not in users:
			continue

		usr_posts = []
		for post in posts:
			if post["user"] == user:
				usr_posts.append(post)

		return sorted(usr_posts, key=lambda x: x["timestamp"], reverse=False)

if __name__ == "__main__":
	pass