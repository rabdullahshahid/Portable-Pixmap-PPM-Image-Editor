#MUHAMMAD ABDULLAH 

#This Python program is a Portable Pixmap (PPM) Image Editor designed for basic image manipulation. It allows users to apply various effects to PPM images, such as converting to greyscale, flipping horizontally, adjusting color negativity, and more, through a simple and interactive command-line interface.





# Reads a PPM image file and returns its header and image data

def read_ppm(file_path):
    with open(file_path, 'r') as file:
        header = file.readline().strip() # PPM header (P3)
        dimensions = file.readline().strip().split() # Image dimensions
        max_val = file.readline().strip() # Maximum color value
        rows, cols = int(dimensions[0]), int(dimensions[1])

        pixel_values = [] # Accumulate all pixel RGB values
        for line in file: # Read each line of pixel data
            pixel_values.extend([int(n) for n in line.strip().split()])
        
        
        # Organize pixel values into a 3D list [row][col][RGB]
        image_data = [[[0, 0, 0] for _ in range(cols)] for _ in range(rows)]
        index = 0
        for row in range(rows):
            for col in range(cols):
                image_data[row][col] = pixel_values[index:index+3]
                index += 3

    return ["P3", f"{rows} {cols}", max_val], image_data


# Writes image data and header to a PPM file
def write_ppm(header, image_data, output_file):
    with open(output_file, 'w') as file:
        # Write the header
        file.write(f"{header[0]}\n{header[1]}\n{header[2]}\n")
       # Write the pixel data
        for row in image_data: 
            for pixel in row:
                file.write(f"{pixel[0]} {pixel[1]} {pixel[2]}\n")

# Applies a given effect function to the image data
def apply_effect(effect_function, image_data):
    return effect_function(image_data)


# Converts the image to greyscale
def convert_to_greyscale(image_data):
    for row in image_data:
        for pixel in row:
            avg = sum(pixel) // 3 # Average of R, G, B values
            for i in range(3): # Apply average to each color component
                pixel[i] = avg
    return image_data


# Flips the image horizontally
def flip_horizontally(image_data):
    for row in image_data: # Reverse each row to flip horizontally
        start, end = 0, len(row) - 1
        while start < end:
            row[start], row[end] = row[end], row[start]
            start, end = start + 1, end - 1
    return image_data

# Sets the specific color component to its negative
def negative_of_color(image_data, color_index):
    for row in image_data:
        for pixel in row:
            pixel[color_index] = 255 - pixel[color_index] # Invert color
    return image_data

# Retains only the specified color component in each pixel
def just_the_color(image_data, color_index):
    for row in image_data:
        for pixel in row:
            for i in range(3):
                if i != color_index: # Zero out all but the specified color
                    pixel[i] = 0
    return image_data

# Flattens the specified color component by setting it to 0
def flatten_red(image_data):
    for row in image_data:
        for pixel in row:
            pixel[0] = 0  # Set red value to 0
    return image_data

def flatten_green(image_data):
    for row in image_data:
        for pixel in row:
            pixel[1] = 0  # Set green value to 0
    return image_data

def flatten_blue(image_data):
    for row in image_data:
        for pixel in row:
            pixel[2] = 0  # Set blue value to 0
    return image_data


#Bonus function

# Applies extreme contrast effect
def extreme_contrast(image_data):
    for row in image_data:
        for pixel in row:
            for i in range(3):
                # Set to 0 or 255 based on midpoint comparison
                pixel[i] = 255 if pixel[i] > 127 else 0
    return image_data


# Display available effects
def apply_effect(image_data, choice):
    
    if choice == '1':
        return convert_to_greyscale(image_data)
    elif choice == '2':
        return flip_horizontally(image_data)
    elif choice == '3':
        return negative_of_color(image_data, 0)  # Red
    elif choice == '4':
        return negative_of_color(image_data, 1)  # Green
    elif choice == '5':
        return negative_of_color(image_data, 2)  # Blue
    elif choice == '6':
        return just_the_color(image_data, 0)  # Just Red
    elif choice == '7':
        return just_the_color(image_data, 1)  # Just Green
    elif choice == '8':
        return just_the_color(image_data, 2)  # Just Blue
    elif choice == '9':
        return flatten_red(image_data)
    elif choice == '10':
        return flatten_green(image_data)
    elif choice == '11':
        return flatten_blue(image_data)
    elif choice == '12':
        return extreme_contrast(image_data)

    return image_data

# Main function to run the PPM image editor
def main():
    
    print("Portable Pixmap (PPM) Image Editor")
    input_file = input("Enter name of image file: ")
    output_file = input("Enter name of output file: ")


    # List each effect option
    continue_operations = 'y'
    while continue_operations.lower() == 'y':
        print("Here are your choices:")
        print("[0] exit")
        print("[1] convert to greyscale")
        print("[2] flip horizontally")
        print("[3] negative of red")
        print("[4] negative of green")
        print("[5] negative of blue")
        print("[6] just the reds")
        print("[7] just the greens")
        print("[8] just the blues")
        print("[9] flatten reds")
        print("[10] flatten greens")
        print("[11] flatten blues")
        print("[12] extreme contrast")


    
    
        # User selects effect
        choice = input("Enter choice: ")

        if choice == '0':
            break
        

        


        header, image_data = read_ppm(input_file)
        # Apply selected effect
        image_data = apply_effect(image_data, choice)
        write_ppm(header, image_data, output_file)
        print(f"{output_file} created with effect.")


        # Option to continue with more operations
        continue_operations = input("Do you want to do more operations (y or n): ")
        if continue_operations.lower() == 'y':
            change_input = input("Do you want to change input file (y or n): ")
            if change_input.lower() == 'y':
                input_file = input("Enter name of image file: ")
            change_output = input("Do you want to change output file (y or n): ")
            if change_output.lower() == 'y':
                output_file = input("Enter name of output file: ")

if __name__ == "__main__":
    main()
