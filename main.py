import Divided_Differences_Table
while True:
    size = int(input("What is your size table:\n"))
    new_table = []
    print("Please enter your table values in this way: Enter value x and then the value f(x)")
    while len(new_table) < size:
        new_table.append([float(input()), float(input())])

    print("Your table:\nx\t  f(x)")
    for i in range(0, len(new_table)):
        print(new_table[i][0], " ", new_table[i][1])
    option = input("To change the table please press '1', otherwise press 2\n")
    if option == '2':
        break

Divided_Differences_Table.divided_differences_table(new_table)
