import numpy as np
from scipy import ndimage


def _convolve(img, kernel):
    '''Convenience method around ndimage.convolve.

    This calls ndimage.convolve with the boundary setting set to 'nearest'.  It
    also performs some checks on the input image.

    Parameters
    ----------
    img : numpy.ndarray
        input image
    kernel : numpy.ndarray
        filter kernel

    Returns
    -------
    numpy.ndarray
        filter image

    Raises
    ------
    ValueError
        if the image is not greyscale
    TypeError
        if the image or filter kernel are not a floating point type
    '''
    if img.ndim != 2:
        raise ValueError('Only greyscale images are supported.')

    if img.dtype != np.float32 and img.dtype != np.float64:
        raise TypeError('Image must be floating point.')

    if kernel.dtype != np.float32 and img.dtype != np.float64:
        raise TypeError('Filter kernel must be floating point.')

    return ndimage.convolve(img, kernel, mode='nearest')


def moving_average(img, width):
    '''Filter an image using a moving-average ("box") filter.

    A box filter is the average of all pixel values within an NxN neighbourhood.
    The filter is implemented as a two-pass, separable kernel.

    Parameters
    ----------
    img : numpy.ndarray
        input image
    width : int
        width of the filter kernel, i.e. 'N'; must be positive and an odd-valued

    Returns
    -------
    numpy.ndarray
        filtered image

    Raises
    ------
    ValueError
        if the width is even, zero or negative
    '''
    raise NotImplementedError('Implement this function/method.')


def gaussian(img, sigma):
    '''Filter an image using a Gaussian kernel.

    The Gaussian is implemented internally as a two-pass, separable kernel.

    Note
    ----
    The kernel is scaled to ensure that its values all sum up to '1'.  The
    slight truncation means that the filter values may not actually sum up to
    one.  The normalization ensures that this is consistent with the other
    low-pass filters in this assignment.

    Parameters
    ----------
    img : numpy.ndarray
        a greyscale image
    sigma : float
        the width of the Gaussian kernel; must be a positive, non-zero value

    Returns
    -------
    numpy.ndarray
        the Gaussian blurred image; the output will have the same type as the
        input

    Raises
    ------
    ValueError
        if the value of sigma is negative
    '''
    raise NotImplementedError('Implement this function/method.')


def laplacian(img):
    '''Filter an image using a Laplacian kernel.

    The Laplacian kernel used by this function is::

        [  0 -1  0 ]
        [ -1  4 -1 ]
        [  0 -1  0 ]

    Parameters
    ----------
    img : numpy.ndarray
        a greyscale image

    Returns
    -------
    numpy.ndarray
        the image after convolving with the Laplacian kernel
    '''
    raise NotImplementedError('Implement this function/method.')
