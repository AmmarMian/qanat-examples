# ========================================
# FileName: utils.py
# Date: 25 mai 2023 - 11:06
# Author: Ammar Mian
# Email: ammar.mian@univ-smb.fr
# GitHub: https://github.com/ammarmian
# Brief: Utils functions
# =========================================

import numpy as np


def format_covariance_latex(cov: np.ndarray) -> str:
    """Format 2D covariance matrix for LaTeX rendering.

    Args:
        cov (np.ndarray): Covariance matrix

    Returns:
        str: Formatted covariance matrix
    """
    return r'\left[\begin{array}{cc} ' + \
        str(cov[0, 0]) + r' & ' + str(cov[0, 1]) + r'\\' + \
        str(cov[1, 0]) + r' & ' + str(cov[1, 1]) + r'\end{array}\right]'


def tikzplotlib_fix_ncols(obj):
    """
    workaround for matplotlib 3.6 renamed legend's _ncol to _ncols,
    which breaks tikzplotlib.

    Obtained from:
    https://stackoverflow.com/questions/75900239/attributeerror-occurs-with-tikzplotlib-when-legend-is-plotted
    Accessed: 25 mai 2023 - 11:06

    Args:
        obj: matplotlib object
    """
    if hasattr(obj, "_ncols"):
        obj._ncol = obj._ncols
    for child in obj.get_children():
        tikzplotlib_fix_ncols(child)
