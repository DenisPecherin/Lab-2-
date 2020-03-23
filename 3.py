# Решите задачу о Ханойской башне
def moveTower(height, fp, tp, wp):
    if height >= 1:
        moveTower(height-1, fp, wp, tp)
        moveDisk(fp, tp)
        moveTower(height-1, wp, tp, fp)

def moveDisk(fp,tp):
    print("Переложить диск с",fp,"на",tp)
n = int(input("Введите высоту башни\n"))
moveTower(n,"A","B","C")
