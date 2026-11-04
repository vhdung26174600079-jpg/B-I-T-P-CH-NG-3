
n = int(input("Nhập số sinh viên (1-60): "))

while n < 1 or n > 60:
    print("Số sinh viên không hợp lệ!")
    n = int(input("Nhập lại n: "))

co_mat = 0
vang_mat = 0
co_phep = 0

for i in range(1, n + 1):
    print("Sinh viên thứ", i)

    trang_thai = int(input("Nhập trạng thái (1: Có mặt, 0: Vắng, 2: Có phép): "))

    while trang_thai != 0 and trang_thai != 1 and trang_thai != 2:
        print("Trạng thái không hợp lệ!")
        trang_thai = int(input("Nhập lại trạng thái: "))

    if trang_thai == 1:
        co_mat = co_mat + 1
    elif trang_thai == 0:
        vang_mat = vang_mat + 1
    else:
        co_phep = co_phep + 1

tong = co_mat + vang_mat + co_phep

ty_le_co_mat = co_mat / n * 100
ty_le_khong_co_mat = (vang_mat + co_phep) / n * 100

print("-------------------")
print("Số sinh viên có mặt:", co_mat)
print("Số sinh viên vắng mặt:", vang_mat)
print("Số sinh viên có phép:", co_phep)

print("Tỷ lệ có mặt:", ty_le_co_mat, "%")
print("Tỷ lệ không có mặt:", ty_le_khong_co_mat, "%")

print("Tổng số sinh viên:", tong)

if tong == n:
    print("Dữ liệu điểm danh hợp lệ!")
else:
    print("Dữ liệu điểm danh không hợp lệ!")
