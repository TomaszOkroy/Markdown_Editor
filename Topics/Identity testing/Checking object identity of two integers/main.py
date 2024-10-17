a = int(input())
b = int(input())

def are_same_object(a, b):
    return a is b

print(are_same_object(a, b))
