from visual import *
from Simulation import *
from CreateBackgroundandSquare import *
def main():
    runs=int(input("Enter number of runs:"))
    Height=int(input("Enter Height:"))
    Width=int(input("Enter Width:"))
    Side=int(input("Enter side:"))
    White=255
    Patharr=Sim(runs,Height,Width,Side,White)
    for i in range(0,runs):
        bg=CreateBackground(Height,Width)
        Bg_Square=CreateSquare(Height,Width,Side,bg,White)
        print(f"frame:{i}")
        visual(Bg_Square)
    path=0
    while path<len(Patharr):
        index=0
        Square=Patharr[path]
        print(f"pos{path}:A:{Square[index]},B:{Square[index+1]},C:{Square[index+2]},D:{Square[index+3]}\n")
        path+=1
if __name__ == "__main__":
    main()