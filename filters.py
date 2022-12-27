'''
Jake Simonds
Project 6 - Warhol Art Generator
filters file
Due 3/4

'''

#importing graphics plus for filters and sys for command line
import graphicsPlus as gp
import sys

import random


    #this filter was built during 2/25 recitation, and swaps the Red and Blue rgb values
def swapRedBlue(image) :
    #nesting for loops to process the image one pixel at a time, i for width, j for height
    for i in range(image.getWidth()):  
        for j in range (image.getHeight()): 
            #original pixel values, broken into three variables for r, g & b
            og_pixel_r = image.getPixel(i,j)[0]
            og_pixel_g = image.getPixel(i,j)[1]
            og_pixel_b = image.getPixel(i,j)[2]
            #this line does a lot: it sets each pixel in a new image, having swapped the values for R & B
            # i, j are coordinates of pixel
            # gp.color_rgb sets the color of this new pixel, and using the variables from above swaps R & B
            #image.setPixel sets this new manipulated pixel in the filtered image
            image.setPixel(i,j,gp.color_rgb(og_pixel_b,og_pixel_g,og_pixel_r))


#extension filter
#this filter makes a rough greyscale of an image by averaging RGB to one value
def grey(image) : 
    #nesting for loops to process image by pixel
    for i in range(image.getWidth()):  
        for j in range (image.getHeight()): 
            #original pixel values as variables
            og_pixel_r = image.getPixel(i,j)[0]
            og_pixel_g = image.getPixel(i,j)[1]
            og_pixel_b = image.getPixel(i,j)[2]
            #new variable of average, which is just average of r,g & b
            average = int((og_pixel_b+og_pixel_g+
            og_pixel_r)/3)
            #i & j are coordinates, gp.color_rgb just sets that new pixel to use the average for R, G, and B. 
            #image.setPixel sets these new pixels in the filtered image
            image.setPixel(i,j,gp.color_rgb(average, average, average))

#this filter uses colors from a warhol print of Marilyn Monroe, tries to imitate it. Colors are...
#rgb(239,95,129) pink
#rgb(235,238,132) yellow
#rgb(53, 47, 43) black-ish
#using average idea from greyscale above, I get the average for each pixel, but instead of converting it to grey...
#...I convert it to pink, yellow, or black-ish, depending on the light-dark of it, which is represented by numerical average
def imitate(image): 
    #nested for loops to process the image pixel by pixel, i for width, j for height
    for i in range(image.getWidth()):  
        for j in range (image.getHeight()): 
            #original pixel values
            og_pixel_r = image.getPixel(i,j)[0]
            og_pixel_g = image.getPixel(i,j)[1]
            og_pixel_b = image.getPixel(i,j)[2]
            #taking average of RGB
            average = int((og_pixel_b+og_pixel_g+og_pixel_r)/3)
            #sets averages 70-128 to pink
            #ranges are somewhat arbitrary - 175 is about halfway between yellow & pink RGB averages
            if average < 175 and average >= 70 : 
                image.setPixel(i,j,gp.color_rgb(239, 95, 129))
            #sets above 175 to yellow
            elif average >= 175: 
                image.setPixel(i,j,gp.color_rgb(235, 238, 132))
            #sets stuff below 70 to "black"ish
            # 70 chosen as just a bit above black-ish average
            elif average < 70 : 
                image.setPixel(i,j,gp.color_rgb(53, 47, 43))


#this filter was based off of my own poor understanding of some computer vision techniques
#The idea was to try to make a filter that would outline shapes by detecting where pixels are different than their neighbor
#this filter does so, but only checking the neighbor directly above.
#if the above pixel's average value of RGB is more than five points different, that pixel is black. Otherwise, pixel is white
def outline(image):
    #nested for loops like previous filters
    for i in range(image.getWidth()):  
        for j in range (image.getHeight()): 
            #original pixel values
            og_pixel_r = image.getPixel(i,j)[0]
            og_pixel_g = image.getPixel(i,j)[1]
            og_pixel_b = image.getPixel(i,j)[2]
            #taking average of RGB
            average = int((og_pixel_b+og_pixel_g+og_pixel_r)/3)
            #this if/else is a lazy fix so bumping up the neighbor pixel doesn't take us out of range, causing an error
            #only affects top line of pixels, so I was okay with that compromise on the image
            if (j+1) < len(range(image.getHeight())): 
                neighbor_j = j + 1
            else: 
                neighbor_j = j
            #neighbor j in all cases except the very top row of pixels is +1, taking us to the pixel above us
            #making variables for r, g & b of this upstairs neighbor
            neighbor_r = image.getPixel(i,neighbor_j)[0]
            neighbor_g = image.getPixel(i,neighbor_j)[1]
            neighbor_b = image.getPixel(i,neighbor_j)[2]
            #taking average for upstairs neighbor
            neighbor_av = int((neighbor_r+neighbor_g+neighbor_b)/3)
            #if absolute value of difference between the pixel's average and its neighbors average is less than 10, pixel = white
            if abs(average - neighbor_av) <= 5: 
                image.setPixel(i,j,gp.color_rgb(250, 250, 250))
            #otherwise, when there is a difference between the neighbors, that pixel is black
            else: 
                image.setPixel(i,j,gp.color_rgb(0, 0, 0))

RANDOM_NUM = 3

def pixel_drop(image): 
        #nested for loops like previous filters
    for i in range(image.getWidth()):  
        for j in range (image.getHeight()):
            if (random.randint(0,RANDOM_NUM) == RANDOM_NUM):
                image.setPixel(i,j,gp.color_rgb(250,250,250))

            

def pixel_drop2(image): 
        #nested for loops like previous filters
    for i in range(image.getWidth()):  
        for j in range (image.getHeight()):
            if (random.randint(0,RANDOM_NUM) == RANDOM_NUM):
                image.setPixel(i,j,gp.color_rgb(250,250,250))
    

    for i in range(image.getWidth()):  
        for j in range (image.getHeight()):
            if (image.getPixel(i,j)[0] == 250 & image.getPixel(i,j)[1] == 250):
                if (j+1) < len(range(image.getHeight())): 
                    neighbor_j = j + 1
                else: 
                    neighbor_j = j

                neighbor_r = image.getPixel(i,neighbor_j)[0]
                neighbor_g = image.getPixel(i,neighbor_j)[1]
                neighbor_b = image.getPixel(i,neighbor_j)[2]

                image.setPixel(i,j,gp.color_rgb(neighbor_r, neighbor_g, neighbor_b))

             





