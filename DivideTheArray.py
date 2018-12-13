n = input("Enter an integers: ").strip().split(" ")
for ix, numb in enumerate(n):
    if (ix + 1) % 2 == 0:
        if int(numb) % 2 == 0:
            print(numb)