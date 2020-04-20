# Membuat program menggunakan for-loop,list dan range

banyak = int(input("Berapa banyak data ?"))

name = []
umur = []

for i in range(0, banyak):
    print(f"Data ke {i}")
    input_name = input("Name : ")
    input_umur = int(input("Umur : "))

    name.append(input_name)
    umur.append(input_umur)

for bio in range(0, len(name)):
    data_name = name[bio]
    data_umur = umur[bio]
    print(f"{data_name} berumur {data_umur} tahun")