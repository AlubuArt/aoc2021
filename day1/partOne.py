measurements = [int(string) for string in open('input.txt').readlines()]   

def countIncreases(input):
    previousMeasurement = input[0]
    count = 0

    for measurement in input:
        if measurement > previousMeasurement:
            count +=1
        previousMeasurement = measurement

    return count


def windows(input):
    window = [sum(input[i: i + 3]) for i in range(len(input) - 2)]
    return window

# part one
print(countIncreases(measurements))
# part two
print(countIncreases(windows(measurements)))