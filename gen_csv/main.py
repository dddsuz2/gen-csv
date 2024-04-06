import csv
import os
import sys
import traceback
import gzip
import shutil

import numpy as np
from faker import Faker

from row import Rows

fake = Faker(locale="ja_JP")


def generate_csv(data_size: int) -> None:
    current_bytes = 0
    row = Rows()

    with open("test.csv", "w") as f:
        writer = csv.writer(f)
        writer.writerow(row.toHeader())

    try:
        while current_bytes < data_size:
            with open("../test_data/test.csv", "a") as f:
                writer = csv.writer(f)
                test_data = create_rows()
                writer.writerow(test_data.toList())
                f.close()

            current_bytes = os.path.getsize("../test_data/test.csv")

        with open('../test_data/test.csv', 'rb') as b_in:
            with gzip.open('../test_data/test.csv.gz', 'wb') as b_out:
                shutil.copyfileobj(b_in, b_out)

    except Exception as e:
        traceback.print_exc()
        os.remove("../test_data/test.csv")


def create_rows() -> Rows:
    row_instance = Rows()

    row_instance.name = fake.name()
    row_instance.age = np.random.randint(0, 100)
    row_instance.ip_addr = fake.ipv4()
    row_instance.address = fake.address()
    row_instance.phone_number = fake.phone_number()

    return row_instance


if __name__ == "__main__":
    data_size = sys.argv[1]
    generate_csv(int(data_size))
