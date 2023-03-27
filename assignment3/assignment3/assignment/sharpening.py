from . import filters


def unsharp_masking(img, gain, sigma):
    '''Sharpen an image via unsharp masking.

    Parameters
    ----------
    img : numpy.ndarray
        input image
    gain : float
        strength of the sharpening
    sigma : float
        the width of the Gaussian blur kernel

    Returns
    -------
    numpy.ndarray
        the sharpened image

    Raises
    ------
    ValueError
        if the gain is negative
    '''
    raise NotImplementedError('Implement this function/method.')


def laplacian(img, gain):
    '''Sharpen an image via Laplacian sharpening.

    Parameters
    ----------
    img : numpy.ndarray
        input image
    gain : float
        strength of the sharpening

    Returns
    -------
    numpy.ndarray
        the sharpened image

    Raises
    ------
    ValueError
        if the gain is negative
    '''
    raise NotImplementedError('Implement this function/method.')
