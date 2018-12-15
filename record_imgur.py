import image_pb2
import sys

def aaa():
    
    my_pb_file = "image.pb"

    my_all_img = image_pb2.all_image()

    num = input("How many? ")

    in_list = []
    for i in range(0, int(num)):
        in_data = input()
        in_list = in_data.split()
        new = my_all_img.image.add()
        new.name = in_list[0]
        new.url = in_list[1]


    with open(my_pb_file, "wb") as f:
        f.write(my_all_img.SerializeToString())

if __name__ == "__main__":
    aaa()
