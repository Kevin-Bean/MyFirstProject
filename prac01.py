import random

def red_packet(total, num):
    for i in range(num - 1):
        per = random.uniform(0.01, total / 2)
        # 返回a, b之间的随机浮点数，范围[a, b]或[a, b), 取决于四舍五入,a不一定要比b小
        total = total - per
        print('%.2f' % per)
        # print('{:.2f}'.format(per)) 保留 2 位小数
    else:
        print('%.2f' % total)

red_packet(100, 5)