list = []
print("so phan tu cua list: ")
n = int(input())
print("nhap tong: ")
tong = int(input())
def nhaplist(n):
    for i in range(1, n+1):
        list.append(input())
def phantach(list):
    for i in list:
        i = int(i)
        for j in list:
            j = int(j)
            if i != j and i + j == tong:
                print(f"cac cap co tong bang so da nhap la {i}, {j}")
            else:
                return "khong co cap nap thua mang bang so da nhap"
nhaplist(n)
print(list)
phantach(list)