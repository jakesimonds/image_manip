'''
Jake Simonds
'''

#to do: 
# ext: get it so you can choose color and size of font - get it into sys.argv
#clean up code
#finish report
#second ext. 

#importing sys for command line action, and functions for my functions as well as graphicsPlus per assignment
import graphicsPlus as gp
import sys
import filters

#print(sys.argv[0])


def main(argv) :
    #if user gives warhol.py and image name, and doesn't specify text size/color
    if len(argv) == 2: 
        #read image data from a file and assign it to four variables for quadrants
        image_t_l = gp.Image(gp.Point(0,0),argv[1])
        image_t_r = gp.Image(gp.Point(0,0),argv[1])
        image_b_l = gp.Image(gp.Point(0,0),argv[1])
        image_b_r = gp.Image(gp.Point(0,0),argv[1])
        #setting the width and height of our images as variables
        width = image_t_l.getWidth()
        height = image_t_l.getHeight()
        #making variables for the text in each quadrent. 
        #setting each text to the center of the quadrent, and 20 pixels up from the bottom of the image
        txt_t_l = gp.Text(gp.Point(width/2 , height - 20),"top left") 
        txt_t_r = gp.Text(gp.Point(width*1.5, height - 20),"top right") 
        txt_b_l = gp.Text(gp.Point(width/2,(2*height - 20)),"bottom left")
        txt_b_r = gp.Text(gp.Point(width*1.5,(2*height-20)),"bottom right") 
        
        #setting default for text when user doesn't specify
        text_size = 20
        text_color = "black"

        #setting text size and color for top-left corner text
        txt_t_l.setSize(text_size)
        txt_t_l.setTextColor(text_color)
        #for top right
        txt_t_r.setSize(text_size)
        txt_t_r.setTextColor(text_color)
        #bottom left
        txt_b_l.setSize(text_size)
        txt_b_l.setTextColor(text_color)
        #bottom right
        txt_b_r.setSize(text_size)
        txt_b_r.setTextColor(text_color)


        #create a graphwin window to display the image
        #width & height * 2 to make it big enough for grid
        window = gp.GraphWin("Image rendered", width*2, height*2)
        # moving images to quadrents
        image_t_l.move(width/2, height/2)
        image_t_r.move(width*1.5, height/2)
        image_b_l.move(width/2, height*1.5)
        image_b_r.move(width*1.5, height*1.5)
        #filter for t_r
        #imported from functions file
        filters.swapRedBlue(image_t_r)
        #filter for b_l
        filters.swapRedBlue(image_b_l)
        #filter for b_r
        filters.outline(image_b_r)
        
        #drawing images in all four quadrents
        image_t_l.draw(window)
        image_t_r.draw(window) 
        image_b_l.draw(window)
        image_b_r.draw(window)
        #writing text on the images for all four quadrents
        txt_t_l.draw(window)
        txt_t_r.draw(window)
        txt_b_l.draw(window)
        txt_b_r.draw(window)
        #wait for user input
        window.getMouse()

        #when the user selects text size and color
        #user  must select  both size and color, just one will produce an error
        #except for where we specify text size and color the code is identical to above (and above is commented a little better)
    elif len(argv) > 2: 
        #read image data from a file and assign it to four variables for quadrants
        image_t_l = gp.Image(gp.Point(0,0),argv[1])
        image_t_r = gp.Image(gp.Point(0,0),argv[1])
        image_b_l = gp.Image(gp.Point(0,0),argv[1])
        image_b_r = gp.Image(gp.Point(0,0),argv[1])
        #setting the width and height of our images as variables 
        width = image_t_l.getWidth()
        height = image_t_l.getHeight()
        #making variables for the text in each quadrent. 
        #setting each text to the center of the quadrent, and 20 pixels up from the bottom of the image
        txt_t_l = gp.Text(gp.Point(width/2 , height - 20),"Original Photo") 
        txt_t_r = gp.Text(gp.Point(width*1.5, height - 20),"Color Masks") 
        txt_b_l = gp.Text(gp.Point(width/2,(2*height - 20)),"Black & White")
        txt_b_r = gp.Text(gp.Point(width*1.5,(2*height-20)),"Edge Detection") 
        
        #taking input from command line for text size
        text_size = int(argv[2])
        #taking input from commmand line for text color
        text_color = str(argv[3])

        #setting text size and color for top-left corner text
        txt_t_l.setSize(text_size)
        txt_t_l.setTextColor(text_color)
        #for top right
        txt_t_r.setSize(text_size)
        txt_t_r.setTextColor(text_color)
        #bottom left
        txt_b_l.setSize(text_size)
        txt_b_l.setTextColor(text_color)
        #bottom right
        txt_b_r.setSize(text_size)
        txt_b_r.setTextColor(text_color)
        #create a graphwin window to display the image
        #width & height * 2 to make it big enough for grid
        window = gp.GraphWin("Image rendered", width*2, height*2)
        # moving images to quadrents
        image_t_l.move(width/2, height/2)
        image_t_r.move(width*1.5, height/2)
        image_b_l.move(width/2, height*1.5)
        image_b_r.move(width*1.5, height*1.5)
        #filters
        #filters.swapRedBlue(image_t_r)
        filters.imitate(image_t_r)
        filters.grey(image_b_l)
        #MAKING A CHANGE**********************************************************
        #filters.pixel_drop(image_t_l)
        #filters.pixel_drop2(image_b_l)
        filters.outline(image_b_r)
        #drawing images
        image_t_l.draw(window)
        image_t_r.draw(window) 
        image_b_l.draw(window)
        image_b_r.draw(window)
        #writing text on the images
        txt_t_l.draw(window)
        txt_t_r.draw(window)
        txt_b_l.draw(window)
        txt_b_r.draw(window)
        #wait for user input
        window.getMouse()


    elif len(argv) < 2 :  
        print("Hello, this Warhol Art generator takes an image and displays it in a grid with filters applied")
        print()
        print("User inputs should be formatted: ")
        print("File name - image you want manipulated - text size (5-36) - text color (ex: blue, red, green, etc)")

#just another way of calling main (conditional call to main function)
if __name__ == "__main__" :
    main(sys.argv)