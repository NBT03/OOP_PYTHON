print("Perfect Number")
n = int(input())
def perfect_number(a):
    tong = 0
    for i in range(1, n):
        i = int(i)
        if n % i == 0:
            print(i)
            tong = tong + i
    print(tong)
    if tong == a:
        print("Perfect Number")
perfect_number(n)