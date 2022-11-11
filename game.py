from print_tab import print_tab as pt
from input_data import input_data
from check import check


def main(tab):
    counter = 0
    win = False
    while not win:
        pt(tab)
        if counter % 2 == 0:
            input_data("\U0001F608", tab)
        else:
            input_data("\U0001F47D", tab)
        counter += 1
        if counter > 4:
            tmp = check(tab)
            if tmp:
                print (tmp, "выиграл! \N{grinning face}")
                win = True
                break
        if counter == 9:
            print ("Ничья! \U0001F92A")
            break
    print("Итоговая таблица: \U0001F4AF")
    pt(tab)


tab = list(range(1,20))

main(tab)