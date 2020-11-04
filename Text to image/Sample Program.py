# This sample program uses textToImage function and output a image named new.png
import textwrap
from textToImage import texttoimg

# Background to write text on
backgroundWidth = 1920
imageLocation = input("Enter the name or location of background file:- ") 

# Section to generate header
textString =  input("Enter a Header:- ")
fontLocation = "./sample.ttf"
fontSize = 109
height = 192
texttoimg(backgroundWidth,height,imageLocation,fontLocation,textString,fontSize)

# Section to generate author's name
textString = "By " + input("Enter the name of the author/creator:- ")
height += 190
imageLocation = "./new.png"
fontLocation = "./sample.ttf"
fontSize = 62
texttoimg(backgroundWidth,height,imageLocation,fontLocation,textString,fontSize,470)

# Section to generate the pargraph
inputParagraph = input("Enter the body\n")
splitPara = textwrap.wrap(inputParagraph,width=62)
fontLocation = "./sample.ttf"
height = height + 200
fontSize = 70
imageLocation = "./new.png"
for line in splitPara:
    texttoimg(backgroundWidth,height,imageLocation,fontLocation,line,fontSize)
    height += 70
