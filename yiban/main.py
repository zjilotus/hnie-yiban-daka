import time

from yiban import yiban_daka


if __name__ == '__main__':
    for name in names:
        yiban_daka(username=name['userid'],
                   password=name['pwd'],
                   name=name['name'])
        time.sleep(1)

