if __name__ == '__main__':

    string_format = "{0:2} | {2:3} | {3:_>8} | {1:4.2f}"

    for i in range(11):
        print(string_format.format(i, i ** .5, i ** 2, i ** 3))
