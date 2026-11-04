
n = int(input("Nhập số lượng giá trị (1-30): "))

while n < 1 or n > 30:
    print("n không hợp lệ!")
    n = int(input("Nhập lại n: "))

dem_hop_le = 0
dem_khong_hop_le = 0
tong = 0

for i in range(1, n + 1):
    gia_tri = float(input("Nhập giá trị thứ " + str(i) + ": "))

    if gia_tri < 0 or gia_tri > 100:
        print("Giá trị không hợp lệ!")
        dem_khong_hop_le = dem_khong_hop_le + 1
        continue

    dem_hop_le = dem_hop_le + 1
    tong = tong + gia_tri

print("-------------------")
print("Số lượng giá trị hợp lệ:", dem_hop_le)
print("Số lượng giá trị không hợp lệ:", dem_khong_hop_le)
print("Tổng các giá trị hợp lệ:", tong)

if dem_hop_le > 0:
    trung_binh = tong / dem_hop_le
    print("Trung bình cộng:", trung_binh)
else:
    print("Không thể tính trung bình!")
