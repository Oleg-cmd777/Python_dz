import controller
import model
import view
import sys
model.init_nul()
x = input("Введите задачу и нажмите enter: ")
print(eval(x))#######################РЕШЕНИЕ СТРОЧНЫМ ФОРМАТОМ
sys.exit(0)


model.init_first()
while True:
    if model.init_ops():
        break
    model.init_second()
    controller.operation()
    view.print_total()
    model.first = model.total


while True: print(e