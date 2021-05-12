import numpy as np
import cv2 as cv
import os


def mask_n_bit_of_image(img_array, mask):
    """
    Applies a mask bitwise on an image to make the n lowest bit zero
    :param img_array: input image
    :param mask: mask to make the n lowest significant bits zero. Maske sample: int('11111110', 2)
    :return: masked image
    """
    for i in range(img_array.shape[0]):
        for j in range(img_array.shape[1]):
            new_value = img_array[i, j] & mask
            img_array[i, j] = new_value

    return img_array


def draw_img_side_by_side(img1, img2, caption):
    h_im = cv.hconcat([img1, img2])
    cv.imshow(caption, h_im)


def write_img(path, name, img):
    """
    :param path:
    :param name:
    :param img:
    :return:
    """
    name = os.path.join(path, name)
    cv.imwrite(name, img)


# print('current working directory is {}'.format(os.getcwd()))
img_path = os.path.join(os.getcwd(), 'lena.png')

img = cv.imread(img_path, 1)
cv.imshow('original image', img)
img_cp = img.copy()
path_dest = os.path.join(os.getcwd(), '2.jpeg')
print('Original image shape {}'.format(img.shape))


mask = int('11111110', 2)
print('mask = {}'.format(mask))
img_n1 = mask_n_bit_of_image(img, mask)
draw_img_side_by_side(img_cp, img_n1, 'Modified image n=1')
# write_img(path_dest, 'cn1.jpg', img_n1)


mask = int('11111100', 2)
print('mask = {}'.format(mask))
img_n2 = mask_n_bit_of_image(img, mask)
draw_img_side_by_side(img_cp, img_n2, 'Modified image n=2')
# write_img(path_dest, 'cn2.jpg', img_n2)


mask = int('11111000', 2)
print('mask = {}'.format(mask))
img_n3 = mask_n_bit_of_image(img, mask)
draw_img_side_by_side(img_cp, img_n3, 'Modified image n=3')
# write_img(path_dest, 'cn3.jpg', img_n3)


mask = int('11110000', 2)
print('mask = {}'.format(mask))
img_n4 = mask_n_bit_of_image(img, mask)
draw_img_side_by_side(img_cp, img_n4, 'Modified image n=4')
# write_img(path_dest, 'cn4.jpg', img_n4)


mask = int('11100000', 2)
print('mask = {}'.format(mask))
img_n5 = mask_n_bit_of_image(img, mask)
draw_img_side_by_side(img_cp, img_n5, 'Modified image n=5')
vis = np.concatenate((img_cp, img_n5), axis=1)
cv.imwrite('steg2_thumbnail.png', vis)
# write_img(path_dest, 'cn5.jpg', img_n5)


mask = int('11000000', 2)
print('mask = {}'.format(mask))
img_n6 = mask_n_bit_of_image(img, mask)
draw_img_side_by_side(img_cp, img_n6, 'Modified image n=6')
# write_img(path_dest, 'cn6.jpg', img_n6)


mask = int('10000000', 2)
print('mask = {}'.format(mask))
img_n7 = mask_n_bit_of_image(img, mask)
draw_img_side_by_side(img_cp, img_n7, 'Modified image n=7')
# write_img(path_dest, 'cn7.jpg', img_n7)


mask = int('00000000', 2)
print('mask = {}'.format(mask))
img_n8 = mask_n_bit_of_image(img, mask)
draw_img_side_by_side(img_cp, img_n8, 'Modified image n=8')
# write_img(path_dest, 'cn8.jpg', img_n8)

cv.waitKey(0)