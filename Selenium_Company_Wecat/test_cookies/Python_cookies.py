"""
使用cookies

driver.get(url)
driver.delete all cookies()
for cookie in cookies:
driver.add cookie(cookie)
driver-refresh()
"""
import shelve

from selenium import webdriver


class TestCookies:

    def setup(self):
        self.driver = webdriver.Chrome()

    def teardown(self):
        # self.driver.quit()
        pass

    def test_wework(self):
        self.driver.get('https://work.weixin.qq.com/')
        # print(self.driver.get_cookies())
        cookies = [{'domain': '.qq.com', 'expiry': 1596442011, 'httpOnly': False, 'name': '_gat', 'path': '/', 'secure': False, 'value': '1'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.d2st', 'path': '/', 'secure': False, 'value': 'a307764'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ref', 'path': '/', 'secure': False, 'value': 'direct'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'Hm_lpvt_9364e629af24cb52acc78b43e8c9f77d', 'path': '/', 'secure': False, 'value': '1596441356'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.vid', 'path': '/', 'secure': False, 'value': '1688850318574042'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.corpid', 'path': '/', 'secure': False, 'value': '1970325002152709'}, {'domain': '.work.weixin.qq.com', 'expiry': 1627977356, 'httpOnly': False, 'name': 'Hm_lvt_9364e629af24cb52acc78b43e8c9f77d', 'path': '/', 'secure': False, 'value': '1596205265,1596437983'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.refid', 'path': '/', 'secure': False, 'value': '20749635693579936'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.vst', 'path': '/', 'secure': False, 'value': 'uWfHSmWIRklKQLQE-3CONp-74mrfI834vaTbZHYisU-CEx53usqXLRu9TN3BxqDjNSWMb_wmDw7R99XAd1sM65MhY21qn1_klHfZFdqXnobsSMHH5AQMpp_MpBUDLUBaK-A1hkCxNaz2VgivJy57pJmGWbe5bkA4Iz5OvXRko6wFxBUc5i9ifZU0AK93u0r26sKyudKLO-5LaamSFcfzgz_cUjEHdh4r2Gib2fTr-qfV64BQen7oyC8ZjjQh1gKDgJBWNEakCXrZrgOc6r0Y6A'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ltype', 'path': '/', 'secure': False, 'value': '1'}, {'domain': '.qq.com', 'httpOnly': False, 'name': 'pgv_info', 'path': '/', 'secure': False, 'value': 'ssid=s9504609136'}, {'domain': '.qq.com', 'expiry': 1596528105, 'httpOnly': False, 'name': '_gid', 'path': '/', 'secure': False, 'value': 'GA1.2.292688081.1596375804'}, {'domain': '.qq.com', 'expiry': 1659513705, 'httpOnly': False, 'name': '_ga', 'path': '/', 'secure': False, 'value': 'GA1.2.1679177664.1596205265'}, {'domain': '.work.weixin.qq.com', 'expiry': 1599033708.198227, 'httpOnly': False, 'name': 'wwrtx.i18n_lan', 'path': '/', 'secure': False, 'value': 'zh-cn'}, {'domain': 'work.weixin.qq.com', 'expiry': 1596469514.808794, 'httpOnly': True, 'name': 'ww_rtkey', 'path': '/', 'secure': False, 'value': 'dablgt'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.vid', 'path': '/', 'secure': False, 'value': '1688850318574042'}, {'domain': '.qq.com', 'expiry': 2147483647.240243, 'httpOnly': False, 'name': 'ptcz', 'path': '/', 'secure': False, 'value': '01c78882260f8862afdd30f3221cafc92a458567c41ff44467b2722db17e07bb'}, {'domain': '.qq.com', 'expiry': 1907232460, 'httpOnly': False, 'name': 'tvfe_boss_uuid', 'path': '/', 'secure': False, 'value': '87e3b58848432c29'}, {'domain': '.work.weixin.qq.com', 'expiry': 1627741042.96689, 'httpOnly': False, 'name': 'wwrtx.c_gdpr', 'path': '/', 'secure': False, 'value': '0'}, {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'pgv_pvid', 'path': '/', 'secure': False, 'value': '8995173307'}, {'domain': '.qq.com', 'expiry': 1620566415, 'httpOnly': False, 'name': 'LW_uid', 'path': '/', 'secure': False, 'value': 'd195L8c9i0Q3e0g4v1S5x4L4F4'}, {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'o_cookie', 'path': '/', 'secure': False, 'value': '1032321374'}, {'domain': '.qq.com', 'expiry': 2147483643.858821, 'httpOnly': False, 'name': 'RK', 'path': '/', 'secure': False, 'value': 'aPLpZvlTXK'}, {'domain': '.qq.com', 'expiry': 1620566751, 'httpOnly': False, 'name': 'LW_sid', 'path': '/', 'secure': False, 'value': 'B1n578Q9n0j3x0j7L511Q3j3Y3'}, {'domain': '.qq.com', 'expiry': 1604227170, 'httpOnly': False, 'name': 'eas_sid', 'path': '/', 'secure': False, 'value': 'b1t547P2x6c9m131m7Z019N1S5'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.sid', 'path': '/', 'secure': False, 'value': 'jGzGpzPYhxIS8qXeCPvjq-Geju4smbu2_VwDnvlP8bZ7eXMrXxIaR2ZwD6PWmBmZ'}, {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'pgv_pvi', 'path': '/', 'secure': False, 'value': '9532613632'}]
    # 获取cookies
        for cookie in cookies:
            #删除失效说明字段
            if 'expiry' in cookie.keys():
                cookie.pop('expiry')
            # 把字典加入到 driver 的 cookie中
            self.driver.add_cookie(cookie)
        self.driver.get('https://work.weixin.qq.com/wework_admin/frame')
        self.driver.find_element_by_id('menu_contacts').click()


    def test_savecookies(self):
        self.driver.get('https://work.weixin.qq.com/')
        #创建或者打开一个本地数据库
        db = shelve.open("cookies")
        # cookies = [
        #     {'domain': '.qq.com', 'expiry': 1596442011, 'httpOnly': False, 'name': '_gat', 'path': '/', 'secure': False,
        #      'value': '1'},
        #     {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.d2st', 'path': '/', 'secure': False,
        #      'value': 'a307764'},
        #     {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ref', 'path': '/', 'secure': False,
        #      'value': 'direct'},
        #     {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'Hm_lpvt_9364e629af24cb52acc78b43e8c9f77d',
        #      'path': '/', 'secure': False, 'value': '1596441356'},
        #     {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.vid', 'path': '/', 'secure': False,
        #      'value': '1688850318574042'},
        #     {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.corpid', 'path': '/', 'secure': False,
        #      'value': '1970325002152709'}, {'domain': '.work.weixin.qq.com', 'expiry': 1627977356, 'httpOnly': False,
        #                                     'name': 'Hm_lvt_9364e629af24cb52acc78b43e8c9f77d', 'path': '/',
        #                                     'secure': False, 'value': '1596205265,1596437983'},
        #     {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.refid', 'path': '/', 'secure': False,
        #      'value': '20749635693579936'},
        #     {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.vst', 'path': '/', 'secure': False,
        #      'value': 'uWfHSmWIRklKQLQE-3CONp-74mrfI834vaTbZHYisU'
        #               '-CEx53usqXLRu9TN3BxqDjNSWMb_wmDw7R99XAd1sM65MhY21qn1_klHfZFdqXnobsSMHH5AQMpp_MpBUDLUBaK'
        #               '-A1hkCxNaz2VgivJy57pJmGWbe5bkA4Iz5OvXRko6wFxBUc5i9ifZU0AK93u0r26sKyudKLO'
        #               '-5LaamSFcfzgz_cUjEHdh4r2Gib2fTr-qfV64BQen7oyC8ZjjQh1gKDgJBWNEakCXrZrgOc6r0Y6A'},
        #     {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ltype', 'path': '/', 'secure': False,
        #      'value': '1'}, {'domain': '.qq.com', 'httpOnly': False, 'name': 'pgv_info', 'path': '/', 'secure': False,
        #                      'value': 'ssid=s9504609136'},
        #     {'domain': '.qq.com', 'expiry': 1596528105, 'httpOnly': False, 'name': '_gid', 'path': '/', 'secure': False,
        #      'value': 'GA1.2.292688081.1596375804'},
        #     {'domain': '.qq.com', 'expiry': 1659513705, 'httpOnly': False, 'name': '_ga', 'path': '/', 'secure': False,
        #      'value': 'GA1.2.1679177664.1596205265'},
        #     {'domain': '.work.weixin.qq.com', 'expiry': 1599033708.198227, 'httpOnly': False, 'name': 'wwrtx.i18n_lan',
        #      'path': '/', 'secure': False, 'value': 'zh-cn'},
        #     {'domain': 'work.weixin.qq.com', 'expiry': 1596469514.808794, 'httpOnly': True, 'name': 'ww_rtkey',
        #      'path': '/', 'secure': False, 'value': 'dablgt'},
        #     {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.vid', 'path': '/', 'secure': False,
        #      'value': '1688850318574042'},
        #     {'domain': '.qq.com', 'expiry': 2147483647.240243, 'httpOnly': False, 'name': 'ptcz', 'path': '/',
        #      'secure': False, 'value': '01c78882260f8862afdd30f3221cafc92a458567c41ff44467b2722db17e07bb'},
        #     {'domain': '.qq.com', 'expiry': 1907232460, 'httpOnly': False, 'name': 'tvfe_boss_uuid', 'path': '/',
        #      'secure': False, 'value': '87e3b58848432c29'},
        #     {'domain': '.work.weixin.qq.com', 'expiry': 1627741042.96689, 'httpOnly': False, 'name': 'wwrtx.c_gdpr',
        #      'path': '/', 'secure': False, 'value': '0'},
        #     {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'pgv_pvid', 'path': '/',
        #      'secure': False, 'value': '8995173307'},
        #     {'domain': '.qq.com', 'expiry': 1620566415, 'httpOnly': False, 'name': 'LW_uid', 'path': '/',
        #      'secure': False, 'value': 'd195L8c9i0Q3e0g4v1S5x4L4F4'},
        #     {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'o_cookie', 'path': '/',
        #      'secure': False, 'value': '1032321374'},
        #     {'domain': '.qq.com', 'expiry': 2147483643.858821, 'httpOnly': False, 'name': 'RK', 'path': '/',
        #      'secure': False, 'value': 'aPLpZvlTXK'},
        #     {'domain': '.qq.com', 'expiry': 1620566751, 'httpOnly': False, 'name': 'LW_sid', 'path': '/',
        #      'secure': False, 'value': 'B1n578Q9n0j3x0j7L511Q3j3Y3'},
        #     {'domain': '.qq.com', 'expiry': 1604227170, 'httpOnly': False, 'name': 'eas_sid', 'path': '/',
        #      'secure': False, 'value': 'b1t547P2x6c9m131m7Z019N1S5'},
        #     {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.sid', 'path': '/', 'secure': False,
        #      'value': 'jGzGpzPYhxIS8qXeCPvjq-Geju4smbu2_VwDnvlP8bZ7eXMrXxIaR2ZwD6PWmBmZ'},
        #     {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'pgv_pvi', 'path': '/',
        #      'secure': False, 'value': '9532613632'}]
        # #将数据存储到shelve中
        # db["cookies"] = cookies
        # db.close()
        cookies = db["cookies"]
        for cookie in cookies:
            # 删除失效说明字段
            if 'expiry' in cookie.keys():
                cookie.pop('expiry')
            # 把字典加入到 driver 的 cookie中
            self.driver.add_cookie(cookie)
        self.driver.get('https://work.weixin.qq.com/wework_admin/frame')
        self.driver.find_element_by_id('menu_contacts').click()