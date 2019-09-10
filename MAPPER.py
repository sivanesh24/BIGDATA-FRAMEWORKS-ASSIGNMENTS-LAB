#!/usr/bin/python3

# The Mapper
import sys

# Set local variables
currentCountry = None
previousCountry = None
current = None
previous = None
percentChange = None
currentKey = None
Map = []

infile = sys.stdin

next(infile) # skip first line of input file

for line in infile:
    line = line.strip()
    line = line.split(',', 2)

    try:
        # Get data from line
        currentCountry = line[1].rstrip()
        if len(line[2]) == 0:
            continue
        current = float(line[2])

        if currentCountry != previousCountry:
            previousCountry = currentCountry
            previous = current
            previousLine = line
            continue

        # If country same as previous, add to map
        elif currentCountry == previousCountry:
            percentChange = ((current - previous) / previous) * 100.00
            percentChange = round(percentChange, 2)
            percentChange = percentChange

        currentKey = (currentCountry, percentChange)

        # Set the array with tuple keys
        Map.append(currentKey)

        # Update Values
        previousCountry = currentCountry
        previous = current
        previousLine = line

    # Handle unexpected errors
    except Exception as e:
        template = "An exception of type {0} occurred. Arguments:\n{1!r}"
        message = template.format(type(e).__name__, e.args)
        print("currentFx: %.2f previousFx: %.2f" % (current, previous))
        print(message)
        sys.exit(1)

# Show the returned values
for i in sorted(Map):
    print(",".join([str(x) for x in i]))
