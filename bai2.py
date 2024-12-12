n= int(input("Nhap N: "))

def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    elif n > 2:
        return fibonacci(n-1) + fibonacci(n-2)

vt= int(input("Nhap vi tri: "))

def lay_phan_tu(vt):
    return fibonacci(vt)

print("Gia tri cua phan tu la: ",lay_phan_tu(vt))



def day(n):
    return [fibonacci(i) for i in range(1, n+1)]
print(day(n))