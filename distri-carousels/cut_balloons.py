from PIL import Image, ImageDraw, ImageFilter, ImageChops
import os
SRC = "/tmp/claude-chrome-screenshots-HjkNgC/"
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)),"balloons")+"/"
shots = {
 "screenshot-1793630073447-2.jpg": ["rosewood","eucalyptus","greentea"],
 "screenshot-1793630073447-3.jpg": ["golddust","duskrose","mattepink"],
 "screenshot-1793630073447-4.jpg": ["matteyellow","reflexgold","matteblue"],
 "screenshot-1793630087923-5.jpg": ["whitesand","red","yellow"],
 "screenshot-1793630087923-6.jpg": ["royalblue","limegreen","fuchsia"],
 "screenshot-1793630087924-7.jpg": ["orange","violet","caribbean"],
}
S = 1568/1920
for f, keys in shots.items():
    im = Image.open(SRC+f).convert("RGB")
    for i, k in enumerate(keys):
        x0 = int((20 + i*640)*S) - 4; x1 = int((20 + i*640 + 620)*S) + 4
        y0 = 0; y1 = int(900*S)
        cell = im.crop((max(x0,0), y0, min(x1, im.width), min(y1, im.height))).convert("RGB")
        # flood fill background from 4 corners with sentinel
        sent = (255, 0, 255)
        w, h = cell.size
        for seed in [(1,1),(w-2,1),(1,h-2),(w-2,h-2),(w//2,1),(w//2,h-2),(1,h//2),(w-2,h//2)]:
            if cell.getpixel(seed) != sent:
                ImageDraw.floodfill(cell, seed, sent, thresh=34)
        # alpha mask: sentinel -> 0, else 255
        r,g,b = cell.split()
        mask = Image.eval(ImageChops.add(ImageChops.difference(r, Image.new("L",(w,h),255)), ImageChops.add(g, ImageChops.difference(b, Image.new("L",(w,h),255)))), lambda v: 255 if v>0 else 0)
        # simpler: build mask by pixel test
        px = cell.load(); m = Image.new("L", (w,h), 255); mp = m.load()
        for y in range(h):
            for x in range(w):
                if px[x,y] == sent: mp[x,y] = 0
        m = m.filter(ImageFilter.MinFilter(3)).filter(ImageFilter.GaussianBlur(0.8))
        rgb = Image.open(SRC+f).convert("RGB").crop((max(x0,0), y0, min(x1, im.width), min(y1, im.height)))
        out = rgb.copy(); out.putalpha(m)
        bbox = m.point(lambda v: 255 if v>8 else 0).getbbox()
        out = out.crop(bbox)
        out.save(OUT+f"{k}.png")
        print(k, out.size)
