a = 0


def test(_):
    global b
    for x in range(3):
        if x == 0:
            b = 3
            print(b)
        else:
            c = b + 1
            print(c)


test(a)
print("/////")
print(b)