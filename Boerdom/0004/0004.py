while True:
    response = input("Fraction: ")
    inputlis = response.strip().split("/")

    try:
        for i in range(len(inputlis)):
            inputlis[i] = int(inputlis[i])
    except ValueError:
        continue
    
    if not inputlis[1]:
        continue

    res = int((inputlis[0] / inputlis[1]) * 100)
    
    match res:
        case 0:
            print("E")
            break
        case 100:
            print("F")
            break
        case _:
            print(f"{res}%")
            break