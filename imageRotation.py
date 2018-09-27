def rotate(image):
    temp = [[0 for x in range(len(image))] for x in range(len(image))]
    size = len(image)

    for x in range(size):
        for y in range(size):
            temp[size - x - 1][y] = image[size - y - 1][x]

    return temp

image = [[1,2,3,4] for x in range(4)]

print(rotate(image))