def convertToSingle(num):
    total = 0
    noOfDigits = 0
    tempNum = 0
    while num != 0:
        tempNum = num % 10
        total += tempNum
        num = num // 10
        noOfDigits += 1

    if total > 9:
        return 1 + convertToSingle(total)
    else:
        return 1


def main():
    # Enter the number
    num = int(input(""))
    print(convertToSingle(num))


if __name__ == "__main__":
    main()
