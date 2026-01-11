import matplotlib.pyplot as plt
def visual(Bg_square):
    """
    makes a visual image using Greyscale Values
    """
    plt.imshow(Bg_square,cmap="gray",vmin=0,vmax=255)
    plt.axis("off")
    plt.show()