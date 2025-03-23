months = {
    "January": 1,
    "February": 2,
    "March": 3,
    "April": 4,
    "May": 5,
    "June": 6,
    "July": 7,
    "August": 8,
    "September": 9,
    "October": 10,
    "November": 11,
    "December": 12
}

while True:
    inpu = input("Date: ").strip()
    if inpu[0].isdigit():
        try:
            if inpu[0].isdigit():
                inpulist = inpu.split("/")
                for i in range(len(inpulist)):
                    try:
                        inpulist[i] = int(inpulist[i])
                    except:
                        continue

            res = ""

            if len(inpulist) == 3 and inpulist[2] >= 1:
                res += str(inpulist[2]) + "-"
            else:
                continue

            if 1 <= inpulist[0] <= 12:
                if inpulist[0] < 10:
                    res += "0" + str(inpulist[0]) + "-"
                else:
                    res += str(inpulist[0]) + "-"
            else:
                continue

            if 1 <= inpulist[1] <= 31:
                if inpulist[1] < 10:
                    res += "0" + str(inpulist[1])
                else:
                    res += str(inpulist[1])
            else:
                continue

            print(res)

            break

        except:
            continue
    elif inpu[0].isalpha():
        try:
            inpulist = inpu.split(" ")
            if len(inpulist) != 3:
                continue
            
            try:
                inpulist[1] = int(inpulist[1].replace(",", ""))
                inpulist[2] = int(inpulist[2])
            except:
                continue
            
            res = ""

            if inpulist[0] in months:
                if inpulist[2] >= 0:
                    res += str(inpulist[2]) + "-"
                else:
                    continue
                
                res += str(months[inpulist[0]]) + "-"
                
                if 1 <= inpulist[1] <= 31:
                    if inpulist[1] < 10:
                        res += "0" + str(inpulist[1])
                    else:
                        res += str(inpulist[1])
                else:
                    continue

                print(res)

                break
        except:
            continue
    else:
        continue