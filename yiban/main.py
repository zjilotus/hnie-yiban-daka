import time

from yiban import yiban_daka
from names import names


if __name__ == '__main__':
    for name in names:
        yiban_daka(username=name['userid'],
                   password=name['pwd'],)
        time.sleep(1)

