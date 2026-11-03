import sys, os
from PIL import Image
import os
OUT=os.environ.get("SHEET_OUT",os.path.join(os.path.dirname(os.path.abspath(__file__)),"out"))
for name in sys.argv[1:]:
    d=f"{OUT}/{name}"
    ims=[Image.open(f"{d}/slide-{i:02d}.png") for i in range(1,8)]
    tw=540; th=675
    sheet=Image.new("RGB",(tw*4+50, th*2+30),(60,60,60))
    for i,im in enumerate(ims):
        im=im.resize((tw,th), Image.LANCZOS)
        sheet.paste(im,((i%4)*(tw+10)+10,(i//4)*(th+10)+10))
    sheet.save(f"{OUT}/{name}_sheet.jpg", quality=80)
    print(f"{OUT}/{name}_sheet.jpg")
