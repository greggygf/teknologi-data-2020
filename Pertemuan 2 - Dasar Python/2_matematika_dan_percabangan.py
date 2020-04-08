# Operasi matematika dasar pada Python
x = 5
y = 3
print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(x % y)    # Modulus, sisa hasil bagi
print(x ** y)   # Exponentiate, alias pangkat

# # Konversi ke tipe data angka
# str_a = "5"
# # Bisa menggunakan fungsi int() atau float()
# a = int(str_a)
# b = float(str_a)
#
# print('Hasil fungsi int() : {}'.format(a))
# print('Hasil fungsi float() : {}'.format(b))
#
# # Boolean - case sensitive
# benar = True
# salah = False
#
# # Operator boolean
# print(benar and salah)      # False
# print(benar or salah)       # True
# print(benar and not salah)  # True
#
# # Percabangan alias IF
#
# str_a = input('Masukkan bilangan A: ')
# str_b = input('Masukkan bilangan B: ')
# a = int(str_a)
# b = int(str_b)
#
# # If di python tidak pakai kurung ( tabnya bukan 1 tab namun 4 spasi dalam python )
# # Ingat: indentasi harus sesuai. Standardnya adalah 4 spasi bukan 1 tab.
# if a < b:
#     print('Bilangan {} lebih kecil dari bilangan {}'.format(a,b))
# elif b < a: # singkatan dari else if
#     print('Bilangan {} lebih kecil dari bilangan {}'.format(b,a))
# else:
#     print('Bilangan {} sama dengan bilangan {}'.format(a,b))