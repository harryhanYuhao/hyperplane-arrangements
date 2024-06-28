def get_hyperplane_arrangements(data, modula):
    """
    Input:
        data is The equation that defines the hyperplanes in forms of
    m *(dimension + 1) matrix represented as a 2D python list

    Example:
    data = [
        [1, 2, 3],
        [1, 3, 4],
    ]
    The hyperplanes represented are x + 2y = 3, x + 3y + 4
        modula defines the field we are working on.
        The dimension is inferred from the width of the matrix


    return a list res, such that
    res[i] = j means there are j points intersected i times
    """

    def get_coor_from_index(index, dimension, modula):
        """
        Auxiliary Function
        """
        tmp = index % pow(modula, dimension)
        coor = []
        for i in range(1, dimension + 1):
            a = tmp // pow(modula, dimension - i)
            tmp -= a * pow(modula, dimension - i)
            coor.append(a)
        return coor

    #################
    # START OF EXECUTION
    #################
    dimension = len(data[0]) - 1
    # res[i] = j means there are j points intersected i times
    res = [0 for i in range(dimension + 1)]

    # Iterates through all the points in F_modula ^ dimension
    for index in range(pow(modula, dimension)):
        coor = get_coor_from_index(index, dimension, modula)
        count = 0
        for i in data:
            sum = 0
            for j in range(len(i)-1):
                sum += coor[j] * i[j]
            if sum % modula == i[-1]:
                count += 1
        # make sure the list is long enough
        while count >= len(res):
            res.append(0)

        res[count] += 1

    #######
    # display and return
    #######
    for i, j in enumerate(res):
        print("{j:>5} points laying on {i} hyperplanes".format(j=j, i=i))

    return res


data = [
    [1, 2, 3, 1],
    [1, 3, 4, 0],
    [4, 1, 1, 0],
]
get_hyperplane_arrangements(data, 5)
