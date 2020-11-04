from PIL import Image,ImageDraw,ImageFont
import textwrap

def texttoimg(backgroundWidth,height,imageLocation,fontLocation,textString,fontSize,offsetWidth=0):
    img = Image.open(imageLocation).convert("RGBA")
    txt = Image.new("RGBA", img.size, (255,255,255,0))
    fontName = ImageFont.truetype(fontLocation, fontSize)
    d = ImageDraw.Draw(txt)
    w, h = d.textsize(textString, font=fontName)
    d.text((((backgroundWidth-w)/2 + offsetWidth),height), textString, font=fontName, fill=(255,255,255,255))
    out = Image.alpha_composite(img, txt)
    out.save("new.png")
