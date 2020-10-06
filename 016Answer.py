x = input().split(" ")

length = int(x[0])
horizontalcut = int(x[1])
verticalcut = int(x[2])

print(max(length-horizontalcut,horizontalcut) * max(length-verticalcut,verticalcut) * 4)
