index = int(input())
exception = dir(locals()['__builtins__'])[index]

print(exception)
