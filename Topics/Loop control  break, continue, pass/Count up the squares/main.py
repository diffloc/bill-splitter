# put your python code here
sum_numbers = 0
sum_squares = 0
while True:
    number = int(input())
    sum_numbers += number
    sum_squares += number ** 2
    if sum_numbers == 0:
        break


print(sum_squares)
