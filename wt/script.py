from math import sqrt


def abs(xs, t):
    count = 0
    for x in xs:
        if x == t:
            count += 1
    
    return count


def deviation(xs: list[float]) -> list[float]:
    return [round(x - 7.06, 3) for x in xs]


def variance(xs: list[float]) -> list[float]:
    return [round(x**2, 3) for x in deviation(xs)]


def totaldev(xs: list[float]) -> float:
    return round(sqrt(totalvar(xs)), 3)


def totalvar(xs: list[float]) -> float:
    return round(1/(len(xs) - 1) * sum(variance(xs)), 3)


def main() -> None:
    
    # xs = [6.4, 8.25, 8.5, 2.15, 1.45, 5.05, 11.4, 11.6, 6.7, 9.65, 6.9, 6.65]
    # print(xs)
    # print("")
    # print(deviation(xs))
    # print("")
    # print(variance(xs))
    # print("")
    # print("totalvar=", totalvar(xs), "totaldev=", totaldev(xs))
    
    bs = [3, 5, 4, 3, 5, 3, 1, 4, 3, 4, 3, 3]
    for i in range(1, 7):
        print("abs=", abs(bs, i), "rel=", 1/len(bs) * abs(bs, i))
    print("")
    
    tpt = [2, 4, 3, 5, 6, 3, 2, 2, 2, 2, 3, 2]
    for i in range(1, 7):
        print("abs=", abs(tpt, i), "rel=", 1/len(tpt) * abs(tpt, i))


if __name__ == "__main__":
    main()
