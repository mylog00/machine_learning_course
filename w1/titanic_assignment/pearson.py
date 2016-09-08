import math


def pearson_coef(x_arg, y_arg):
    x_sum = sum(x_arg)
    y_sum = sum(y_arg)
    # average (x^)
    x_avg = x_sum / len(x_arg)
    y_avg = y_sum / len(y_arg)
    # difference (x^ - x)
    x_diff = diff(x_arg, x_avg)
    y_diff = diff(y_arg, y_avg)

    diff_sum = sum([x * y for x, y in zip(x_diff, y_diff)])
    print(diff_sum)
    x_sqrt_sum = math.sqrt(sum([x * x for x in x_diff]))
    y_sqrt_sum = math.sqrt(sum([y * y for y in y_diff]))
    print(x_sqrt_sum)
    print(y_sqrt_sum)

    result = diff_sum / (x_sqrt_sum * y_sqrt_sum)
    return result


def diff(arr, avg):
    result = []
    for i in arr:
        result.append(avg - i)
    return result

# test data
# x_agr = [24, 27, 26, 21, 20, 31, 26, 22, 20, 18, 30, 29, 24, 26]
# y_iq = [100, 115, 117, 119, 134, 94, 105, 103, 111, 124, 122, 109, 110, 86]
# -0.42109242545908376
# print(pearson_coef(x_agr, y_iq))
