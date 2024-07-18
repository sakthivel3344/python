def countingValleys(steps, path):
    count = 0
    altitude = 0
    for ch in path:
        if (ch == 'U'):
            if (altitude < 0 and ((altitude + 1) >= 0)):
                count += 1
            altitude += 1
        else:
            altitude -= 1
    return count

print(countingValleys(8, "UDDDUDUU"))