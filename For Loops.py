for i in range(99, 0, -1):
    print(i, "bottles of Pepsi on the wall, take one down, pass it around", i - 1, "bottles of Pepsi on the wall")

    if i == 2:
        print("1 bottle of Pepsi on the wall, take one down, pass it around 0 bottles of Pepsi on the wall")
        print("No more bottles of Pepsi on the wall, no more bottles of Pepsi, Take one down pass it around, "
              "no more bottles of Pepsi on the wall")
        print("Go to the store and buy some more, 99 bottles of Pepsi on the wall")
        break
