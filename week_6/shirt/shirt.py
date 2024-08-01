from PIL import Image, ImageOps
import sys
in_file = sys.argv[1]
out_file = sys.argv[2]

def is_valid_input():
    in_image = in_file.split(".")
    out_image = out_file.split(".")
    extensions = ["jpg", "jpeg", "png"]

    # if the user does not specify exactly two command-line arguments,
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    elif len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")

    # if the input’s name does not have the same extension as the output’s name.
    elif in_image[1] not in extensions:
        sys.exit("Invalid output")

    # have different extensions
    elif in_image[1] != out_image[1]:
        sys.exit("Input and output have different extensions")

    else: return True

def overlay_img():
    try:
        # open the image
        img = Image.open(in_file)
        shirt = Image.open("shirt.png")

        # crop the image
        img = ImageOps.fit(img, shirt.size)

        # overlay the image
        img.paste(shirt, mask = shirt)

        # save the image
        img.save(out_file)

    except FileNotFoundError:
        sys.exit("File not found")

def main():
    if is_valid_input():
        overlay_img()

if __name__ == "__main__":
    main()
