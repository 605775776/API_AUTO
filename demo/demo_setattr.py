class Demo:

    member_id = 2
    token = 'abc'

if __name__ == '__main__':
    a = getattr(Demo, 'memer_id', '闲人')
    print(a)

