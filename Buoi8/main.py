# Hàm không có tham số và không trả về giá trị

name = "thắng"


def hello():
    print("hello function")


# Hàm có tham số và không trả về giá trị
def hello(name):
    print(f"Hello {name}")


def find_max(arr):
    max_pos = 0
    for i in range(len(arr)):
        if arr[i] > arr[max_pos]:
            max_pos = i
    return arr[max_pos]


def test():
    name = "thắng 2"
    print(name)


# def tong(a, b):
#     print(name)
#     return a + b
def add_one(num):
    num += 1
    print(f"Num trong hàm add_one = {num}")


num = 10
add_one(num)
print(num)
