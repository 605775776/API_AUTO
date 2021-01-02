import random


def generate_mobile():
    "随机生成手机号码  1[3,5,8,9]+ 9"

    phone = '1' + random.choice(['3', '5', '8', '9'])
    for i in range(9):
        num = random.randint(0, 9)
        phone += str(num)
    return phone

# if __name__ == '__main__':
#     print(generate_mobile())