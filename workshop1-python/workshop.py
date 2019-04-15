from PIL import Image

# RGB values for recoloring.

darkBlue = (0, 51, 76)
red = (217, 26, 33)
lightBlue = (112, 150, 158)
yellow = (252, 227, 166)

# Import image.

my_image = Image.open(raw_input("Picture name: ")) #change IMAGENAME to the path on your computer to the image you're using
image_list = my_image.getdata() # each pixel is represented in the form (red value, green value, blue value, transparency). You don't need the fourth value.
image_list = list(image_list) # Turns the sequence above into a list. The list can be iterated through in a loop.
recolored = [] #list that will hold the pixel data for the new image.

#YOUR CODE to loop through the original list of pixels and build a new list based on intensity should go here.
for pixel in image_list:
    # Calculate the intensity of the pixel, adjusting with a bias.
    intensity = (pixel[0] + pixel[1] + pixel[2]) / 3.
    # Based on the intensity color the new pixel.
    if intensity <= 64:
        recolored.append(darkBlue)
    elif intensity <= 128:
        recolored.append(lightBlue)
    elif intensity <= 192:
        recolored.append(yellow)
    else:
        recolored.append(red)

# Fix pixels.
fix_enable = raw_input("Fix pixels(y/n)? ") == "y"
if fix_enable:
    chunk_size = 3
    chunks = [range(i, i+chunk_size) for i in range(0, len(recolored), chunk_size)]
    for xs in chunks:
        # Filter out indexes that are out of bounds.
        xs = [i for i in xs if i < len(recolored)]
        num_lb = sum([1 if recolored[i] == lightBlue else 0 for i in xs])
        num_db = sum([1 if recolored[i] == darkBlue else 0 for i in xs])
        num_r = sum([1 if recolored[i] == red else 0 for i in xs])
        num_y = sum([1 if recolored[i] == yellow else 0 for i in xs])
        if num_lb >= chunk_size/2+1:
            for i in xs:
                recolored[i] = lightBlue
        elif num_db >= chunk_size/2+1:
            for i in xs:
                recolored[i] = darkBlue
        elif num_r >= chunk_size/2+1:
            for i in xs:
                recolored[i] = red
        elif num_y >= chunk_size/2+1:
            for i in xs:
                recolored[i] = yellow


# Create a new image using the recolored list. Display and save the image.
new_image = Image.new("RGB", my_image.size) #Creates a new image that will be the same size as the original image.
new_image.putdata(recolored) #Adds the data from the recolored list to the image.
new_image.show() #show the new image on the screen
new_image.save("recolored.jpg", "jpeg") #save the new image as "recolored.jpg"
