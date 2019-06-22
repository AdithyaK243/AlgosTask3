
def strengthOfWall(wallLength, noOfBricks):
    brickStrengths = []
    for i in range(noOfBricks):
        x = int(input(""))
        brickStrengths.append(x)

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
