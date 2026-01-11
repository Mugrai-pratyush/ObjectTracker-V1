def histograminit(num):
    """
    initializes histogram with 0 initial values and an indexarr and also returns them
    """
    histValues=[]
    for i in range(0,num):
        histValues.append(0)
    return histValues
def PixelDictinit(num):
    """
    initializes Dict key 0 to num and values [] and also returns it
    """
    PixelDict={}
    for i in range(0,num):
        PixelDict[i]=[]
    return PixelDict
def histogramCreater(histogramArr,height,width,D2pixelarr):
    """
    Loops over D2pixelarr visiting each pixel once and recording the pixel value in an 0 initiated histogram array for that perticualr pixel
    pixels are b/w 0,255 ig we will check 
    inputs: height of the D2pixelarr
            width of the D2pixelarr
            D2pixelarr
            histogramArr
    returns: updated histogramArr
    """
    for i in range(0,height):
        for j in range(0,width):
            val=D2pixelarr[i][j]#between 0,255
            histogramArr[val]+=1
    return histogramArr
def dictCreator(PixelDict,height,width,D2pixelarr):
    """
    Loops over D2pixelarr visiting each pixel once and recording the pixel value in an 0 initiated dict val to key setup 
    where key is 0-255 and val is [x,y]
    input: height of the D2pixelarr
            width of the D2pixelarr
            D2pixelarr
            PixelDict
    returns: updated PixelDict
    """
    for i in range(0,height):
        for j in range(0,width):
            key=D2pixelarr[i][j]
            pixelPoseArr=[i,j]
            PixelDict[key].append(pixelPoseArr)
    return PixelDict
def squarefinder(dict):
    """
    Calulates points using pixeldict
    returns:Pointsarray
    """
    pointsarray=dict[255]
    A=pointsarray[0]
    forB=[]
    forC=[]
    for i in pointsarray:
        forB.append(i[1])
        forC.append(i[0])
    maxlateredge=max(forB)
    maxh=max(forC)
    B=[A[0],maxlateredge]
    C=[maxh,A[1]]
    D=[maxh,maxlateredge]
    points=[A,B,C,D]
    return points