import time
import os

x = -1
y = 10
a = input("문구를 입력하시오(최대 9자): ")

#b = 123456789
#a + {len(b)-len(a)}

if len(a) <= 9:
    a = f'{a:#^9}'
    while x < 10:

        x = x + 1
        y = y - 1

        if x == 0:
            print(a[x:])
            time.sleep(0.4)
            os.system('cls')

        else:
            print(a[-x:]+a[:y])
            time.sleep(0.4)
            os.system('cls')

            if x == 9: break

else:
    print("9자를 넘겼습니다.")    