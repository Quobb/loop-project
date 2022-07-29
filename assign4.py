fact=int(input())
factorial=fact

i = factorial-1
while i > 1:
    factorial=factorial*i
    i=i-1
    print(factorial)