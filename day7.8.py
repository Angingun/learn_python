# 约瑟夫环问题


def main(n, m):
     """
        环的问题，
        共有n个人围成一圈，从1开始报数，数到m时退出，再从1开始，直到所有人退出
    """
    persons = [True] * n
    counter, index, num = 0, 0, 0
    while counter < m:
        if persons[index]:
            num += 1
            if num == 9:
                persons[index] = False
                counter += 1
                num = 0
        index += 1
        index %= 30
    for person in persons:
        print('C' if person else 'N', end='')
    for i, person in enumerate(persons):
        if person:
            print(i+1,)


if __name__ == "__main__":
    main(30, 15)
