import os
import random
import time

from yiban.wanGui import wanGui
from names import names


def writeFile(ip):
    file1 = open(r'modifyIp.bat', 'w', encoding='ansi')
    # 打开文件，w表示清空后写入，a表示append，追加的意思
    str = 'netsh interface ip set address name="以太网" source=static addr=' + ip + ' mask=255.255.255.0 gateway=10.0.38.1'
    file1.write(str)
    # 写入内容
    file1.close()
    # 关闭文件


if __name__ == '__main__':
    ip = "10.0.38." + str(random.randint(40, 90))
    writeFile(ip)
    os.system("E:\\Desktop\\11.bat")
    time.sleep(4)

    wg = wanGui("202003020240", "124455")

    wg.sign_up()
    res = wg.getDM()
    for re in res['aaData']:
        data = {
            "dm": re['DM'],
            "sjdm": re['SJDM'],
        }
        ans = wg.daka(data)
        print(ans)

    # i = 0
    # for name in names:
    #     i += 1
    #     if i % 5 == 0:
    #         ip = "10.0.38." + str(random.randint(40, 90))
    #         writeFile(ip)
    #         os.system("E:\\Desktop\\11.bat")
    #         time.sleep(4)
    #     print(name)
    #     wg = wanGui(name['username'], name['password'])
    #     wg.sign_up()
    #     res = wg.getDM()
    #     for re in res['aaData']:
    #         data = {
    #             "dm": re['DM'],
    #             "sjdm": re['SJDM'],
    #         }
    #         ans = wg.daka(data)
    #         print(ans)