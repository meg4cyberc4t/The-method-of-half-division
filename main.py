import os

def solve(function, variable):
    print(function.replace("x", f"({str(variable)})"))
    answer = float(eval(function.replace("x", f"({str(variable)})")))
    print(answer)
    return answer

def main():
    os.system('clear')
    formula = input('f(x) = ')
    min = float(input("min = "))
    max = float(input("max = "))

    if (solve(formula, min) * solve(formula, max) > 0):
        print('Корней нет или больше одного')
        exit(0)

    vos = False if solve(formula, min) > solve(formula, (min + max) / 2) else True
    print(f"{vos}")

    while True:
        middleX = (min + max) / 2
        middleX = round(middleX, 3)
        middleY = solve(formula, middleX)
        if middleY == 0:
            break
        if not vos and middleY < 0:
            min, max = min, middleX
        elif vos and middleY > 0:
            min, max = min, middleX
        else: 
            min, max = middleX, max 

    
    print(f"{middleX=}, {middleY=}")
        
    
if __name__ == "__main__":
    main()
