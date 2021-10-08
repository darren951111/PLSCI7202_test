"""
Unit Test for Assignment A2

This module implements several test cases for a2.  It is incomplete.  You should look
though this file for places to add tests.

Jiaqi Xia (jx338)
11/21/21
"""
import introcs
import a2

def test_complement():
    """
    Test function complement
    """
    introcs.assert_equals(introcs.RGB(255-250, 255-0, 255-71),
                          a2.complement_rgb(introcs.RGB(250, 0, 71)))
    introcs.assert_equals(introcs.RGB(255-92, 255-128, 255-255),
                          a2.complement_rgb(introcs.RGB(92, 128, 255)))

    # Make sure we are not modifying the color
    rgb = introcs.RGB(128,128,128)
    introcs.assert_not_equals(id(rgb),id(a2.complement_rgb(rgb)))


def test_round():
    """
    Test function round (a2 version)
    """
    introcs.assert_equals(130.6,   a2.round(130.59,1))
    introcs.assert_equals(130.5,   a2.round(130.54,1))
    introcs.assert_equals(100.0,   a2.round(100,1))
    introcs.assert_equals(100.6,   a2.round(100.55,1))
    introcs.assert_equals(99.57,   a2.round(99.566,2))
    introcs.assert_equals(99.99,   a2.round(99.99,2))
    introcs.assert_equals(100.00,  a2.round(99.995,2))
    introcs.assert_equals(22.00,   a2.round(21.99575,2))
    introcs.assert_equals(21.99,   a2.round(21.994,2))
    introcs.assert_equals(10.01,   a2.round(10.013567,2))
    introcs.assert_equals(10.00,   a2.round(10.000000005,2))
    introcs.assert_equals(10.00,   a2.round(9.9999,3))
    introcs.assert_equals(9.999,   a2.round(9.9993,3))
    introcs.assert_equals(1.355,   a2.round(1.3546,3))
    introcs.assert_equals(1.354,   a2.round(1.3544,3))
    introcs.assert_equals(0.046,   a2.round(.0456,3))
    introcs.assert_equals(0.045,   a2.round(.0453,3))
    introcs.assert_equals(0.006,   a2.round(.0056,3))
    introcs.assert_equals(0.001,   a2.round(.0013,3))
    introcs.assert_equals(0.000,   a2.round(.0004,3))
    introcs.assert_equals(0.001,   a2.round(.0009999,3))


def test_str5():
    """
    Test function str5
    """
    introcs.assert_equals('130.6',  a2.str5(130.59))
    introcs.assert_equals('130.5',  a2.str5(130.54))
    introcs.assert_equals('100.0',  a2.str5(100))
    introcs.assert_equals('100.6',  a2.str5(100.55))
    introcs.assert_equals('99.57',  a2.str5(99.566))
    introcs.assert_equals('99.99',  a2.str5(99.99))
    introcs.assert_equals('100.0',  a2.str5(99.995))
    introcs.assert_equals('22.00',  a2.str5(21.99575))
    introcs.assert_equals('21.99',  a2.str5(21.994))
    introcs.assert_equals('10.01',  a2.str5(10.013567))
    introcs.assert_equals('10.00',  a2.str5(10.000000005))
    introcs.assert_equals('10.00',  a2.str5(9.9999))
    introcs.assert_equals('9.999',  a2.str5(9.9993))
    introcs.assert_equals('1.355',  a2.str5(1.3546))
    introcs.assert_equals('1.354',  a2.str5(1.3544))
    introcs.assert_equals('0.046',  a2.str5(.0456))
    introcs.assert_equals('0.045',  a2.str5(.0453))
    introcs.assert_equals('0.006',  a2.str5(.0056))
    introcs.assert_equals('0.001',  a2.str5(.0013))
    introcs.assert_equals('0.000',  a2.str5(.0004))
    introcs.assert_equals('0.001',  a2.str5(.0009999))


def test_str5_color():
    """
    Test the str5 functions for cmyk and hsv.
    """
    # Tests for str5_cmyk
    introcs.assert_equals('(98.45, 25.36, 72.80, 1.000)',
                              a2.str5_cmyk(introcs.CMYK(98.448, 25.362, 72.8, 1.0)))

    # Tests for str5_cmyk
    introcs.assert_equals('(23.49, 37.98, 1.000, 0.993)',
                              a2.str5_cmyk(introcs.CMYK(23.48573, 37.984457, 0.9999, 0.99345)))

    # Tests for str5_hsv
    introcs.assert_equals('(0.000, 0.314, 1.000)',
                              a2.str5_hsv(introcs.HSV(0.0,0.313725490196,1.0)))

    # Tests for str5_hsv
    introcs.assert_equals('(60.00, 0.000, 1.000)',
                              a2.str5_hsv(introcs.HSV(60, 0, 0.9999999)))

def test_rgb_to_cmyk():
    """
    Test translation function rgb_to_cmyk
    """
    rgb = introcs.RGB(255, 255, 255)
    cmyk = a2.rgb_to_cmyk(rgb)
    # Test cyan of CMYK
    introcs.assert_equals('0.000', a2.str5(cmyk.cyan))
    # Test magenta of CMYK
    introcs.assert_equals('0.000', a2.str5(cmyk.magenta))
    # Test yellow of CMYK
    introcs.assert_equals('0.000', a2.str5(cmyk.yellow))
    # Test black of CMYK
    introcs.assert_equals('0.000', a2.str5(cmyk.black))

    rgb = introcs.RGB(0, 0, 0)
    cmyk = a2.rgb_to_cmyk(rgb)
    # Test cyan of CMYK
    introcs.assert_equals('0.000', a2.str5(cmyk.cyan))
    # Test magenta of CMYK
    introcs.assert_equals('0.000', a2.str5(cmyk.magenta))
    # Test yellow of CMYK
    introcs.assert_equals('0.000', a2.str5(cmyk.yellow))
    # Test black of CMYK
    introcs.assert_equals('100.0', a2.str5(cmyk.black))

    rgb = introcs.RGB(217, 43, 164)
    cmyk = a2.rgb_to_cmyk(rgb)
    # Test cyan of CMYK
    introcs.assert_equals('0.000', a2.str5(cmyk.cyan))
    # Test magenta of CMYK
    introcs.assert_equals('80.18', a2.str5(cmyk.magenta))
    # Test yellow of CMYK
    introcs.assert_equals('24.42', a2.str5(cmyk.yellow))
    # Test black of CMYK
    introcs.assert_equals('14.90', a2.str5(cmyk.black))

    rgb = introcs.RGB(100, 100, 100)
    cmyk = a2.rgb_to_cmyk(rgb)
    # Test cyan of CMYK
    introcs.assert_equals('0.000', a2.str5(cmyk.cyan))
    # Test magenta of CMYK
    introcs.assert_equals('0.000', a2.str5(cmyk.magenta))
    # Test yellow of CMYK
    introcs.assert_equals('0.000', a2.str5(cmyk.yellow))
    # Test black of CMYK
    introcs.assert_equals('60.78', a2.str5(cmyk.black))

    rgb = introcs.RGB(123, 234, 132)
    cmyk = a2.rgb_to_cmyk(rgb)
    # Test cyan of CMYK
    introcs.assert_equals('47.44', a2.str5(cmyk.cyan))
    # Test magenta of CMYK
    introcs.assert_equals('0.000', a2.str5(cmyk.magenta))
    # Test yellow of CMYK
    introcs.assert_equals('43.59', a2.str5(cmyk.yellow))
    # Test black of CMYK
    introcs.assert_equals('8.235', a2.str5(cmyk.black))

    rgb = introcs.RGB(100, 0, 100)
    cmyk = a2.rgb_to_cmyk(rgb)
    # Test cyan of CMYK
    introcs.assert_equals('0.000', a2.str5(cmyk.cyan))
    # Test magenta of CMYK
    introcs.assert_equals('100.0', a2.str5(cmyk.magenta))
    # Test yellow of CMYK
    introcs.assert_equals('0.000', a2.str5(cmyk.yellow))
    # Test black of CMYK
    introcs.assert_equals('60.78', a2.str5(cmyk.black))


def test_cmyk_to_rgb():
    """
    Test translation function cmyk_to_rgb
    """
    cmyk = introcs.CMYK(10.0, 20.0, 30.0, 40.0)
    rgb = a2.cmyk_to_rgb(cmyk)
    # Test red of RGB
    introcs.assert_equals(138, rgb.red)
    # Test green of RGB
    introcs.assert_equals(122, rgb.green)
    # Test blue of RGB
    introcs.assert_equals(107, rgb.blue)

    cmyk = introcs.CMYK(0.0, 0.0, 0.0, 0.0)
    rgb = a2.cmyk_to_rgb(cmyk)
    # Test red of RGB
    introcs.assert_equals(255, rgb.red)
    # Test green of RGB
    introcs.assert_equals(255, rgb.green)
    # Test blue of RGB
    introcs.assert_equals(255, rgb.blue)

    cmyk = introcs.CMYK(100.0, 100.0, 100.0, 0.0)
    rgb = a2.cmyk_to_rgb(cmyk)
    # Test red of RGB
    introcs.assert_equals(0, rgb.red)
    # Test green of RGB
    introcs.assert_equals(0, rgb.green)
    # Test blue of RGB
    introcs.assert_equals(0, rgb.blue)

    cmyk = introcs.CMYK(0.0, 0.0, 0.0, 100.0)
    rgb = a2.cmyk_to_rgb(cmyk)
    # Test red of RGB
    introcs.assert_equals(0, rgb.red)
    # Test green of RGB
    introcs.assert_equals(0, rgb.green)
    # Test blue of RGB
    introcs.assert_equals(0, rgb.blue)


def test_rgb_to_hsv():
    """
    Test translation function rgb_to_hsv
    """
    # MAX = MIN
    rgb = introcs.RGB(0, 0, 0)
    hsv = a2.rgb_to_hsv(rgb)
    # Test hue of HSV
    introcs.assert_equals('0.000', a2.str5(hsv.hue))
    # Test saturation of HSV
    introcs.assert_equals('0.000', a2.str5(hsv.saturation))
    # Test value of HSV
    introcs.assert_equals('0.000', a2.str5(hsv.value))

    # MAX = R and G >= B
    rgb = introcs.RGB(200, 100, 50)
    hsv = a2.rgb_to_hsv(rgb)
    # Test hue of HSV
    introcs.assert_equals('20.00', a2.str5(hsv.hue))
    # Test saturation of HSV
    introcs.assert_equals('0.750', a2.str5(hsv.saturation))
    # Test value of HSV
    introcs.assert_equals('0.784', a2.str5(hsv.value))

    # MAX = R and G < B
    rgb = introcs.RGB(200, 50, 100)
    hsv = a2.rgb_to_hsv(rgb)
    # Test hue of HSV
    introcs.assert_equals('340.0', a2.str5(hsv.hue))
    # Test saturation of HSV
    introcs.assert_equals('0.750', a2.str5(hsv.saturation))
    # Test value of HSV
    introcs.assert_equals('0.784', a2.str5(hsv.value))

    # MAX = G
    rgb = introcs.RGB(50, 200, 100)
    hsv = a2.rgb_to_hsv(rgb)
    # Test hue of HSV
    introcs.assert_equals('140.0', a2.str5(hsv.hue))
    # Test saturation of HSV
    introcs.assert_equals('0.750', a2.str5(hsv.saturation))
    # Test value of HSV
    introcs.assert_equals('0.784', a2.str5(hsv.value))

    # MAX = B
    rgb = introcs.RGB(100, 100, 200)
    hsv = a2.rgb_to_hsv(rgb)
    # Test hue of HSV
    introcs.assert_equals('240.0', a2.str5(hsv.hue))
    # Test saturation of HSV
    introcs.assert_equals('0.500', a2.str5(hsv.saturation))
    # Test value of HSV
    introcs.assert_equals('0.784', a2.str5(hsv.value))

    # MAX = MIN
    rgb = introcs.RGB(255, 255, 255)
    hsv = a2.rgb_to_hsv(rgb)
    # Test hue of HSV
    introcs.assert_equals('0.000', a2.str5(hsv.hue))
    # Test saturation of HSV
    introcs.assert_equals('0.000', a2.str5(hsv.saturation))
    # Test value of HSV
    introcs.assert_equals('1.000', a2.str5(hsv.value))


def test_hsv_to_rgb():
    """
    Test translation function hsv_to_rgb
    """
    # Hi = 0
    hsv = introcs.HSV(30.0, 0.1, 0.9)
    rgb = a2.hsv_to_rgb(hsv)
    # Test red of RGB
    introcs.assert_equals(230, rgb.red)
    # Test green of RGB
    introcs.assert_equals(218, rgb.green)
    # Test blue of RGB
    introcs.assert_equals(207, rgb.blue)

    # Hi = 1
    hsv = introcs.HSV(61.0, 1.0, 1.0)
    rgb = a2.hsv_to_rgb(hsv)
    # Test red of RGB
    introcs.assert_equals(251, rgb.red)
    # Test green of RGB
    introcs.assert_equals(255, rgb.green)
    # Test blue of RGB
    introcs.assert_equals(0, rgb.blue)

    # Hi = 2
    hsv = introcs.HSV(150, 0.7, 0.7)
    rgb = a2.hsv_to_rgb(hsv)
    # Test red of RGB
    introcs.assert_equals(54, rgb.red)
    # Test green of RGB
    introcs.assert_equals(179, rgb.green)
    # Test blue of RGB
    introcs.assert_equals(116, rgb.blue)

    # Hi = 3
    hsv = introcs.HSV(200, 0.123, 0.456)
    rgb = a2.hsv_to_rgb(hsv)
    # Test red of RGB
    introcs.assert_equals(102, rgb.red)
    # Test green of RGB
    introcs.assert_equals(112, rgb.green)
    # Test blue of RGB
    introcs.assert_equals(116, rgb.blue)

    # Hi = 4
    hsv = introcs.HSV(250, 0.5, 0.5)
    rgb = a2.hsv_to_rgb(hsv)
    # Test red of RGB
    introcs.assert_equals(74, rgb.red)
    # Test green of RGB
    introcs.assert_equals(64, rgb.green)
    # Test blue of RGB
    introcs.assert_equals(128, rgb.blue)

    # Hi = 5
    hsv = introcs.HSV(310.0, 0.3, 0.4)
    rgb = a2.hsv_to_rgb(hsv)
    # Test red of RGB
    introcs.assert_equals(102, rgb.red)
    # Test green of RGB
    introcs.assert_equals(71, rgb.green)
    # Test blue of RGB
    introcs.assert_equals(97, rgb.blue)


def test_to_float_list():
    """
    Test conversion function to_float_list
    """
    seq = ['1.0', '2.2', '3.5']
    lst = a2.to_float_list(seq)
    # Test the first element of the list
    introcs.assert_floats_equal(1.0, lst[0])
    # Test the second element of the list
    introcs.assert_floats_equal(2.2, lst[1])
    # Test the third element of the list
    introcs.assert_floats_equal(3.5, lst[2])

    seq = ['2.2', '3.5']
    lst = a2.to_float_list(seq)
    # Test the first element of the list
    introcs.assert_floats_equal(2.2, lst[0])
    # Test the second element of the list
    introcs.assert_floats_equal(3.5, lst[1])

    seq = ['1.0', '2.2', '3.5', '-7.5']
    lst = a2.to_float_list(seq)
    # Test the first element of the list
    introcs.assert_floats_equal(1.0, lst[0])
    # Test the second element of the list
    introcs.assert_floats_equal(2.2, lst[1])
    # Test the third element of the list
    introcs.assert_floats_equal(3.5, lst[2])
    # Test the fourth element of the list
    introcs.assert_floats_equal(-7.5, lst[3])


def test_file_to_data():
    """
    Test file function file_to_data
    """
    file = 'colorblind/normal.dat'
    data = a2.file_to_data(file)
    # Test the name of the colorblindness disorder
    introcs.assert_equals('Normal',data[0])
    # Test the first row of the matrix
    introcs.assert_float_lists_equal([1,0,0],data[1])
    # Test the second row of the matrix
    introcs.assert_float_lists_equal([0,1,0],data[2])
    # Test the third row of the matrix
    introcs.assert_float_lists_equal([0,0,1],data[3])

    file = 'colorblind/tritanomaly.dat'
    data = a2.file_to_data(file)
    # Test the name of the colorblindness disorder
    introcs.assert_equals('Tritanomaly',data[0])
    # Test the first row of the matrix
    introcs.assert_float_lists_equal([0.967, 0.033, 0],data[1])
    # Test the second row of the matrix
    introcs.assert_float_lists_equal([0, 0.733, 0.267],data[2])
    # Test the third row of the matrix
    introcs.assert_float_lists_equal([0, 0.183, 0.817],data[3])


def test_files_to_dictionary():
    """
    Test loading function files_to_dictionary
    """
    files = ['colorblind/normal.dat','colorblind/tritanomaly.dat']
    maps = a2.files_to_dictionary(files)

    # Test the length of the dictionary (i.e. number if key-value pairs)
    introcs.assert_equals(2,len(maps))
    # Test whether the key 'Normal' is in the dictionary
    introcs.assert_true('Normal' in maps)
    # Test whether the key 'Tritanomaly' is in the dictionary
    introcs.assert_true('Tritanomaly' in maps)
    # Test the first element of the value of the key 'normal'
    introcs.assert_float_lists_equal([1,0,0],maps['Normal'][0])
    # Test the second element of the value of the key 'normal'
    introcs.assert_float_lists_equal([0,1,0],maps['Normal'][1])
    # Test the third element of the value of the key 'normal'
    introcs.assert_float_lists_equal([0,0,1],maps['Normal'][2])
    # Test the first element of the value of the key 'Tritanomaly'
    introcs.assert_float_lists_equal([0.967, 0.033, 0],maps['Tritanomaly'][0])
    # Test the second element of the value of the key 'Tritanomaly'
    introcs.assert_float_lists_equal([0, 0.733, 0.267],maps['Tritanomaly'][1])
    # Test the third element of the value of the key 'Tritanomaly'
    introcs.assert_float_lists_equal([0, 0.183, 0.817],maps['Tritanomaly'][2])


# Script Code
# THIS PREVENTS THE TESTS RUNNING ON IMPORT
if __name__ == '__main__':
    # Execute the tests
    test_complement()
    test_round()
    test_str5()
    test_str5_color()
    test_rgb_to_cmyk()
    test_cmyk_to_rgb()
    test_rgb_to_hsv()
    test_hsv_to_rgb()
    test_to_float_list()
    test_file_to_data()
    test_files_to_dictionary()
    print('Module a2 is working correctly')
