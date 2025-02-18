import databases
from prntandinput import print_ops, get_response, print_post

def main():
	users_path = "database/users.csv"
	posts_path = "database/posts.csv"
	follows_path = "database/follows.csv"

	users, posts, follows = databases.load_database(users_path, posts_path, follows_path)
	active_user = None

	while True:
		if not active_user:
			main_menu_ops = ["Login", "Register", "Exit"]
			print_ops(main_menu_ops)

			match get_response(main_menu_ops):
				case 0:
					active_user = databases.login(users)
				case 1:
					while True:
						register_ops = ["Register", "Back to Main Menu"]
						print_ops(register_ops)
						if get_response(register_ops) == 0:
							databases.register(users, users_path)
						break
				case 2:
					break
		else:
			logged_in_ops = ["Make Post", "Follow User", "View My Posts", "View Followed Posts", "Search User Posts", "Logout"]
			print_ops(logged_in_ops)

			match get_response(logged_in_ops):
				case 0:
					databases.make_post(active_user, posts, posts_path)
				case 1:
					databases.follow_user(active_user, follows, follows_path, users)
				case 2:
					for post in databases.fetch_user_posts(active_user, posts, posts_path):
						print_post(post)
				case 3:
					for post in databases.fetch_followed_posts(follows[active_user], posts, posts_path):
						print_post(post)
				case 4:
					for post in databases.fetch_other_user_posts(posts, posts_path, users):
						print_post(post)
				case 5:
					active_user = None

if __name__ == "__main__":
	main()