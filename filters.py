def grayscale(w_, h_, img):
    new_img = []
    for row in range(h_):
        new_img.append([])
        for col in range(w_):
            avg = img[row][col][0]/3 + img[row][col][1]/3 + img[row][col][2]/3
            avg = int(avg) % 256
            new_img[row].append([])
            for _ in range(3):
                new_img[row][col].append(avg)

    return new_img

def reflect(w_, h_, img):
    new_img = []
    for row in range(h_):
        new_img.append([])
        for col in range(w_):

            new_img[row].append(img[row][w_ - col - 1])
            

    return new_img

def calc_kernel(w_, h_, cp_x, cp_y, img, kernel):

    new_pixel = [0, 0, 0]

    for i in range(-1, 2):
        for j in range(-1, 2):
            ni = cp_y + i
            nj = cp_x + j
            if 0 <= ni < h_ and 0 <= nj < w_:
                for k in range(3):
                    new_pixel[k] += int(img[ni][nj][k] * kernel[i + 1][j + 1])

    for i in range(3):
        new_pixel[i] = max(min(new_pixel[i], 255), 0)
    return new_pixel
    

def apply_kernel(w_, h_, img, kernel):
    new_img = []

    for row in range(h_):
        new_img.append([])
        for col in range(w_):
            new_img[row].append(calc_kernel(w_, h_, col, row, img, kernel))
            

    return new_img