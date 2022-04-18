import os

path=anne_file='202203161116'
origin='C:\\Users\\27654\\PycharmProjects\\pythonProject2'
list = os.listdir(path)
os.makedirs(os.path.join(origin,'imageset'))
os.makedirs(os.path.join(origin,'imageset','Segmentation'))


f1=open(os.path.join(origin,'imageset\\Segmentation\\train.txt'),'w')
for i in range(len(list)-10):
    f1.write(list[i][:-4]+'\n')



f1=open(os.path.join(origin,'imageset\\Segmentation\\val.txt'),'w')
for i in range(8):
    f1.write(list[i+70][:-4]+'\n')

f1=open(os.path.join(origin,'imageset\\Segmentation\\trainval.txt'),'w')
for i in range(6):
    f1.write(list[i+20][:-4]+'\n')

