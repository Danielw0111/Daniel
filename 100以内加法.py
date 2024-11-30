import random

i = 0
while i < 100:
    i = i + 1
    a = random.randint(0, 100)
    b = random.randint(0, 100)
    print('第', i, '题')
    print(a, '+', b, '=')
    answer = input()

    j = 1
    if (a+b) == int(answer):
        print('你是个大聪明')
        print('下一题')
    else:
        while j < 3:
            j = j + 1
            answer = input('再给一次机会')
            if (a+b) == int(answer):
                print('总算做对了，你还是个大聪明')
                break
        else:
            print('大笨蛋，三次全做错了，继续努力吧！')
            print('告诉你正确答案：', a, '+', b, '=', a+b)
            print('下一题')


