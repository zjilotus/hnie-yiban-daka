import random

import requests
import hashlib


class wanGui:
    def __init__(self, username, password):
        self.num = None  # 时间戳
        self.cookies = None  # cookie
        self.username = username
        self.password = password

    def getpw(self):  # 加密规则
        pwd = self.password.encode(encoding='utf-8')
        m = hashlib.md5()
        m.update(pwd)
        pwd = m.hexdigest()
        if len(pwd) > 5:
            pwd = pwd[0:5] + "a" + pwd[5:len(pwd)]

        if len(pwd) > 10:
            pwd = pwd[0:10] + "b" + pwd[10:len(pwd)]

        pwd = pwd[0:len(pwd) - 2]
        self.password = pwd

    def sign_up(self):  # 登录
        self.getpw()
        login_url = "http://172.31.0.187/website/login"
        params = {
            'uname': self.username,
            'pd_mm': self.password,
        }

        try:
            res = requests.post(login_url, params=params)
            cookies = requests.utils.dict_from_cookiejar(res.cookies)
            res = res.json()
            index_url = res['goto2']
            print("密码正确，成功登陆")
            num = index_url[-13:]  # 获得时间戳
        except Exception as e:
            if 'error' in res:
                print(res['msg'])
            return None

        self.cookies = cookies
        self.num = num

    def getDM(self):
        url = "http://172.31.0.187/content/tabledata/gygl/sign/stu/sign"
        params = {
            "bSortable_0": "false",
            "bSortable_1": "true",
            "iSortingCols": 1,
            "iDisplayStart": 0,
            "iDisplayLength": 12,
            "iSortCol_0": 3,
            "sSortDir_0": "desc",
            "_t_s_": self.num,
        }
        res = requests.get(url, cookies=self.cookies, params=params).json()
        return res

    def daka(self, data):  # 打卡
        daka_url = "http://172.31.0.187/content/gygl/sign/stu/sign?_t_s_=" + self.num

        zb_x = "112.94" + str(random.randint(0, 3))
        zb_y = "27.85" + str(random.randint(10, 90))

        try:
            params = {
                "pathFile": "",
                "dm": data['dm'],
                "sjdm": data['sjdm'],
                "zb": zb_x + "," + zb_y,
                "wz": "湖南省 湘潭市 岳塘区 至善路 156号 靠近湖南工程学院-明德公寓(10)",
                "ly": "baidu",
                "qdwzZt": "1",
                "qperationType": "update",
            }
            res = requests.post(daka_url, cookies=self.cookies, data=params).json()
        except Exception as e:
            print(e)
            return None
        return res


if __name__ == '__main__':
    wg = wanGui("", "")
    wg.sign_up()
    # print(wg.daka())
    res = wg.getDM()
    for re in res['aaData']:
        data = {
            "dm": re['DM'],
            "sjdm": re['SJDM'],
        }
        ans = wg.daka(data)
        print(ans)
