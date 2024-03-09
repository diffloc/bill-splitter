# Initialize empty int list
int_list = []

# Prompt user for number of elements (n)
n = int(input())

# Prompt user for 'n' values
for i in range(0, n):
    int_value = int(input())
    # Add int_value to int_list
    int_list.append(int_value)

# Iterate through int_list -- if int is multiple of 7
# output int squared

for j in int_list:
    if j % 7 == 0:
        print(j ** 2)
