def return_tab(tab):
    line = '-' * 13 + '\n'
    table = line
    for i in range(3):
        table += f'| {tab[0 + i * 3]} | {tab[1 + i * 3]} | {tab[2 + i * 3]} |\n'
        table += line
    return table
