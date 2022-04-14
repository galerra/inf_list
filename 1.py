#шебанг
if __name__ == "__main__":
    path = input("Enter a path: ")
    with open(path, "r", encoding="utf-8") as file_obj:
        a = file_obj.readlines()
    big = 0
    for i in a:
        if len(i) > big:
            big = len(i)
    for j in a:
        if len(j) == big:
            print(j)
