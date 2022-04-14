#шебанг
if __name__ == "__main__":
    lst = list(map(int, input().split()))
    cop_lst = lst.copy()
    cop_lst.sort()
    if lst == cop_lst:
        print('Yeees')
    else:
        print('Nooo')
