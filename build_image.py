from PIL import Image
import pyimgur

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

    img_addr = "binded_image/"+sender+".png"
    #儲存新的照片
    rstPic.save(img_addr)
    
    CLIENT_ID = "9150a06aa5d4a85"
    PATH = img_addr

    im = pyimgur.Imgur(CLIENT_ID)
    uploaded_image = im.upload_image(PATH, title=sender)
    #print(uploaded_image.title)
    #print(uploaded_image.link)
    #print(uploaded_image.size)
    #print(uploaded_image.type)
    
    

    return uploaded_image.link

