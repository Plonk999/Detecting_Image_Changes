from PIL import Image, ImageChops

def detect_differences(image1_path, image2_path, output_path):
    image1 = Image.open(image1_path).convert("L")  
    image2 = Image.open(image2_path).convert("L")  

    diff = ImageChops.difference(image1, image2)

    threshold = 50
    diff = diff.point(lambda p: p > threshold and 255)

    diff.save(output_path)

    diff.show()

if __name__ == "__main__":

    try:
        image1_path = input("Enter initial image path here: ")
        image2_path = input("Enter final image path here: ")

  
    except FileNotFoundError:
        print("No such file directory. Enter a valid file path.")
        

    output_path = r"D:\difference_image.png"

    detect_differences(image1_path, image2_path, output_path)
