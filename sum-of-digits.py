def digital_root(n):
    while n > 9:
        len_of_num = len(str(n))
        split_num = [int(str(n)[index]) for index in range(len_of_num)]
        n = sum(split_num)
    return n
