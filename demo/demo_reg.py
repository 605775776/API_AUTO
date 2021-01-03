import re

mystr = '{"member_id": "#member_id#", "loan_id": "#loan_id#", "token": "#token#", "username": "#username#"}'

# re_pattern = r'#(.*?)#'
# res = re.findall(re_pattern, mystr)
# res_1 = re.search(re_pattern, mystr)
# print(res)
# print(res_1)
# 组
# 替换 re.sub
# new_str = re.sub(re_pattern,'123', mystr, 1)
# print(new_str)

class Context:
    member_id = 888
    loan_id = 777
    token = "111"
    username = 'dsw'

def replace_label(target):


    re_pattern = r"#(.*?)#"
    while re.findall(re_pattern, target):
        key = re.search(re_pattern, target).group(1)
        # value = getattr(CaseKeys, key, '')
        target = re.sub(re_pattern, str(getattr(Context, key)), target, 1)
    return target

if __name__ == '__main__':
    mystr = '{"member_id": "#member_id#", "loan_id": "#loan_id#", "token": "#token#", "username": "#username#"}'
    # re_pattern = r'#(.*?)#'
    a = replace_label(mystr)
    print(a)

