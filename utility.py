import cv2


def color_profiles(n):
    """returns color profile based on the passed parameter.

    Args:
        n (Integer): return color profile based on assigned Integer

    Returns:
        name: color profile name
        hsv_lower: lower bound color value
        hsv_upper: upper bound color value
    """
    if n == 0:
        name = "Pepsi"
        hsv_lower = (95, 100, 100)
        hsv_upper = (115, 255, 255)
        return (name, hsv_lower, hsv_upper)
    if n == 1:
        name = "Coke"
        hsv_lower = (0, 100, 100)
        hsv_upper = (10, 255, 255)
        return (name, hsv_lower, hsv_upper)


def draw_detection_ui(biggest, frame, name):
    """draws a rect using the countours

    Args:
        biggest (array): the countours
        frame (array): the rgb image
        name (String): name of color profile being checked
    """

    rect = cv2.boundingRect(biggest)
    x, y, w, h = rect
    cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 255), 2)
    cv2.putText(frame, name, (x, y),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
