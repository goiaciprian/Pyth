
def Lazi():
    l = int(input("::"))
    h = int(input("::"))
    cate = 0
    times = 0

    for i in range(h):
        if (cate + l) <= h:
            cate += l
            times += 1

    print(times)

if __name__ == "__main__":
    Lazi()
