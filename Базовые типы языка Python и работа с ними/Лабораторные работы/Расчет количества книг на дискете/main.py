disk_volume_mb = 1.44
pages_per_book = 100
lines_per_page = 50
chars_per_line = 25
bytes_per_char = 4

disk_volume_bytes = disk_volume_mb * 1024 * 1024
book_volume_bytes = pages_per_book * lines_per_page * chars_per_line * bytes_per_char

number_of_books = int(disk_volume_bytes // book_volume_bytes)

print(f"Количество книг, помещающихся на дискету: {number_of_books}")