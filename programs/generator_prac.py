num = (x*2 for x in range(1,11))

while True:
    try:
        print(next(num))
    except StopIteration:
        break