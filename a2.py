"""
Functions for Assignment A2

This file contains the functions for the assignment.  You should replace the stubs
with your own implementations.

Jiaqi Xia (jx338)
3/21/21
"""
import introcs
import math


def complement_rgb(rgb):
    """
    Returns: the complement of color rgb.

    Parameter rgb: the color to complement
    Precondition: rgb is an RGB object
    """
    rgb.red = 255 - rgb.red
    rgb.green = 255 - rgb.green
    rgb.blue = 255 - rgb.blue
    return introcs.RGB(rgb.red, rgb.green, rgb.blue)


def round(number, places):
    """
    Returns: the number rounded to the given number of decimal places.

    This function is more stable than the built-in round.  The built-in round
    has weird behavior where round(100.55,1) is 100.5 while round(100.45,1) is
    also 100.5.  We want to ensure that anything ending in a 5 is rounded UP.

    It is possible to write this function without the second precondition on
    places. If you want to do that, we leave that as an optional challenge.

    Parameter number: the number to round to the given decimal place
    Precondition: number is a float

    Parameter places: the decimal place to round to
    Precondition: places is an int; 0 <= places <= 3
    """
    # To get the desired output, do the following
    #   1. Shift the number "to the left" so that the position to round to is left of
    #      the decimal place.  For example, if you are rounding 100.556 to the first
    #      decimal place, the number becomes 1005.56.  If you are rounding to the second
    #      decimal place, it becomes 10055.6.  If you are rounding 100.556 to the nearest
    #      integer, it remains 100.556.
    #   2. Add 0.5 to this number
    #   3. Convert the number to an int, cutting it off to the right of the decimal.
    #   4. Shift the number back "to the right" the same amount that you did to the left.
    #      Suppose that in step 1 you converted 100.556 to 1005.56.  In this case,
    #      divide the number by 10 to put it back.
    number = number * 10 ** places
    number = number + 0.5
    number = int(number)
    number = number / 10 ** places
    return number


def str5(value):
    """
    Returns: value as a string, but expand or round to be exactly 5 characters.

    The decimal point counts as one of the five characters.

    Examples:
        str5(1.3546)  is  '1.355'.
        str5(21.9954) is  '22.00'.
        str5(21.994)  is  '21.99'.
        str5(130.59)  is  '130.6'.
        str5(130.54)  is  '130.5'.
        str5(1)       is  '1.000'.

    Parameter value: the number to convert to a 5 character string.
    Precondition: value is a number (int or float), 0 <= value <= 360.
    """
    # Note:Obviously, you want to use the function round() that you just defined.
    # However, remember that the rounding takes place at a different place depending
    # on how big value is. Look at the examples in the specification.
    value = float(value)
    strvalue = str(value)
    dotpos = introcs.index_str(strvalue, '.')
    intlength = len(strvalue[:dotpos])
    decimal = 5 - intlength - 1
    newvalue = round(value, decimal)
    result = str(newvalue) + '00000'
    result = result[:5]
    return result


def str5_cmyk(cmyk):
    """
    Returns: String representation of cmyk in the form "(C, M, Y, K)".

    In the output, each of C, M, Y, and K should be exactly 5 characters long.
    Hence the output of this function is not the same as str(cmyk)

    Example: if str(cmyk) is

          '(0.0,31.3725490196,31.3725490196,0.0)'

    then str5_cmyk(cmyk) is '(0.000, 31.37, 31.37, 0.000)'. Note the spaces after the
    commas. These must be there.

    Parameter cmtk: the color to convert to a string
    Precondition: cmyk is an CMYK object.
    """
    C = str5(cmyk.cyan)
    M = str5(cmyk.magenta)
    Y = str5(cmyk.yellow)
    K = str5(cmyk.black)
    return '(' + C + ', ' + M + ', ' + Y + ', ' + K + ')'


def str5_hsv(hsv):
    """
    Returns: String representation of hsv in the form "(H, S, V)".

    In the output, each of H, S, and V should be exactly 5 characters long.
    Hence the output of this function is not the same as str(hsv)

    Example: if str(hsv) is

          '(0.0,0.313725490196,1.0)'

    then str5_hsv(hsv) is '(0.000, 0.314, 1.000)'. Note the spaces after the
    commas. These must be there.

    Parameter hsv: the color to convert to a string
    Precondition: hsv is an HSV object.
    """
    H = str5(hsv.hue)
    S = str5(hsv.saturation)
    V = str5(hsv.value)
    return '(' + H + ', ' + S + ', ' + V + ')'


def rgb_to_cmyk(rgb):
    """
    Returns: color rgb in space CMYK, with the most black possible.

    Formulae from en.wikipedia.org/wiki/CMYK_color_model.

    Parameter rgb: the color to convert to a CMYK object
    Precondition: rgb is an RGB object
    """
    # The RGB numbers are in the range 0..255.
    # Change the RGB numbers to the range 0..1 by dividing them by 255.0.
    R = rgb.red / 255.0
    G = rgb.green / 255.0
    B = rgb.blue / 255.0
    C1 = 1 - R
    M1 = 1 - G
    Y1 = 1 - B
    if C1 == 1 and M1 == 1 and Y1 == 1:
        return introcs.CMYK(0.0, 0.0, 0.0, 100.0)
    else:
        K = min(C1, M1, Y1)
        C = (C1 - K) / (1 - K)
        M = (M1 - K) / (1 - K)
        Y = (Y1 - K) / (1 - K)
        return introcs.CMYK(C*100, M*100, Y*100, K*100)


def cmyk_to_rgb(cmyk):
    """
    Returns : color CMYK in space RGB.

    Formulae from en.wikipedia.org/wiki/CMYK_color_model.

    Parameter cmyk: the color to convert to a RGB object
    Precondition: cmyk is an CMYK object.
    """
    # The CMYK numbers are in the range 0.0..100.0.  Deal with them in the
    # same way as the RGB numbers in rgb_to_cmyk()
    C = cmyk.cyan / 100.0
    M = cmyk.magenta / 100.0
    Y = cmyk.yellow / 100.0
    K = cmyk.black / 100.0
    R = (1 - C) * (1 - K)
    G = (1 - M) * (1 - K)
    B = (1 - Y) * (1 - K)
    R = int(round(R * 255, 0))
    G = int(round(G * 255, 0))
    B = int(round(B * 255, 0))
    return introcs.RGB(R, G, B)


def rgb_to_hsv(rgb):
    """
    Return: color rgb in HSV color space.

    Formulae from wikipedia.org/wiki/HSV_color_space.

    Parameter rgb: the color to convert to a HSV object
    Precondition: rgb is an RGB object
    """
    # The RGB numbers are in the range 0..255.
    # Change them to range 0..1 by dividing them by 255.0.
    R = rgb.red / 255.0
    G = rgb.green / 255.0
    B = rgb.blue / 255.0
    MAX = max(R, G, B)
    MIN  = min(R, G, B)
    if MAX == MIN:
        H = 0
    elif MAX == R and G >= B:
        H = 60.0 * (G - B) / (MAX - MIN)
    elif MAX == R and G < B:
        H = 60.0 * (G - B) / (MAX - MIN) + 360.0
    elif MAX == G:
        H = 60.0 * (B - R) / (MAX - MIN) + 120.0
    elif MAX == B:
        H = 60.0 * (R - G) / (MAX - MIN) + 240.0
    if MAX == 0:
        S = 0
    else:
        S = 1 - MIN / MAX
    V = MAX
    return introcs.HSV(H, S, V)


def hsv_to_rgb(hsv):
    """
    Returns: color in RGB color space.

    Formulae from http://en.wikipedia.org/wiki/HSV_color_space.

    Parameter hsv: the color to convert to a RGB object
    Precondition: hsv is an HSV object.
    """
    import math
    H = hsv.hue
    S = hsv.saturation
    V = hsv.value
    Hi = math.floor(H / 60)
    f = H / 60 - Hi
    p = V * (1 - S)
    q = V * (1 - f * S)
    t = V * (1 - (1 - f) * S)
    if Hi == 0:
        R = V
        G = t
        B = p
    elif Hi == 1:
        R = q
        G = V
        B = p
    elif Hi == 2:
        R = p
        G = V
        B = t
    elif Hi == 3:
        R = p
        G = q
        B = V
    elif Hi == 4:
        R = t
        G = p
        B = V
    elif Hi == 5:
        R = V
        G = p
        B = q
    R = int(round(R * 255, 0))
    G = int(round(G * 255, 0))
    B = int(round(B * 255, 0))
    return introcs.RGB(R, G, B)


# COLOR BLIND FILE SUPPORT

def to_float_list(thelist):
    """
    Returns a copy of the old list, with all values cast to floats

    Example: to_float_list(['1', '2.2', '3.5']) returns [1.0, 2.2, 3.5]

    Parameter thelist: The list of strings to convert
    Precondition: The elements of the list can be converted to floats
    """
    mycopy = []
    for x in thelist:
        mycopy.append(float(x))
    return mycopy


def file_to_data(filename):
    """
    Returns the data for the given file name.

    The file is guaranteed to be a DAT file.  DAT files have the following format:

        SETTING
        x1, y1, z1
        x2, y2, x2
        x3, y3, z3

    where SETTING is the name of the color setting, and all of the other values are
    floats.

    The data is returned as a (sort of) two-dimensional list.
    * The list has 4 elements
    * The first element is just a string with the SETTING NAME
    * The remaining elements are lists contain the three floats for each line

    Example: Suppose the DAT file contains the following information

        Tritanomaly
        0.967, 0.033, 0
        0,     0.733, 0.267
        0,     0.183, 0.817

    Then this function returns

    ['Tritanomaly', [0.967, 0.033, 0.0], [0.0, 0.733, 0.267], [0.0, 0.183, 0.817]]

    Parameter filename: The name of the file
    Precondition: filename is the name of a DAT file
    """
    # RULE: We want you to use a for-loop to convert the last three rows to float lists
    # HINT: Use to_float_list
    mylist = []
    with open(filename, 'r') as f:
        x = f.readline().strip()
        mylist.append(x)
        x = f.readline().strip().replace(' ', '').split(',')
        mylist.append(x)
        x = f.readline().strip().replace(' ', '').split(',')
        mylist.append(x)
        x = f.readline().strip().replace(' ', '').split(',')
        mylist.append(x)
    mylist2 = []
    for x in mylist:
        if type(x) == list:
            mylist2.append(to_float_list(x))
        else:
            mylist2.append(x)
    return mylist2


def files_to_dictionary(files):
    """
    Returns the data dictionary for a list of file names.

    The contents of the list returned are the results of file_to_data on the list of
    file names.

    Example: If filenames is ['normal.dat', 'tritanomaly.dat'], this function
    returns the multi-dimensional list

    { 'Normal' : [[1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0]].
      'Tritanomaly' : [[0.967, 0.033, 0.0], [0.0, 0.733, 0.267], [0.0, 0.183, 0.817]]
    }

    Parameter files: The list of filenames
    Precondition: files is a list of names of DAT files
    """
    mydict = {}
    for x in files:
        pair = file_to_data(x)
        mydict[pair[0]] = pair[1:]
    return mydict




# PROVIDED FUNCTIONS (DO NOT TOUCH)
def components_to_num(coeffs, rgb):
    """
    Returns: the linear combination rgb's components with the given coefficients.

    The answer will be a single number.  It should be rounded to the nearest int.

    Example: If coeffs is [0.25,0.5,0.25] and rgb is (red=92,green=128,blue=255), this
    function returns

        0.25*92+0.5*128+0.25*255 = 150.75 which rounds to 151

    Parameter coeffs: The coefficient list
    Precondition: A list of three floats that sum to 1.0

    Parameter rgb: The color to apply the coefficients to
    Precondition: rgb is an RGB object
    """
    return int(round(coeffs[0]*rgb.red + coeffs[1]*rgb.green + coeffs[2]*rgb.blue,0))


def apply_matrix(matrix, rgb):
    """
    Returns: a new color object resulting from applying matrix to color rgb

    The matrix is applied as follows:
    * The coefficients in the first row are applied to the color to get the red value
    * The coefficients in the second row are applied to the color to get the green value
    * The coefficients in the third row are applied to the color to get the blue value

    Parameter matrix: The colorblind conversion matrix
    Precondition: matrix is a 3x3 matrix, which each row summing to 1.0

    Parameter rgb: the color to convert to a CMYK object
    Precondition: rgb is an RGB object
    """
    new_r = components_to_num(matrix[0], rgb)
    new_g = components_to_num(matrix[1], rgb)
    new_b = components_to_num(matrix[2], rgb)
    return introcs.RGB(new_r, new_g, new_b)
