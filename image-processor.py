import matplotlib.pyplot as plt
import numpy as np
import sys

from filters import grayscale, reflect, apply_kernel

def main():
    if len(sys.argv) != 3 or sys.argv[1] not in ['-g', '-b', '-r', '-e']:
        print("Usage: python image-processor.py <image-path> [-g, -b, r, -e]")
        return

    if sys.argv[2][-4:] in ['.png', '.jpg']:
        image = plt.imread(sys.argv[2])
    else:
        print("Not a valid image file. Accepted: png/jpg.")
        return
    
    height, width = image.shape[:-1]

    filter = sys.argv[1]

    if filter == '-g':
        image = grayscale(width, height, image)
    elif filter == '-r':
        image = reflect(width, height, image)
    elif filter == '-b':
        blur_kernel = [ [1/9, 1/9, 1/9],
                        [1/9, 1/9, 1/9],
                        [1/9, 1/9, 1/9] ]
        image = apply_kernel(width, height, image, blur_kernel)
    elif filter == '-e':
        edge_kernel = [[-1, -1, -1],
                       [-1, 8, -1],
                       [-1, -1, -1]]
        image = apply_kernel(width, height, image, edge_kernel)

    image = np.array(image)

    ax = plt.subplots(figsize=(10, 10))[1]
    ax.imshow(image)
    ax.axis('off')

    plt.show()

    image = image.astype(np.uint8)

    if sys.argv[2][-4:] == '.png':
        plt.imsave(f'output{filter}.png', image)
    else:
        plt.imsave(f'output{filter}.jpg', image)


if __name__ == '__main__':
    main()
