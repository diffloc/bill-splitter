def square(n):
    if n >= 0:
        print(n * n)
    else:
        raise ValueError()


value = int(input())
try:
    square(value)
except ValueError as e:
    print("Input must not be less than 0")
