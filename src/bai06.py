
n = int(input("Nhập số mặt hàng (1-20): "))

while n < 1 or n > 20:
    print("Số mặt hàng không hợp lệ!")
    n = int(input("Nhập lại n: "))

tong_so_luong = 0
tong_tien = 0

for i in range(1, n + 1):
    print("Mặt hàng thứ", i)

    don_gia = float(input("Nhập đơn giá: "))

    while don_gia <= 0:
        print("Đơn giá phải lớn hơn 0!")
        don_gia = float(input("Nhập lại đơn giá: "))

    so_luong = int(input("Nhập số lượng: "))

    while so_luong <= 0:
        print("Số lượng phải lớn hơn 0!")
        so_luong = int(input("Nhập lại số lượng: "))

    thanh_tien = don_gia * so_luong

    print("Thành tiền:", thanh_tien)

    tong_so_luong = tong_so_luong + so_luong
    tong_tien = tong_tien + thanh_tien

print("-------------------")
print("Tổng số lượng sản phẩm:", tong_so_luong)
print("Tổng tiền thanh toán:", tong_tien)
