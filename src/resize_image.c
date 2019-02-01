#include <stdlib.h>
#include <stdio.h>
#include <math.h>
#include "image.h"

float nn_interpolate(image im, float x, float y, int c)
{
    // TODO Fill in
    float result = 0;
    x = round(x);
    y = round(y);
    result = get_pixel(im, x, y, c);
    return result;
}

image nn_resize(image im, int w, int h)
{
    // TODO Fill in (also fix that first line)
    float ax = (float)(im.w) / (float)(w);
    float ay = (float)(im.h) / (float)(h);
    float bx = 0.5 * (ax - 1);
    float by = 0.5 * (ay - 1);
    int size_column = w; 
    int size_row = h;
    int size_channel = im.c;
    int index = 0;
    float map_value_x = 0;
    float map_value_y = 0;
    image nn_resize_img = make_image(size_column, size_row, size_channel);
    // TODO Fill this in
    nn_resize_img.data = calloc(size_column*size_row*size_channel, sizeof(float));

    for(int k = 0; k < size_channel; ++k){
        for(int j = 0; j < size_row; ++j){
            for(int i = 0; i < size_column; ++i){
                index = i + size_column*j + size_column*size_row*k;
                map_value_x = (ax * i) + bx;
                map_value_y = (ay * j) + by;
                nn_resize_img.data[index] = nn_interpolate(im, map_value_x, map_value_y, k);
            }
        }
    }
    return nn_resize_img;
}

float bilinear_interpolate(image im, float x, float y, int c)
{
    // TODO
    return 0;
}

image bilinear_resize(image im, int w, int h)
{
    // TODO
    return make_image(1,1,1);
}

