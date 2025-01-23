res = ""

with open("input.txt") as file:
    inpu = file.read().replace("\n", "")
    for i in range(len(inpu)):
        is_num = False
        try:
            int(inpu[i])
            is_num = True
        except:
            pass

        if not is_num:
            res += inpu[i].strip()

    print(res)