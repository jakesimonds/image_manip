# image_manip

This was a class assignment where we built image filters in python utilizing a simple graphics library. I really enjoyed this project. 

In the top-left of the image below is the original image. Top-right is a filter where I created masks where each pixel got converted to a luminousity value and then assigned to whatever color it was closest in luminousity to, the three colors taken from a Warhol print. Bottom-right is the black & white filter I used for the previous filter, which I also used for the next filter. That filter (bottom-right) being a very rudimentary edge detector. I compared neighbor-pixel values, and then when there was a significant difference in luminousity between the pixels (an edge, hopefully), that pixel got assigned black, whereas non-edge pixels get assigned white. I then played around with sensitivity until I liked the product. 

<img width="874" alt="Screen Shot 2022-12-27 at 1 41 49 PM" src="https://user-images.githubusercontent.com/87023634/209709637-f86ec9bf-cbbf-4d25-a7a7-e154585825f7.png">
