# This is a sample Python script.

def fibonacci(term, pop):
    child, parent = 1, 1
    for i in range(term-1):
        child, parent = parent, parent + (child * pop)

    print(str(child))


n = 32
k = 2
fibonacci(n, k)
