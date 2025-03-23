def print_ops(ops):
	for op in range(len(ops)):
		print(f"{op + 1}). {ops[op]}")

def get_response(ops):
	while True:
		num = input("Enter an Option: ").strip()
		num = int(num) - 1
		if num not in range(len(ops)):
			continue
		return num

def print_post(post):
	print("+" * 37)
	print(f"{"=" * 4} {post["title"]} {"=" * 4}")
	print(f"{"=" * 2} posted by {post["user"]} on {post["timestamp"]} {"=" * 2}")
	print(post["content"])
	print("+" * 37)

if __name__ == "__main__":
	pass