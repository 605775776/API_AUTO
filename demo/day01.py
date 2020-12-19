import requests
# requests.DEFAULT_RETRIES = 5
# s = requests.session()
# s.keep_alive = False
# register_url = "http://120.78.128.25:8766/futureloan/member/register"
# data = {"mobile_phone": "15745612312", "pwd": "12345612"}
# header = {"X-Lemonban-Media-Type": "lemonban.v1", 'Connection': 'close'}
#
# res = requests.post(register_url, json=data, headers=header)
# print(res.json())
#
login_url = "http://120.78.128.25:8766/futureloan/member/login"
data = {"mobile_phone": "15745612312", "pwd": "12345612"}
header = {"X-Lemonban-Media-Type": "lemonban.v2"}
res_login = requests.post(login_url, json=data, headers=header)
print(res_login.json())
# token = res_login.json()['data']['token_info']['token']
#
#
# header = {"X-Lemonban-Media-Type": "lemonban.v2", "Authorization": "Bearer {}".format(token)}
# id = res_login.json()['data']['id']
# recharge_url = 'http://120.78.128.25:8766/futureloan/member/recharge'
# data = {"member_id": id, "amount": 100}
# res_recharge = requests.post(recharge_url, json=data, headers=header)
# print(res_login.json())
# 15745612312 12345612







# data = {"member_id": "111", "amount": 1000}
# recharge = requests.post(recharge_url, json=data, headers=header)
# print(recharge.json())

#
# url = "http://test.lemonban.com/futureloan/mvc/api/member/login"