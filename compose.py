import functools as ft
from toolz import compose

def manual_compose(*functions):
    return ft.reduce(lambda f, g: lambda x: f(g(x)), functions)

if __name__ == "__main__":
    ma_fonction = manual_compose(lambda s: print(f"Resultat: {s}"), lambda x: x+1)
    ma_fonction2 = compose(lambda s: print(f"Result: {s}"), lambda x: x+1)
    ma_fonction(7)
    ma_fonction2(7)