"""This program helps the user to find out the brain tumour from the brain MRI.
--- This program takes the image from the user and identifies the tumour in it.
--- Tumour is represented in red color.
--- Firstly, the original image is shown,
--- Secondly, the image will be shown, which will mark the sufficiently bright parts of the image 
    with red color indiacting the tuomor and rest of the part will be colored with green color indicating 
    that this region does not have any tumour.
--- Finally, the image of tumour in the brain will be shown. 
"""

from simpleimage import SimpleImage

BRIGHT_THRESHOLD = 200
DEFAULT_FILE = 'mri1.jpg'

def get_file():
    filename = input('Enter image file (or press enter for default): ')
    if filename == '':
        filename = DEFAULT_FILE
    return filename

def get_avg(pixel):
    return (pixel.red + pixel.green + pixel.blue) // 3

def trim_filename(original_filename, trim_size):
    
    new_width = original_filename.width - 2 * trim_size
    new_height = original_filename.height - 2 * trim_size
    trimmed_filename = SimpleImage.blank(new_width,new_height)

    for x in range(new_width):
        for y in range(new_height):
            old_x = x + trim_size
            old_y = y + trim_size
            orig_pixel =original_filename.get_pixel(old_x, old_y)
            trimmed_filename.set_pixel(x,y,orig_pixel)
    return trimmed_filename

def find_tumour(filename):
    for pixel in filename:
        pixel_avg = get_avg(pixel)
        if pixel.red >= BRIGHT_THRESHOLD:
            pixel.red = pixel_avg * 2
            pixel.green = 0
            pixel.blue = 0
        else:
            pixel.green = pixel_avg * 2
            pixel.red = 0
            pixel.blue = 0
    return filename

def main():

    filename = get_file()
    filename = SimpleImage(filename)
    filename.show()
    find_tumour_filename = find_tumour(filename)
    find_tumour_filename.show()
    trimmed_filename = trim_filename(filename, 40)
    find_tumour_filename = find_tumour(trimmed_filename)
    find_tumour_filename.show()
    

if __name__ == '__main__':
    main()