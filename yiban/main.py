import os
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


def writeFile(ip):
    file1 = open(r'E:\\Desktop\\11.bat', 'w', encoding='ansi')
    # 打开文件，w表示清空后写入，a表示append，追加的意思
    str = 'netsh interface ip set address name="以太网" source=static addr=' + ip + ' mask=255.255.255.0 gateway=10.0.38.1'
    file1.write(str)
    # 写入内容
    file1.close()
    # 关闭文件


if __name__ == '__main__':
    # for name in names:
    #     if name['userid'] == "" or name['pwd'] == "":
    #         break
    #     do(name)

        # time.sleep(1)

    # for i in range(40, 90):
    #     ip = "10.0.38." + str(i)
    #     writeFile(ip)
    #     os.system("E:\\Desktop\\11.bat")
    writeFile("10.0.38.9")
    os.system("E:\\Desktop\\11.bat")

