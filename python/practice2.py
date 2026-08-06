#Practice with two functions 

def outer(x):
    def inner(y):
        return x + y
    return inner

f = outer(10)
g = outer(9)

print(f(20))
print(g(20))

print(g(f(20)))