data = ["3 minggu 3 hari 7 jam 21 menit",
        "5 minggu 5 hari 8 jam 11 menit",
        "7 minggu 1 hari 5 jam 33 menit"]

# Fungsi untuk memeriksa apakah karakter adalah angka
def is_digit(char):
    return char.isdigit()

# Menggunakan fungsi filter untuk mengambil hanya nilai integer
filtered_data = [list(filter(is_digit, item.split())) for item in data]

# Menggabungkan hasilnya kembali menjadi string
result = [' '.join(filtered_item) for filtered_item in filtered_data]

# Mencetak hasil
for item in result:
    print(item)