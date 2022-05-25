import requests
import hashlib


class yiban:
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
        login_url = "http://59.71.0.224/website/login"
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

    def get_last(self):  # 获得上一次打卡信息
        try:
            last_url = "http://59.71.0.224/content/student/temp/zzdk/lastone"
            params = {
                '_t_s_': self.num,
            }
            res = requests.get(last_url, params=params, cookies=self.cookies).json()
        except Exception as e:
            print(e)
            return None
        return res

    def daka(self, last_json):  # 打卡
        daka_url = "http://59.71.0.224/content/student/temp/zzdk?_t_s_=" + self.num

        try:
            if last_json['sfzx'] == 1:  # 是否在学校
                str_sfzx = "在校"
            else:
                str_sfzx = "不在校"

            if not last_json['jzdXian']:  # 有人没有县
                jzdXian = None
            else:
                jzdXian = last_json['jzdXian']['dm']

            params = {
                'zdjg': "",
                'yczk1': last_json['yczk']['mc'],  # 无症状
                'yczk.dm': last_json['yczk']['dm'],  # 01
                'xgym1': '已接种已完成',
                'xgym': 2,
                'xcm1': '绿色',
                'xcm': 1,
                'twM.dm': last_json['twM']['dm'],  # 01
                'tw1': last_json['twM']['mc'],  # 体温 '[35.0~37.2]正常'
                'tw1M.dm': last_json['tw1M']['dm'],
                'tw11': last_json['tw1M']['mc'],
                'tw2M.dm': last_json['tw2M']['dm'],
                'tw12': last_json['tw2M']['mc'],
                'tw3M.dm': last_json['tw3M']['dm'],
                'tw13': last_json['tw3M']['mc'],
                'sfzx1': str_sfzx,  # 是否在校
                'sfzx': last_json['sfzx'],
                'operationType': 'Create',  # Create第一次打今天的卡 update更新打卡
                'lxdh': last_json['lxdh'],  # 联系电话
                'jzYy': "",
                'jzInd': last_json['jzInd'],  # 0
                'jzdXian.dm': jzdXian,  # 居住地县
                'jzdShi.dm': last_json['jzdShi']['dm'],  # 居住地市
                'jzdSheng.dm': last_json['jzdSheng']['dm'],  # 居住地省
                'jzdValue': {last_json['jzdSheng']['dm'], last_json['jzdShi']['dm'], jzdXian},
                'jzdDz2': last_json['jzdDz2'],  # 居住地 常驻地址
                'jzdDz': last_json['jzdDz'],  # 居住地 详细地址
                'jrStzk1': last_json['jrStzk']['mc'],  # 身体健康、无异常
                'jrStzk.dm': last_json['jrStzk']['dm'],  # 01
                'jrJccry1': last_json['jrJccry']['mc'],  # 未接触传染源
                'jrJccry.dm': last_json['jrJccry']['dm'],  # 01
                'jkm1': '绿色',  # 健康码
                'jkm': last_json['jkm'],  # 1
                'hsjc1': '是',  # 核酸检测
                'hsjc': 1,
                'fxrq': "",
                'fbrq': "",
                'dm': "",
                'dkly': last_json['dkly'],  # baidu or yiban
                'dkdz': last_json['dkdz'],  # 打卡地址 "湖南省岳阳市岳阳楼区金鹗中路135号"
                'dkdzZb': "112.944,27.8296",
                'dkd': last_json['dkd'],  # 打卡地 "湖南省岳阳市"
                'bz': last_json['bz'],  # 备注
                'brStzk1': last_json['brStzk']['mc'],  # 身体健康、无异常
                'brStzk.dm': last_json['brStzk']['dm'],  # 01
                'brJccry1': last_json['brJccry']['mc'],  # 未接触传染源
                'brJccry.dm': last_json['brJccry']['dm'],  # 01
            }
            res = requests.post(daka_url, cookies=self.cookies, data=params).json()
        except Exception as e:
            print(e)
            return None
        return res
