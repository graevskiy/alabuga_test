import functools

MONTH_DAYS = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)


def day_number(month: int, day: int) -> int:
    return functools.reduce(
        lambda x, y: x + y, MONTH_DAYS[:month-1], 0
    ) + day

def main():
    l1 = list(map(int, input().split()))
    l2 = list(map(int, input().split()))

    s_d = day_number(l1[1], l1[2])
    f_d = day_number(l2[1], l2[2])

    years = l2[0] - l1[0]
    if f_d >= s_d:
        days = f_d - s_d
    else:
        days = 365 - s_d + f_d
        years -= 1
    days += years * 365

    to_seconds = [60 * 60, 60, 1]
    s_s, f_s = 0, 0
    for i in range(3):
        s_s += l1[3 + i] * to_seconds[i]
        f_s += l2[3 + i] * to_seconds[i]

    if f_s >= s_s:
        seconds = f_s - s_s
    else:
        seconds = 24 * 60 * 60 - s_s + f_s
        days -= 1

    return days, seconds


if __name__ == "__main__":
    print(*main())
