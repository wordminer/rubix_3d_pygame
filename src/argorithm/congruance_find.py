def congruance_of_p(module_p : int, number : int):
    rememder = number % module_p
    if rememder > module_p/2:
        rememder = rememder - module_p
    return rememder

