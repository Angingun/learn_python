# 双色球选号

from random import randrange, sample


def display(balls):
    for index, ball in enumerate(balls):
        if index == len(balls) - 1:
            print('|', end=' ')
        print('{:>2d}'.format(ball, end=''))
    print()


def random_select():
    red_balls = [x for x in range(1, 34)]
    selected_balls = []
    selected_balls = sample(red_balls, 6)
    selected_balls.sort()
    selected_balls.append(randrange(1, 16))
    return selected_balls


def main():
    n = int(input('machine choose'))
    for _ in range(n):
        display(random_select())


if __name__ == "__main__":
    main()
