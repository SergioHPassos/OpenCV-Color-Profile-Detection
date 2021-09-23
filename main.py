from utility import color_profiles, draw_detection_ui
import cv2

# entry point
if __name__ == "__main__":

    # load image
    frame = cv2.imread("cola-pepsi.jpg")

    # convert image to hsv
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # loop between both color profiles
    for i in range(2):
        name, hsv_lower, hsv_upper = color_profiles(i)

        # checks the image to see if any values--
        # --falls between the lower and upper bound
        mask = cv2.inRange(hsv, hsv_lower, hsv_upper)

        # shape detection
        contours, hierarchy = cv2.findContours(
            mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

        # sort in ascending order
        biggest = sorted(contours, key=cv2.contourArea, reverse=True)[0]

        # draw ui detection
        draw_detection_ui(biggest, frame, name)

    #  display image
    cv2.imshow("Image", frame)
    # cv2.imshow("MASK", mask)

    # stops automatic closing by waiting for key press
    cv2.waitKey(0)

    # after key press than destroy
    cv2.destroyAllWindows()
