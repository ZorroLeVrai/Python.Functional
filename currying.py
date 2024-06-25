from functools import partial
from toolz import compose, curry
from operator import add

def manually_curried_add(a):
    def add_b(b):
        def add_c(c):
            return a + b + c
        return add_c
    return add_b

def not_curried_add(a, b, c):
    return a + b + c

@curry
def curried_add(a, b, c):
    return a + b + c


if __name__ == "__main__":
    #using manual currying
    print(manually_curried_add(2)(3)(4))

    #currying by using partial and composition
    print(compose(partial(add,2), partial(add,3), partial(add,4))(0))
    print(partial(partial(not_curried_add,2),3)(4))

    #using curried version
    print(curried_add(2)(3)(4))
    print(curried_add(2,3,4))
