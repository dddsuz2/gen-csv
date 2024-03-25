import csv
import os
import sys
import traceback

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
            with open("test.csv", "a") as f:
                writer = csv.writer(f)
                test_data = create_rows()
                print(test_data.toList())
                writer.writerow(test_data.toList())

            current_bytes = os.path.getsize("test.csv")

    except Exception as e:
        traceback.print_exc()
        os.remove("test.csv")


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
