import time

from yiban import yiban_daka
from names import names


if __name__ == '__main__':
    for name in names:
        if name['userid'] == "" or name['pwd'] == "":
            break
        yiban_daka(username=name['userid'],
                   password=name['pwd'],)
        time.sleep(1)

