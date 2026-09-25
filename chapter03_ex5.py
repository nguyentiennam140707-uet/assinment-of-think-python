def bottle_verse(n):
    print(str(n) + " " + "bottles of beer on the wall,")
    print(str(n) + " " + "bottles of beer.")
    print("Take one down, pass it around,")
    print(str(n - 1) + " " + "bottles of beer on the wall.")

#bottle_verse(99)
for i in range(99, 0, -1):
    bottle_verse(i)
    print()