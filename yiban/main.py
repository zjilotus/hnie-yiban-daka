import time

from yiban import yiban
from names import names


def do(name):
    yb = yiban(username=name['userid'],
               password=name['pwd'], )

    print("现在打卡的是：" + name['userid'] + "  " + name['pwd'])

    yb.sign_up()  # 登录
    if not yb.cookies or not yb.num:
        print("")
        time.sleep(2)
        return

    last_json = yb.get_last()
    if not last_json:
        print("")
        return

    res = yb.daka(last_json)
    if not res:
        print("")
        return
    elif res['result']:
        print("打卡结果：打卡成功")
    else:
        print("打卡结果: " + str(res['errorInfoList']))

    print(last_json['dkd'])
    print("")


if __name__ == '__main__':
    for name in names:
        if name['userid'] == "" or name['pwd'] == "":
            break
        do(name)

        time.sleep(1)

