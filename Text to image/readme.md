##Text to Image
#Libraries required
    * Pillow(PIL fork) 
    * textwrap(To implement multi line text.)

This is a simple function to use PIL in a single line rather than calling different modules again and again.

You can provide the following parameters: 
* backgroundWidth :- Width of your background image to auto centre the text.
* height :- This is the height of your text object.
* imageLocation :- Location for background image.
* fontLocation :- Location for the font which is to be used.
* textString :- Whatever text you want.
* fontSize :- Size of the font you want(DUH!)
* offsetWidth :- If you want to offset text from centre.

There's a sample implementation of header and body using this function in sample file.

