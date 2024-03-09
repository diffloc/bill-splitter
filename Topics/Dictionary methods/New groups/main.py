# the list with classes; please, do not modify it
groups = ['1A', '1B', '1C', '2A', '2B', '2C', '3A', '3B', '3C']

# your code here
num_groups = int(input())
children = [int(input()) for _ in range(num_groups)]

classes = {group: None for group in groups}


for i in range(num_groups):
    classes.update({groups[i]: children[i]})

print(classes)
