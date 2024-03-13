# def divide():
#     for i in range(2000, 3201):
#         if i % 7 == 0 and i % 5 != 0:
#             print(i, end = ',')
# divide()
#________________________________________________#
#Bai2 Viết một chương trình có thể tính giai thừa của một số cho trước. Kết quả được in thành chuỗi trên một dòng, phân tách bởi dấu phẩy. Ví dụ, số cho trước là 8 thì kết quả đầu ra phải là 40320.
# print('nhap vao so can tinh giai thua:')
# n = int(input())
# def giaithua(n):
#     if n == 1 or n == 0:
#         return 1
#     else:
#         return n * giaithua(n-1)
# print(f'giai thua cua {n} la: {giaithua(n)}')
# def giaithua(n):
#     tich = 1
#     for i in range(1, n+1):
#         tich *= i
#     return tich
# print(f'giai thua cua {n} la: {giaithua(n)}')
#Bai 3 Với số nguyên n nhất định, hãy viết chương trình để tạo ra một dictionary chứa (i, i*i) như là số nguyên từ 1 đến n (bao gồm cả 1 và n) sau đó in ra dictionary này.
# print("nhap n:")
# n = int(input())
# dic = dict()
# for i in range(1, n+1):
#     dic[i] = i*i
# print(dic)
# Bài 4:
# Câu hỏi:
#
# Viết chương trình chấp nhận một chuỗi số, phân tách bằng dấu phẩy từ giao diện điều khiển, tạo ra một danh sách và một tuple chứa mọi số.
#
# Ví dụ: Đầu vào được cung cấp là 34,67,55,33,12,98 thì đầu ra là:
#
# ['34', '67', '55', '33', '12', '98']
# ('34', '67', '55', '33', '12', '98')
# values = input('nhap cac gia tri dau vao:')
# l = values.split(",")
# t = tuple(l)
# print(l)
# print(t)
# Bài 5:
# Câu hỏi:
#
# Định nghĩa một class có ít nhất 2 method:
#
# getString: để nhận một chuỗi do người dùng nhập vào từ giao diện điều khiển.
# printString: in chuỗi vừa nhập sang chữ hoa.
# Thêm vào các hàm kiểm tra đơn giản để kiểm tra method của class.
# class Input_out():
#     def __init__(self):
#         self.s = " "
#     def get_sting(self):
#         self.s = input("nhap chuoi")
#     def print_string(self):
#         print(self.s.upper())
# obj = Input_out()
# obj.get_sting()
# obj.print_string()
# viet mot method tinh toan gia tri binh phuong cua 1 so
# class number():
#     def __init__(self, n):
#         self.n = n
#     def binhphuong(self):
#         return self.n * self.n
# print("nhap so can binh phuong: ")
# n = int(input())
# obj = number(n)
# print(obj.binhphuong())
# Bài 8:
# Câu hỏi:
#
# Định nghĩa một lớp gồm có tham số lớp và có cùng tham số instance
#
# Gợi ý:
#
# Khi định nghĩa tham số instance, cần thêm nó vào __init__
# Bạn có thể khởi tạo một đối tượng với tham số bắt đầu hoặc thiết lập giá trị sau đó.
# class Person:
#     name = "person"
#     def __init__(self, name = None):
#         self.name = name
# Jerri = Person("person")
# print(Person.name, Jerri.name)
# Jerri.name = "lmao"
# print(Person.name, Jerri.name)
# Bài 9:
# Câu hỏi: Tính tuổi dựa trên ngày tháng năm sinh nhập vào.
#
# Ví dụ: Nhập vào ngày tháng năm sinh dạng y/m/d, hãy tính tuổi của người này.
#
# Gợi ý: Sử dụng module datetime. Sử dụng datetime, chúng ta có thể tìm tuổi bằng cách trừ năm sinh cho năm hiện tại.
import  datetime as d
print(" vui long nhap ngay thang nam sinh cua ban: ")
day = int(input())
month = int(input())
year = int(input())
current_year = d.date.today().year
current_month = d.date.today().month
current_day = d.date.today().day
def tuoi():
    nam_tuoi = current_year - year
    thang_tuoi = current_month - month
    if thang_tuoi < 0:
        nam_tuoi = nam_tuoi - 1
        thang_tuoi = abs
    ngay_tuoi = abs(current_day - day)
    print(f"tuoi cua nguoi nhap vao la: {nam_tuoi}, {thang_tuoi}, {ngay_tuoi}")

