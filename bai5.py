def tong_uoc(n):
    # Ham tinh tong cac uoc so cua n (tru n)
    tong = 0
    for i in range(1, n):
        if n % i == 0:
            tong += i
    return tong

def so_hoan_thien(n):
    # Kiem tra xem n co phai so hoan thien khong
    return tong_uoc(n) == n

def so_thinh_vuong(n):
    # Kiem tra xem n co phai so thinh vuong khong
    return tong_uoc(n) > n



n = int(input("Nhap mot so nguyen duong n: "))
if n <= 0:
    print("Vui long nhap mot so nguyen duong lon hon 0.")
else:
    tong_uoc_so = tong_uoc(n)  # Tinh tong cac uoc so
    print("Tong cac uoc so (tru",n,") = ",tong_uoc_so)

    if so_hoan_thien(n):
        print("So",n,"la so hoan thien.")
    else:
        print("So",n,"khong phai la so hoan thien.")

    if so_thinh_vuong(n):
        print("So",n,"la so thinh vuong.")
    else:
        print("So",n,"khong phai la so thinh vuong.")

