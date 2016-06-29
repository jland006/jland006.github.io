# -*- coding: utf-8 -*-
'''
Uses procedural programming paradigm instead of functional programming paradigm.
'''
import matplotlib.pyplot as plt

###
# Read the image data
###
fig, ax = plt.subplots(1, 1)


img = plt.imread("mario.jpg")
ax.imshow(img, interpolation='none')

height = len(img)
width = len(img[0])

for r in range(height):
    for c in range(width-205):
        if c % 4:
            img[r][c] = img[r][c+205]
      
plt.imsave("mario_shift.jpg", img)
fig.show()

