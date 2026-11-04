
n = int(input("Nhập số lượng tối đa n (1-30): "))

while n < 1 or n > 30:
    print("n không hợp lệ!")
    n = int(input("Nhập lại n: "))

dem = 0
tong = 0

for i in range(1, n + 1):
    so = int(input("Nhập số nguyên thứ " + str(i) + ": "))

    if so == -1:
        print("Đã nhận tín hiệu kết thúc!")
        break

    dem = dem + 1
    tong = tong + so

print("-------------------")
print("Số lượng giá trị đã nhập:", dem)
print("Tổng các giá trị:", tong)

if dem > 0:
    trung_binh = tong / dem
    print("Trung bình cộng:", trung_binh)
else:
    print("Không thể tính trung bình!")
