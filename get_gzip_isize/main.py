import os

with open('../test_data/test.csv.gz', 'rb') as f:
    f.seek(-4, 2)
    size = int.from_bytes(f.read(), 'little')

actual_csv_size = os.path.getsize('../test_data/test.csv')

print(size)

actual_csv_size == size
