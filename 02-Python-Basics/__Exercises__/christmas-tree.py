picture = [
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 1, 1, 1, 0, 0],
    [0, 1, 1, 1, 1, 1, 0],
    [1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0]
]


for row in picture:
    row_length = len(row)
    pixelIdx = 0
    line_ending = ""
    while pixelIdx < row_length:
        pixel = row[pixelIdx]
        if pixelIdx == row_length - 1:
            line_ending = "\n"
        if pixel == 0:
            print(" ", end=line_ending)
        elif pixel == 1:
            print("*", end=line_ending)
        pixelIdx += 1
