import random

def main():
    level = get_level()
    for i in range(10):
        int1 = generate_integer(level)
        int2 = generate_integer(level)
        correct_ans = int1 + int2

        for i in range(3):     
            ans = input(f"{int1} + {int2} = ")

            if ans == str(correct_ans):
                break
            else:
                earn_score = False

            print("EEE")


def get_level():
    while True:
        level = input("Level: ").strip()

        try:
            level = int(level)
        except:
            continue
        
        if level not in (1, 2, 3):
            continue

        return level

def generate_integer(level):
    res = ""
    for i in range(level):
        res += str(random.randint(0, 9))
    return int(res)

if __name__ == "__main__":
    main()