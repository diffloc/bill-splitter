try:
    full_name = input()
    name, surname = full_name.split()
except ValueError:
    print("You need to enter exactly 2 words. Try again!")
else:
    print(f'Welcome to our party, {name} {surname}')
