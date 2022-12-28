from Chef import Chef
from ChineseChef import ChineseChef  #ChineseChef took functions from Chef class using inheritance in those files.

myChef = Chef()
myChef.make_steak()


myChineseChef = ChineseChef()
myChineseChef.make_special_dish()
myChineseChef.make_salad()