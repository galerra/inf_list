#шебанг
if __name__ == "__main__":
    lst = list(map(int, input().split()))
    for i, e in enumerate(lst):
        mn = min(range(i, len(lst)), key=lst.__getitem__) #енумирайт
        lst[i], lst[mn] = lst[mn], e
    print(lst)
