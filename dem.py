print("nhap ki tu can dem: ")
n = input()
print("nhap chuoi: ")
chuoi = input()
dem = 0
for i in chuoi:
    if n == i:
        dem += 1
print(f"so lan suat hien cua ki tu {n} trong chuoi {chuoi} la: {dem}")
