input = [line.strip() for line in open('input.txt')]

# Part one


def getColumns(input):
    columns = []
    for column in range(len(max(input))):
        columns.append([n[column] for n in input])
    return columns


def construct():
    gammarate = ""
    epsilonrate = ""
    col = getColumns(input)
    # print(col)
    for column in col:
        gammarate += max(set(column))
        epsilonrate += min(set(column))
    #print(gammarate, epsilonrate)
    gammarate = gammarate
    epsilonrate = epsilonrate
    #print(gammarate * epsilonrate)
    return gammarate, epsilonrate


construct()


# part two

def findRatings():
    def max_binary(l):
        if l.count("0") > l.count("1"):
            return "0"
        else:
            return "1"

    def min_binary(l):
        if l.count("1") < l.count("0"):
            return "1"
        else:
            return "0"

    genRating = input
    scrubRating = input

    
    for i in range(len(max(input, key=len))):
        mostCommon = max_binary([n[i] for n in genRating])
        leastCommon = min_binary([n[i] for n in scrubRating])

        if len(genRating) > 1:
            genRating = list(filter(lambda n: n[i] == mostCommon, genRating))

        if len(scrubRating) > 1:
            scrubRating = list(
                filter(lambda n: n[i] == leastCommon, scrubRating))

    
    genRating = int(genRating[0], 2)
    scrubRating = int(scrubRating[0], 2)

    
    print(genRating)
    print(scrubRating)
    print(genRating * scrubRating)


findRatings()
