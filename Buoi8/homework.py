import math
from datetime import datetime


def is_int(num):  # Bài 1
    phan_nguyen = math.floor(num)
    phan_thap_phan = num - phan_nguyen
    if phan_thap_phan == 0:
        return True
    else:
        return False


def is_prime(num):  # Bài 2
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                return False
        return True
    else:
        return False


def enum_prime(n):  # Bài 3
    count = 0
    i = 2
    while count < n:
        if is_prime(i):
            print(i)
            count += 1
        i += 1


def giai_thua(num):
    tich = 1
    for i in range(1, num + 1):
        tich *= i
    return tich


def bai_4(n):
    result = 0
    for i in range(1, n + 1):
        result += giai_thua(i) / i
    print(f"Result: {result}")


def bai_5():
    now = datetime.now()
    print(f"Today is {now.strftime('%d/%m/%Y')}")
    print(f"Time right now: {now.strftime('%H:%M:%S')}")


def main():
    bai_5()


main()
