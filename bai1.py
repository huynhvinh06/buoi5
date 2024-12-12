#Nhap doanh thu va chi phi
dt= float(input("Nhap doanh thu: "))
cp= float(input("Nhap chi phi: "))
#tinh ROI
roi= (dt - cp)/cp

print("Chi so ROI la ",roi)

if roi >= 0.75:
    print("Nen dau tu du an")
else:
    print("Khong nen dau tu du an")