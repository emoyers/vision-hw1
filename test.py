from uwimg import *
im = load_image("data/dogsmall.jpg")
a = nn_resize(im, im.w*4, im.h*4)
save_image(a, "dog4x-nn")

a = bilinear_resize(im, im.w*4, im.h*4)
save_image(a, "dog4x-bl")

im = load_image("data/dog.jpg")
f = make_box_filter(7)
blur = convolve_image(im, f, 1)
save_image(blur, "dog-box7")
thumb = nn_resize(blur, blur.w//7, blur.h//7)
save_image(thumb, "dogthumb")

highpass = make_highpass_filter()
blur_h = convolve_image(im, highpass, 0)
clamp_image(blur_h)
save_image(blur_h, "doghighpass")

sharpen = make_sharpen_filter()
blur_sharp = convolve_image(im, sharpen, 1)
clamp_image(blur_sharp)
save_image(blur_sharp, "dog_sharpen")

emboss = make_emboss_filter()
blur_emboss = convolve_image(im, emboss, 1)
clamp_image(blur_emboss)
save_image(blur_emboss, "dog_emboss")

f = make_gaussian_filter(2)
blur_gaussian = convolve_image(im, f, 1)
save_image(blur_gaussian, "dog-gauss2")

f = make_gaussian_filter(2)
lfreq = convolve_image(im, f, 1)
hfreq = im - lfreq
reconstruct = lfreq + hfreq
save_image(lfreq, "low-frequency")
save_image(hfreq, "high-frequency")
save_image(reconstruct, "reconstruct")

res = sobel_image(im)
mag = res[0]
feature_normalize(mag)
save_image(mag, "magnitude")

direction = res[1]
feature_normalize(direction)
save_image(direction, "direction")

sobel_color = colorize_sobel(im)
save_image(sobel_color, "sobel_color")
