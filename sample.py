#l = [1, 'a', 3.4]
t = (1, 2, 3, [4, 5, 6])

#t = (1, 2, 3, [4, 50, 6])
t[3][1] = 50
print(t) 
 
l = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
l = [j for i in l for j in i]
print(l)

def dec(func):
    def inner(a, b):
        if b == 0:
            print("denominator should not be 0")
        func()
    return inner

@dec
def divide(a, b):
    return a/b

