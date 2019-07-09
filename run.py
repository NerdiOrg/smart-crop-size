from PIL import Image
import os, glob, sys
def start():
    width = int(input("Please type the desired crop width without 'px' and press ENTER!"))
    height = int(input("Please type the desired crop height without 'px' and press ENTER!"))
    stretch = int(input("Type 1 to stretch images that are too small. Type 0 to skip them (no crop). Press ENTER when done."))
    input("Press any key to start cropping, or close out. Every png, jpg/jpeg, and gif file in the current directory of imgcrop.py will be cropped!")
    crop(width, height, stretch)
    print("\r\n")
    print("Thank you for using William Passmore's 'usefulPython' bulk image cropping & resizing tool (SmartCropSize.py)!")
    print("https://github.com/NerdiOrg/usefulPython/blob/master/images/SmartCropSize.py")

def crop(width, height, stretch):
    searchdir = "./" # end in slash!
    os.chdir(searchdir) # this directory
    savepath = searchdir + "crops" # single folder, do not include end slash!
    if not os.path.exists(savepath):
        os.mkdir(savepath)

    if not os.path.exists(savepath):
        sys.exit("The folder "+savepath+" does not exist & could not be generated!")

    types = ("png", "jpg", "jpeg", "gif")
    for type in types:
        print("Searching for '."+type+"' files in path: "+savepath)
        for file in glob.glob("*."+type):
            img = Image.open(file) # open the img
            original_width, original_height = img.size # dimensions of the img
            if(original_width < width):
                if(stretch == 0):
                    print("Image"+file+" has a width smaller than desired crop dimension & has been skipped.")
                    continue

            if(original_height < height):
                if(stretch == 0):
                    print("Image"+file+" has a height smaller than desired crop dimension & has been skipped.")
                    continue

            print("Cropping & Sizing: " +file)
            savepathfile = savepath + "/" + file

            if width > height:
                ratio = float(height / width)
                newheight = original_width * ratio
                if(newheight > original_height):
                    newwidth = original_height * (width/height)
                    newheight = original_height
                else:
                    newwidth = original_width

            else:
                ratio = float(width / height)
                newwidth = original_height * ratio
                if(newwidth > original_width):
                    newheight = original_width * (height/width)
                    newwidth = original_width
                else:
                    newheight = original_height


            # offsets are used to make sure image center is preserved, we crop sides equally!
            offsetwidth = (original_width - newwidth) / 2
            offsetheight = (original_height - newheight) / 2

            # Resize will make sure the aspect ratio is preserved AND also use offsets
            resize = (offsetwidth,offsetheight,original_width-offsetwidth,original_height-offsetheight)

             # crop to desired aspect ratio & resize to desired w/h
            img = img.crop(resize).resize((width,height))

            # save the image
            img.save(savepathfile, "PNG") # save img
            print("Saved image: " + savepathfile)


start()
