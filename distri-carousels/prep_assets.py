import os
import sys
from PIL import Image, ImageChops
SRC = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Distri huisstijlen") + "/"
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "assets") + "/"

def trim(im, pad=0):
    bg = Image.new("RGBA", im.size, (0,0,0,0))
    diff = ImageChops.difference(im, bg)
    bbox = diff.getbbox()
    if bbox:
        im = im.crop(bbox)
    if pad:
        w,h = im.size
        canvas = Image.new("RGBA", (w+2*pad, h+2*pad), (0,0,0,0))
        canvas.paste(im, (pad,pad))
        im = canvas
    return im

def knockout_white(im, lo=215, hi=250):
    """Make near-white transparent with soft falloff between lo..hi on min channel."""
    im = im.convert("RGBA")
    px = im.load()
    w,h = im.size
    for y in range(h):
        for x in range(w):
            r,g,b,a = px[x,y]
            m = min(r,g,b)
            if m >= hi:
                px[x,y] = (r,g,b,0)
            elif m > lo:
                # partial alpha
                t = (m - lo)/(hi-lo)
                px[x,y] = (r,g,b,int(a*(1-t)))
    return im

# Mooideco
for name, out in [("Logo's/Original on Transparent.png","mooideco_color.png"),("Logo's/mooideco logo wit.png","mooideco_white.png"),("Logo's/Black on Transparent.png","mooideco_black.png")]:
    im = Image.open(SRC+"Mooideco/"+name).convert("RGBA")
    im = trim(im)
    im.thumbnail((2000,2000))
    im.save(OUT+out)
    print(out, im.size)

# Go International hi-res (white bg) -> knockout
im = Image.open(SRC+"Go International/Logo/goint hi res (2).jpg").convert("RGBA")
im.thumbnail((1600,1600))
im = knockout_white(im)
im = trim(im)
im.save(OUT+"goint_color.png"); print("goint_color.png", im.size)
# also a white-card version (original on white, trimmed)
im2 = Image.open(SRC+"Go International/Logo/goint hi res (2).jpg").convert("RGB")
im2.thumbnail((1600,1600))
im2.save(OUT+"goint_onwhite.jpg", quality=92)

# Segelken
im = Image.open(SRC+"Segelken/logo-website.jpg").convert("RGBA")
im = knockout_white(im, lo=225, hi=252)
im = trim(im)
im.save(OUT+"segelken_color.png"); print("segelken_color.png", im.size)
# white version for dark bg: recolor all opaque pixels to white
w = im.copy(); px = w.load()
for y in range(w.size[1]):
    for x in range(w.size[0]):
        r,g,b,a = px[x,y]
        if a>0: px[x,y] = (255,255,255,a)
w.save(OUT+"segelken_white.png")

# STX
flor = Image.open(SRC+"STX EU/FLOR SOLID.png").convert("RGBA"); flor = trim(flor); flor.thumbnail((800,800)); flor.save(OUT+"stx_flor.png"); print("flor", flor.size)
full = Image.open(SRC+"STX EU/1.SempertexEurope_Origineel_RGB.png").convert("RGBA"); full = trim(full); full.thumbnail((1600,1600)); full.save(OUT+"stx_full.png"); print("full", full.size)
# white flor (monochrome) for dark bg: keep colors (flor is colourful, that's the point). Also make a white version of full logo
fw = full.copy(); px = fw.load()
for y in range(fw.size[1]):
    for x in range(fw.size[0]):
        r,g,b,a = px[x,y]
        if a>0: px[x,y] = (255,255,255,a)
fw.save(OUT+"stx_full_white.png")
