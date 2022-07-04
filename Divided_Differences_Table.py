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
