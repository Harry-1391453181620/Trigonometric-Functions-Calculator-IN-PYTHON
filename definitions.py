import math
def sin_func(value):
    radian = math.radians(value)
    return math.sin(radian)
def cos_func(value):
    radian = math.radians(value)
    return math.cos(radian)
def tan_func(value):
    radian = math.radians(value)
    return math.tan(radian)
def cot_func(value):
    radian = math.radians(value)
    if math.sin(radian) == 0:
        return float('inf') if math.cos(radian) > 0 else float('-inf')
    return math.cos(radian) / math.sin(radian)
def sec_func(value):
    radian = math.radians(value)
    if math.cos(radian) == 0:
        return float('inf') if math.cos(radian) > 0 else float('-inf')
    return 1 / math.cos(radian)
def csc_func(value):
    radian = math.radians(value)
    if math.sin(radian) == 0:
        return float('inf') if math.sin(radian) > 0 else float('-inf')
    return 1 / math.sin(radian)
def arcsin_func(value):
    if not -1 <= value <= 1:
        raise ValueError("Input number must be in range [-1,1]")
    return math.degrees(math.asin(value))
def arccos_func(value):
    if not -1 <= value <= 1:
        raise ValueError("Input number must be in range [-1,1]")
    return math.degrees(math.acos(value))
def arctan_func(value):
    return math.degrees(math.atan(value))
def arccot_func(value):
    return math.degrees(math.atan(1 / value)) if value != 0 else 90
def arcsec_func(value):
    if abs(value) < 1:
        raise ValueError("The absolute value of the input number must be in range [1,infinite)")
    return math.degrees(math.acos(1 / value))
def arccsc_func(value):
    if abs(value) < 1:
        raise ValueError("The absolute value of the input number must be in range [1,infinite)")
    return math.degrees(math.asin(1 / value))
def versin_func(value):
    radian = math.radians(value)
    return 1 - math.cos(radian)
def coversin_func(value):
    radian = math.radians(value)
    return 1 - math.sin(radian)
def haversin_func(value):
    radian = math.radians(value)
    return (1 - math.cos(radian)) / 2
def hacoversin_func(value):
    radian = math.radians(value)
    return (1 - math.sin(radian)) / 2
def exsec_func(value):
    radian = math.radians(value)
    if math.cos(radian) == 0:
        return float('inf') if math.cos(radian) > 0 else float('-inf')
    return 1 / math.cos(radian) - 1
def excsc_func(value):
    radian = math.radians(value)
    if math.sin(radian) == 0:
        return float('inf') if math.cos(radian) > 0 else float('-inf')
    return 1 / math.sin(radian) - 1
