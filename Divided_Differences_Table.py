def divided_differences_table(table):
    s = 1
    dividing = []  # for each dividing
    all_solution = []  # for all dividing
    for j in range(0, len(table) - 1):
        solution = []
        if j == 0:  # the first dividing
            for i in range(0, len(table) - j - 1):
                solution.append((table[i + 1][1] - table[i][1]) / (table[i + s][0] - table[i][0]))
        else:  # for other dividing
            for i in range(0, len(table) - j - 1):
                solution.append((dividing[i + 1] - dividing[i]) / (table[i + s][0] - table[i][0]))
        dividing = solution
        s += 1
        all_solution.append(solution)

    # print the values of each dividing
    print("x\t  f(x)\n-----------------")  # print the title
    for i in range(0, len(table)):
        print(table[i][0], " ", '%.5f' % table[i][1])
    print("\n")
    for i in range(0, len(all_solution)):
        print(i + 1, "dividing differences\n--------------------------")
        for j in all_solution[i]:
            print('%.5f' % j)
        print("\n")








    '''first = []
    for i in range(0, len(table) - 1):
        first.append((table[i + 1][1] - table[i][1]) / (table[i + 1][0] - table[i][0]))
    print(first)

    second = []
    for i in range(0, len(first) - 1):
        second.append((first[i + 1] - first[i]) / (table[i + 2][0] - table[i][0]))

    third = []
    for i in range(0, len(second) - 1):
        third.append((second[i + 1] - second[i]) / (table[i + 3][0] - table[i][0]))
    print(third)
    # print as a table
    print(len(first), "    sec", len(second), "   thi", len(third))
    print("i\tx\t  f(x)\t\t First divided differences\tSecond divided differences\tThird divided differences")
    print("----------------------------------------------------------------------------------------------------------")
    count_s = 0
    count_t = 0
    for i in range(0, len(table) - 1):
        print(i, " ", table[i][0], " ", '%.5f' % table[i][1])
        if 0 < i < (len(table) - 1):
            print("\t\t\t\t\t\t\t\t\t\t\t\t\t", '%.5f' % second[count_s])
            count_s += 1
        print("\t\t\t\t\t\t", '%.5f' % first[i])
        if 0 < i < (len(table) - 2):
            print("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t", '%.5f' % third[count_t])
            count_t += 1
    print(len(table) - 1, " ", table[len(table) - 1][0], " ", '%.5f' % table[len(table) - 1][1])'''
