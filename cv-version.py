import cv2
import numpy as np
import sys

def main():
    if len(sys.argv) != 3 or sys.argv[1] not in ['-g', '-b', '-r', '-e']:
        print("Usage: python image-processor.py <image-path> [-g, -b, r, -e]")
        return

    if sys.argv[2][-4:] in ['.png', '.jpg']:
        image = cv2.imread(sys.argv[2])
    else:
        print("Not a valid image file. Accepted: png/jpg.")
        return

    filter = sys.argv[1]

    if filter == '-g':
        image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    elif filter == '-r':
        image = cv2.flip(image, 1)
    elif filter == '-b':
        blur_kernel = [ [1/9, 1/9, 1/9],
                        [1/9, 1/9, 1/9],
                        [1/9, 1/9, 1/9] ]
        image = cv2.filter2D(image, -1, np.array(blur_kernel))
    elif filter == '-e':
        edge_kernel = [[-1, -1, -1],
                       [-1, 8, -1],
                       [-1, -1, -1]]
        image = cv2.filter2D(image, -1, np.array(edge_kernel))

    image = np.array(image)

    cv2.imshow('Image', image)

    cv2.waitKey(0)

    cv2.destroyAllWindows()

    if sys.argv[2][-4:] == '.png':
        cv2.imwrite(f'cv-output{filter}.png', image)
    else:
        cv2.imwrite(f'cv-output{filter}.jpg', image)


if __name__ == '__main__':
    main()
