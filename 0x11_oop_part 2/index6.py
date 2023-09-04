# Method Resolution Order(MRO)
class A:
    def do_something(self):
        print("Method Defination In : A")


class B(A):
    def do_something(self):
        print("Method Defination In : B")


class C(A):
    def do_something(self):
        print("Method Defination In : C")


class D(B, C):
    pass

    def do_something(self):
        print("Method Defination In : D")
        # super().do_something()  ## this would just class the next class

# print(D.__mro__)
# print(D.mro())
# help(D)


thing = D()
thing.do_something()


#           A
#         /   \
#         B    C
#         \    /
#           D

# D, B,C, A, object
