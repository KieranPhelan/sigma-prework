import math


def calculate_min_max(numbers):
    min = math.inf
    max = -math.inf

    for number in numbers:
        if number < min:
            min = number

        if number > max:
            max = number

    return [min, max]


def main():
    int1 = [2, 4, 1, 0, 2, -1]
    int2 = [20, 50, 12, 6, 14]
    int3 = [100, -100]

    minmax = calculate_min_max(int1)
    print(minmax)

    minmax = calculate_min_max(int2)
    print(minmax)

    minmax = calculate_min_max(int3)
    print(minmax)


if __name__ == "__main__":
    main()
