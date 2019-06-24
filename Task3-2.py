
def strengthOfWall(wallLength, noOfBricks):
    brickStrengths = []
    brickStrengths = list(map(int, input().split()))

    brickStrengths.sort()

    i = noOfBricks
    while i > wallLength:
        brickStrengths[1] += brickStrengths[0]
        brickStrengths.pop(0)
        i -= 1

    return min(brickStrengths)


def main():
    wallLength = int(input(""))
    noOfBricks = int(input(""))
    print(strengthOfWall(wallLength, noOfBricks))


if __name__ == "__main__":
    main()
