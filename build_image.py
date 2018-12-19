from PIL import Image
import pyimgur
import image_pb2
import sys
import os
import psycopg2

DATABASE_URL = os.environ['DATABASE_URL']

conn = psycopg2.connect(DATABASE_URL, sslmode='require')


def rebuild_list(imagelist):
    graph = [["_","_","_"],
            ["_","_","_"],
            ["_","_","_"]]
    for i in range(0, len(imagelist)):
        j = -1
        if imagelist[i][0] == "A":
            j = 0
        elif imagelist[i][0] == "B":
            j = 1
        elif imagelist[i][0] == "C":
            j = 2

        k = -1
        if imagelist[i][1] == "1":
            k = 0
        elif imagelist[i][1] == "2":
            k = 1
        elif imagelist[i][1] == "3":
            k = 2

        if i%2 == 0:
            graph[k][j] = "o"
        else:
            graph[k][j] = "x"

    ooxx_str = ""
    for i in range(0, 9):
        ooxx_str = ooxx_str + graph[int(i/3)][i%3]

    return ooxx_str

def bind_image(imagelist, sender):
    image_name = rebuild_list(imagelist)
    cur = conn.cursor()

    cur.execute("SELECT * from IMGUR")
    rows = cur.fetchall()
    
    for row in rows:
        if row[0] == image_name:
            return row[1]
    #my_pb_file = "image.pb"

    #my_all_image = image_pb2.all_image()
    #my_all_image1 = image_pb2.all_image()

    #with open(my_pb_file, "rb") as f:
    #    my_all_image.ParseFromString(f.read())
    
    #for image in my_all_image.image:
    #    if image.name == image_name:
    #        #print("---\n\nyes\n\n---")
    #        return image.url
        
    
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
    rstPic.save(img_addr)
    
    CLIENT_ID = "9150a06aa5d4a85"
    #CLIENT_ID = os.environ['IMGUR_ID']
    PATH = img_addr

    im = pyimgur.Imgur(CLIENT_ID)
    uploaded_image = im.upload_image(PATH, title=sender)
    #print(uploaded_image.title)
    #print(uploaded_image.link)
    #print(uploaded_image.size)
    #print(uploaded_image.type)
    
    #new_image = my_all_image1.image.add()

    #new_image.url = uploaded_image.link
    #new_image.name = image_name

    #with open(my_pb_file, "ab") as f:
    #    f.write(my_all_image1.SerializeToString())

    cur.execute("INSERT INTO IMGUR VALUES('" + image_name+"', '"+uploaded_image.link+"');")
    conn.commit()

    return uploaded_image.link

