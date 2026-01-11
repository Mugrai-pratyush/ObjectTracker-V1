import random
def CreateBackground(height,Width):
    """
    Creates and reaturns the bacground basically 0 pixel values
    """
    bg=[]
    for i in range(0,height):
        newline=[]
        for j in range(0,Width):
            newline.append(0)
        bg.append(newline)
    return bg
def CreateSquare(height,width,side,bg,squarepixelVal):
    """
    Create a square ABDC and put it on the bg
    """
    pointhA=random.randint(0,height-side)
    pointwA=random.randint(0,width-side)
    h=0
    while h<side:
        w=0
        while w<side:
            poshA=pointhA+h
            posWA=pointwA+w
            bg[poshA][posWA]=squarepixelVal
            w+=1
        h+=1
    return bg
    


