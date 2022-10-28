import os, sys
from PIL import Image

#modified from pillow tutorial
def jpeg(img):
    outfile = os.path.splitext(img)[0] + ".thumbnail"
    print(outfile)
    if img != outfile:
        try:
            with Image.open(img) as im:
                im.save(img, "JPEG")
        except OSError:
            print("cannot convert", img)

def split(im):
    source = im.split()

    R, G, B = 0, 1, 2

    # select regions where red is less than 100
    mask = source[R].point(lambda i: i < 100 and 255)

    # process the green band
    out = source[G].point(lambda i: i * 0.7)

    # paste the processed band back, but only where red was < 100
    source[G].paste(out, None, mask)

    # build a new multiband image
    im = Image.merge(im.mode, source)

    return im

def pixel(src, dim, col):
    #with Image.open(img) as src:

    #src.show() 
    #if src.mode() != "P":
    
    #src.convert("P")
    #m = src.mode
    #print(m)
    w, h = src.size

    pixelWidth = w//dim
    pixelHeight = h//dim

    boxt = [0,0,pixelWidth,pixelHeight]
    while boxt[2] <= w:
        while boxt[3] <= h:
            box=tuple(boxt)
            region = src.crop(box)
            region = region.quantize(col)
            src.paste(region, box)
            boxt[1]=boxt[1]+(pixelHeight)
            boxt[3]=boxt[3]+(pixelHeight)
        boxt[1]=0
        boxt[3]=pixelHeight
        boxt[0]=boxt[0]+(pixelWidth)
        boxt[2]=boxt[2]+(pixelHeight)


    #box = (0,0,2*pixelWidth,2*pixelHeight)
    #box2 = (4*pixelWidth,4*pixelHeight,8*pixelWidth,8*pixelHeight)
    #pixel1 = src.crop(box)
    #pixel1.show()
    #pixel2 = src.crop(box2)
    #pixel2.show()
    src.show()
    #output = Image.new(src.mode,src.size(),None)
    return src

#j = jpeg("grinning-face.png")
#px = split(Image.open("money-with-wings.png"))
#pixels must divide 128
# rgba_image = Image.open("1f92c.png")
# rgba_image.load()

# background = Image.new("RGB", rgba_image.size, (255, 255, 255))

# background.paste(rgba_image, mask = rgba_image.split()[3])

# background.save("sample_2.jpg", "JPEG", quality=100)


# im = Image.open("sample_2.jpg")
# im.show()
# #im.convert("P")
# ic = im.convert(mode="P")
# #ic = im.convert(mode="P", palette=Image.ADAPTIVE, colors=16)
# ic.show

p = pixel(Image.open("1f92c.png"),32,1)

#print(p.mode)
#p2 = pixel(p,32,4)
#p3 = pixel(p2,16,1)
#p4 = pixel(p3,16,1)