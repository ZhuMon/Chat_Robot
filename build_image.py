from PIL import Image

def bind_image(imagelist, sender):
    rstPic = Image.new('RGBA', (180,180), (0,0,0,0))
    #open image
    for i in range(0, len(imagelist)):
        if i%2 == 0:
            imageA = Image.open("processing/"+imagelist[i]+"_o.png")
        else:
            imageA = Image.open("processing/"+imagelist[i]+"_x.png")
        imageA = imageA.convert('RGBA')
        rstPic.paste(imageA, (0,0), imageA)


    #儲存新的照片
    rstPic.save("binded_image"+sender+".png")

