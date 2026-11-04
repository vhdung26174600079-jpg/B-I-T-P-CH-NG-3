n = int(input("Nhập số lượng n (1-30): "))
while n < 1 or n > 30:
    print("n không hợp lệ!")
    n = int(input("Nhập lại n (1-30): "))
tong = 0
for i in range(1, n + 1):
    so = int(input("Nhập số nguyên thứ " + str(i) + ": "))
    tong = tong + so
trung_binh = tong / n
print("Số lượng:", n)
print("Tổng các số:", tong)
print("Trung bình cộng:", trung_binh)
