import functools as ft
from toolz import compose

lst = [2, 3, 5, 7, 11, 13, 17, 19]

def process_list(data_list: list[int]):
    """
    filtrer les valeurs supérieures à 10
    doubler ces données
    retourner la somme
    """
    return sum(map(lambda x: 2*x, filter(lambda x: x>10, data_list)))

def process_list_composition(data_list: list[int]):
    partial_filter = lambda lst: filter(lambda x: x>10, lst)
    partial_map = lambda lst: map(lambda x: 2*x, lst)
    return sum(partial_map(partial_filter(data_list)))

def process_list_composition2(data_list: list[int]):
    partial_filter = ft.partial(filter, lambda x: x>10)
    partial_map = ft.partial(map, lambda x: 2*x)
    return compose(sum, partial_map, partial_filter)(data_list)


if __name__ == "__main__":
    print(process_list(lst))
    print(process_list_composition(lst))
    print(process_list_composition2(lst))
