if __name__ == "__main__":
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    c = a + b
    c.sort()
    print(c)
