from PIL import ImageGrab
import datetime

BASEPATH = "Z:/Docket/Source/img/"

# Save image from the cliboard
def save_clip_image():
    # create a filename based on the date time
    baseName="shot"
    suffix = datetime.datetime.now().strftime("%y%m%d_%H%M%S")
    filename = "_".join([baseName, suffix])
    imagePath = BASEPATH + filename + '.png'

    im = ImageGrab.grabclipboard()
    try:
        im.save(imagePath,'PNG')
        print(f'![[{filename}.png]]')

    except:
        print("![[No image copied on the clipboard.]]")

save_clip_image()