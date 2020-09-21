""" array_mods.

Description
"""

__author__ = "Your Name"
__license__ = "GPL"
__version__ = "1.0.1"
__email__ = "your.address@education.nsw.com.au"
__status__ = "Prototype, Development or Production"
""" revision notes:


"""


def loadArray(inArray):
    """Appends new data to an existing array.

    creates a copy of the input array then prompts the user
    to enter data which is appended to the new array

    Args:
        inArray: the array to which the data will be added

    Returns:
        outArray: the modified array

    Challenge:
        Ensure that the new data is of the same type as the existing data
    """
    outArray = inArray[:]  # this creates a copy of inArray
    return outArray
    print("loadArray run as a stub - array not modified")


def printArrayContents(thisArray):
    """prints the contents of an array.

    Prints the contents of the input array one element per line

    Args:
        thisArray: the array to be printed.

    Returns:
        None
    """
    i = 0  #indices in python start at 0
    print("printArrayContents run as a stub")


def sumArrayContents(thisArray):
    """Sums the contents of an array.

    add up the values of all elements in a numerical
    array and return the total

    Args:
        thisarray: the array which you want to sum the contents of.

    Returns:
        total: sum of the array.

    Challenge:
        Include error checking to ensure that all members open
        the array are numbers.
    """
    return None
    print("sumArrayContents run as a stub")


def FindMax(inArray):
    """Finds the maximum value in an array

    Args:
        inArray: the array to find the max value in

    Returns:
        maxArray: an array of the max value and the index of the max value

    Challenge:
        Include error checking to ensure that all members open
        the array are numbers.
    """
    return [None, None]
    print("FindMax run as a stub")


def FindMin(inArray):
    """Finds the minimum value in an array

    Args:
        inArray: the array to find the min value in

    Returns:
        minArray: an array of the min value and the index of the min value

    Challenge:
        Include error checking to ensure that all members open
        the array are numbers.
    """
    return [None, None]
    print("FindMin run as a stub")


def LinearSearch(inArray, target):
    """Performs a linear search.

    accepts a target value and checks every element of the array
    to be searched in turn, until either a match is found or
    the end of the array is reached.

    Args:
        inArray: the array to find the max value in
        target: the value to be found

    Returns:
        targetIndex: the index for the target or None if not found
    """
    print("LinearSearch run as a stub")


def BinarySearch(inArray, target):
    """Performs a binary search.

    divides the data set into two parts and determines
    in which part the element is to be found. That part
    of the array is again divided into two parts and a
    further decision is made as to which part may
    contain the target value. The process is continued
    until either the value is found or there are no
    more elements in the data set to be checked.

    Args:
        inArray: the array to find the max value in
        target: the value to be found

    Returns:
        targetIndex: the index for the target or None if not found
    """
    print("BinarySearch run as a stub")


def BubbleSort(inArray):
    """Performs a bubble sort.

    creates a copy of the input array then sorts the new
    array using a bubble sort.
    
    the elements of the array are compared in pairs and swapped
    if necessary. In this way, the larger of the
    pair ‘bubbles’ towards one end of the array.
    After each pass one more element will have
    moved to its correct position in the array.

    Args:
        inArray: the array to be sorted

    Returns:
        sortedArray: a copy of the array that has been sorted

    Challenge:
        Include error checking to ensure that all members open
        the array are numbers.
    """
    print("BubbleSort run as a stub")


def SelectionSort(inArray):
    """Performs a selection sort.

    creates a copy of the input array then sorts the new
    array using a selection sort.

    logically divide the array into two parts
    – an unsorted part and a sorted part.
    Each pass through the unsorted part finds
    the largest value and places it at the
    start of the sorted part. Initially the
    sorted part is empty. The size of the
    sorted part of the array increases by
    1 with each pass.

    Args:
        inArray: the array to be sorted

    Returns:
        sortedArray: a copy of the array that has been sorted
    """
    print("SelectionSort run as a stub")


def InsertionSort(inArray):
    """Performs an insertion sort.

    creates a copy of the input array then sorts the new
    array using an insertion sort.

    logically divide the array into two parts
    – an unsorted part and a sorted part.
    Each pass through the unsorted part takes
    the end value of the unsorted part and
    places it in the correct position. It
    achieves this by successively moving
    the correct number of elements in the
    sorted part by one position to make room.
    Initially the sorted part contains one element.
    The size of the sorted part of the array
    increases by 1 with each pass.

    Args:
        inArray: the array to be sorted

    Returns:
        sortedArray: a copy of the array that has been sorted
    """
    print("InsertionSort run as a stub")


def InsertElement(inArray, newElement):
    """Inserts an element into the correct position of a sorted array.

    creates a copy of the input array then inserts a new name into its correct position in an existing array, which is already in ascending order.

    Args:
        inArray: the array to be sorted

    Returns:
        editedArray: a copy of the array that has the
        element inserted in the correct position
    """
    print("InsertElement run as a stub")
