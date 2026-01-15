n = int(input().strip())  # Convert string to integer

if (n % 2) != 0:
    print("Weired")
else:
    if 2<= n <= 5:
        print("Not Weired")
    elif 6<= n <= 20:
        print("Weired")
    else:
        print("Not Weired")