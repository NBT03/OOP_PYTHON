print("nhap n: ")
n = int(input())
def giaithua(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * giaithua(n-1)
print(f"giai thua cua {n} la: {giaithua(n)}")