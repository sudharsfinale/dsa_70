list = [2, 4, 5, 11]


def findFirstNNumber(number):
    # for number in list:
    for index in range(len(list)):
        if (list[index] == 11):
            return {"found": True, "Index": index}
        else:
            continue
    else:
        return {"found": False, "Index": index}


print(findFirstNNumber(11))
