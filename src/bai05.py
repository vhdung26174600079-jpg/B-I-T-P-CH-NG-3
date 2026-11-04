
a = float(input("Nhập a (khác 0): "))

while a == 0:
    print("a phải khác 0!")
    a = float(input("Nhập lại a: "))

n = int(input("Nhập n (0-20): "))

while n < 0 or n > 20:
    print("n không hợp lệ!")
    n = int(input("Nhập lại n: "))

ket_qua = 1

for i in range(n):
    ket_qua = ket_qua * a

print("Kết quả:", ket_qua)

