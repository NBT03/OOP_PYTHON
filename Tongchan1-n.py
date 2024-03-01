print("nhap n: ")
n = int(input())
tong = 0
for i in range (1, n+1):
    i = int(i)
    if(i % 2 == 0):
        tong += i
print(f"tong cua cac so chan tu 1 den n la: {tong}")