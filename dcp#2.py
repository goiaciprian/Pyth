
def prodArray(array: list):
    """
    Return a list of the product of all items in the array exept the index.

    :param list iter: Input an array
    :return list: Return a list of the product of all items in the array exept
    the index.
    """

    returnedList, prodTotal = [], 1
    for i in array:
        prodTotal *= i

    for i in array:
        returnedList.append(int(prodTotal/i))

    return returnedList

if __name__ == "__main__":
    print(prodArray([1, 2, 3, 4, 5]))
