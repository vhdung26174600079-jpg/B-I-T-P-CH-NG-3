
initial_money = float(input("Nhập số tiền ban đầu: "))

while initial_money <= 0:
    print("Số tiền phải lớn hơn 0!")
    initial_money = float(input("Nhập lại số tiền: "))

n = int(input("Nhập số tháng (1-24): "))

while n < 1 or n > 24:
    print("Số tháng không hợp lệ!")
    n = int(input("Nhập lại số tháng: "))

so_du = initial_money
tong_tien_gui_them = 0
tong_tien_lai = 0

for i in range(1, n + 1):
    print("Tháng", i)

    tien_lai = so_du * 0.005

    tien_gui_them = float(input("Nhập tiền gửi thêm: "))

    while tien_gui_them <= 0:
        print("Tiền gửi thêm phải lớn hơn 0!")
        tien_gui_them = float(input("Nhập lại tiền gửi thêm: "))

    so_du = so_du + tien_lai + tien_gui_them

    tong_tien_gui_them = tong_tien_gui_them + tien_gui_them
    tong_tien_lai = tong_tien_lai + tien_lai

    print("Số dư cuối tháng:", so_du)

print("-------------------")
print("Số dư cuối cùng:", so_du)
print("Tổng tiền gửi thêm:", tong_tien_gui_them)
print("Tổng tiền lãi:", tong_tien_lai)
