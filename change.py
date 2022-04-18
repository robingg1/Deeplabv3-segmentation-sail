from pycocotools.coco import COCO
from PIL import Image
import imgviz
import tqdm
import os
import numpy as np
import shutil
import cv2

def save_colored_mask(mask, save_path):
    lbl_pil = Image.fromarray(mask.astype(np.uint8), mode="P")
    colormap = imgviz.label_colormap()
    lbl_pil.putpalette(colormap.flatten())
    lbl_pil.save(save_path)


anne_file='202203161116_coco.json'
coco = COCO(anne_file)
catIds = coco.getCatIds()
dic1={}
for i in range(len(catIds)):
    dic1[catIds[i]]=1+i-0.1

imgIds = coco.getImgIds()
print("catIds len:{}, imgIds len:{}".format(len(catIds), len(imgIds)))

os.makedirs('SegmentationClass', exist_ok=True)
os.makedirs('JPEGImages', exist_ok=True)

for imgId in tqdm.tqdm(imgIds, ncols=100):
    img = coco.loadImgs(imgId)[0]
    cat_ids = coco.getCatIds()

    anns_ids = coco.getAnnIds(imgIds=img['id'], catIds=cat_ids, iscrowd=None)
    anns = coco.loadAnns(anns_ids)

    if len(anns_ids) > 0:
        coco.showAnns(anns)
        mask = coco.annToMask(anns[0])
        for i in range(len(anns)):
            if anns[i]['category_id']=="cf6c9df68ded66fc2c9d509d76ae22cc":
                mask=coco.annToMask(anns[i])
        img_origin_path = os.path.join('202203161116', img['file_name'])
        img_output_path = os.path.join('JPEGImages', img['file_name'])
        seg_output_path = os.path.join('SegmentationClass', img['file_name'].replace('.jpg', '.png'))
        shutil.copy(img_origin_path, img_output_path)
        save_colored_mask(mask, seg_output_path)






