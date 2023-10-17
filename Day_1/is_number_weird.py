#Given an integer, , perform the following conditional actions:
# If  is odd, print Weird
# If  is even and in the inclusive range of 2 to 5, print Not Weird
# If  is even and in the inclusive range of 6 to 20, print Weird
# If  is even and greater than 20, print Not Weird

#Constraints: n should be in the inclusive range of 1 to 100





if __name__ == '__main__':
    n = int(input().strip())

if 1 <= n <= 100:
    if n % 2 == 1:
        print("Weird")

    elif n % 2 == 0:
        if 2 <= n <= 5:
            print("Not Weird")
        elif 6 <= n <= 20:
            print("Weird")
        elif n >= 20:
            print("Not Weird")