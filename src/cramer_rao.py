# ========================================
# FileName: cramer_rao.py
# Date: 26 mai 2023 - 16:32
# Author: Ammar Mian
# Email: ammar.mian@univ-smb.fr
# GitHub: https://github.com/ammarmian
# Brief: Cramer-Rao lower bound functions
# =========================================

import numpy as np
from statsmodels.tsa.tsatools import (
        duplication_matrix
)


def crb_centered_multivariate_gaussian(
        cov: np.ndarray, n_samples: int) -> np.ndarray:
    """Compute Cramer-Rao lower bound for centered multivariate Gaussian.

    Args:
        cov (np.ndarray): Covariance matrix of the centered multivariate
        n_samples (int): Number of samples

    Returns:
        np.ndarray: Cramer-Rao lower bound matrix
    """

    icov = np.linalg.inv(cov)

    return np.linalg.inv(
            n_samples * duplication_matrix(n_samples).T @
            np.kron(icov, icov) @ duplication_matrix(n_samples)
        )
