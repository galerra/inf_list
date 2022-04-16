#шебанг

def func(strr, sstr):
    for i in range(len(strr)):
        c = 0
        
        if strr[i] == sstr[0]:
            for j in range(len(sstr)):
                
                if strr[i + j] == sstr[j]:
                    c += 1
                    if c == len(sstr):
                        return i
    return False


if __name__ == "__main__":
    x = input().strip()
    y = input().strip()
    p = func(x, y)
    if p is not False:
        print(p + 1)
    else:
        print("No")
