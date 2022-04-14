#шебанг
if __name__ == "__main__":
    lst = []
    i = 1
    c = 0
    while True:
        i = float(input('Введите число:'))
        if i == 0:
            break
        else:
            lst.append(i)
    for j in lst:
        if j == max(lst):
            c += 1
    print(c)
