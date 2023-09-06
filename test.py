
class A:
    def __init__(self, num) -> None:
        self.num = num


def main():

    a = A(10)
    b = A(20)

    print(a.num)
    print(b.num)


main()

print("finish")
