if __name__ == "__main__":
    path = input("Enter a path: ")
    with open(path, "r", encoding="utf-8") as file_obj:
        lst = file_obj.readlines()
    for i in range(len(lst)):
        for j in range(len(lst[i])):
            if j != len(lst[i]) - 1: #индексация с нуля
                if lst[i][j] == lst[i][j+1]:
                    print(lst[i])
                    break #конец
