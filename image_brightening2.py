import cv2 as cv
import argparse



def BrightnessContrast(brightness=0):
    
    # getTrackbarPos returns the current
    # position of the specified trackbar.
    brightness = cv.getTrackbarPos('Brightness',
                                    'Original Image')
     
    contrast = cv.getTrackbarPos('Contrast',
                                  'Original Image')
 
    editted_image = controller(img, brightness,
                        contrast)
 
    # The function imshow displays an image
    # in the specified window
    cv.imshow('Editted Image', editted_image)
 
def controller(img, brightness=255,
               contrast=127):
   
    brightness = int((brightness - 0) * (255 - (-255)) / (510 - 0) + (-255))
 
    contrast = int((contrast - 0) * (127 - (-127)) / (254 - 0) + (-127))
 
    if brightness != 0:
 
        if brightness > 0:
 
            shadow = brightness
 
            max = 255
 
        # else:
 
        #     shadow = 0
        #     max = 255 + brightness
 
        alpha = (max - shadow) / 255
        gamma = shadow
 
        # The function addWeighted calculates
        # the weighted sum of two arrays
        cal = cv.addWeighted(img, alpha,
                              img, 0, gamma)
 
    else:
        cal = img
 
    if contrast != 0:
        Alpha = float(131 * (contrast + 127)) / (127 * (131 - contrast))
        Gamma = 127 * (1 - Alpha)
 
        # The function addWeighted calculates
        # the weighted sum of two arrays
        cal = cv.addWeighted(cal, Alpha,
                              cal, 0, Gamma)
 
    # putText renders the specified text string in the image.
    # cv.putText(cal, 'B:{},C:{}'.format(brightness,
    #                                     contrast), (10, 30),
    #             cv.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
 
    return cal

if __name__ == '__main__':

    # The function imread loads an image
    # from the specified file and returns it.
    parser = argparse.ArgumentParser(description='Code for Changing the contrast and brightness of an image! tutorial.')
    parser.add_argument('--image', help='Path to input image.', default='lena.jpg')
    args = parser.parse_args()

    original = cv.imread(cv.samples.findFile(args.image))
 
    # Making another copy of an image.
    img = original.copy()
 
    # The function namedWindow creates a
    # window that can be used as a placeholder
    # for images.
 
    # The function imshow displays an
    # image in the specified window.
    cv.imshow('Original Image', original)
 
    # createTrackbar(trackbarName,
    # windowName, value, count, onChange)
     # Brightness range -255 to 255
    cv.createTrackbar('Brightness',
                       'Original Image', 255, 2 * 255,
                       BrightnessContrast)
     
    # Contrast range -127 to 127
    cv.createTrackbar('Contrast', 'Original Image',
                       127, 2 * 127,
                       BrightnessContrast) 
 
     
    BrightnessContrast(0)
 
# The function waitKey waits for
# a key event infinitely  or for delay
# milliseconds, when it is positive.
cv.waitKey(0)





