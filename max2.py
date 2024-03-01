list = []
print("nhap so phan tu cua list: ")
n = int(input())
for i in range(1, n+1):
    list.append(input())
def max2(list):
    m = 0
    n = 0
    for i in list:
        i = int(i)
        if i > m:
            m = i
    for i in list:
        i = int(i)
        if i > n and i < m :
            n = i
    return n
print(max2(list))
