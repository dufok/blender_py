from math import log

def kelvin_to_rgb_normalized(kelvin):
    temp = kelvin / 100.0
    red, green, blue = 255, 255, 255

    # Calculate Red
    if temp <= 66:
        red = 255
    else:
        red = temp - 60
        red = 329.698727446 * (red ** -0.1332047592)
        red = min(max(red, 0), 255)

    # Calculate Green
    if temp <= 66:
        green = temp
        green = 99.4708025861 * log(green) - 161.1195681661
    else:
        green = temp - 60
        green = 288.1221695283 * (green ** -0.0755148492)
    green = min(max(green, 0), 255)

    # Calculate Blue
    if temp >= 66:
        blue = 255
    elif temp <= 19:
        blue = 0
    else:
        blue = temp - 10
        blue = 138.5177312231 * log(blue) - 305.0447927307
        blue = min(max(blue, 0), 255)

    # Normalize the values to 0-1
    red_normalized = round(red / 255.0, 3)
    green_normalized = round(green / 255.0, 3)
    blue_normalized = round(blue / 255.0, 3)

    return red_normalized, green_normalized, blue_normalized

# Example usage
kelvin = 3200

rgb_normalized = kelvin_to_rgb_normalized(kelvin)
print(rgb_normalized)

