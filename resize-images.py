import os 
import glob # https://pynative.com/python-glob/
from PIL import Image, ImageOps


def resize_images(root, extension):
    
    path = f'{root}*{extension}'
    print(path)
    try:
        
        for file in sorted(glob.glob(path, recursive=False)):
            
            full_filename = f'{root}{os.path.basename(file)}'

            size = (500, 692)
            with Image.open(full_filename) as im:
                # ImageOps.contain(im, size).save("imageops_contain.jpg")
                # ImageOps.cover(im, size).save("imageops_cover.jpg")
                # ImageOps.fit(im, size).save("imageops_fit.jpg")
                ImageOps.pad(im, size, color="#cfd8dc").save(full_filename)

                # # thumbnail() can also be used,
                # # but will modify the image object in place
                # im.thumbnail(size)
                # im.save(full_filename)

    except Exception as e:
        print(e)


'''
Main function
'''

folder = 'C:\\Users\\brian\\OneDrive - Trinity Schools\\Classes\\9DGT\\9DGT-A\\Photos\\'


resize_images(folder, ".jpg")