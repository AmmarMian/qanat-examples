# ========================================
# FileName: plot.py
# Date: 25 mai 2023 - 10:36
# Author: Ammar Mian
# Email: ammar.mian@univ-smb.fr
# GitHub: https://github.com/ammarmian
# Brief: Plot MSE curve and lower bound
# as a function of the number of samples.
# =========================================

import argparse
import os
import numpy as np
import pickle
import matplotlib.pyplot as plt
import tikzplotlib

import sys
file_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(file_dir, '../..'))
from src.utils import (
        tikzplotlib_fix_ncols)


# Activate LaTeX text rendering
# if available on your system
plt.rc('text', usetex=True)
plt.rc('font', family='serif')


def generate_figure(mse_location_mean,
                    mse_location_std,
                    mse_covariance_mean,
                    mse_covariance_std,
                    trias_range,
                    folder,
                    save=False):

    # Figure with location
    fig_location, ax_location = plt.subplots(1, 1, figsize=(6, 4))
    ax_location.plot(trias_range, mse_location_mean, label='Location',
                     marker='o', markersize=2, linestyle='--')
    ax_location.set_xlabel('Number of samples')
    ax_location.set_ylabel('MSE')
    ax_location.set_title(
            'MSE as a function of the number of samples: location')
    ax_location.set_xscale('log')
    ax_location.set_yscale('log')

    if save:
        plt.savefig(os.path.join(folder, 'MSE_location.pdf'),
                    bbox_inches='tight')
        tikzplotlib_fix_ncols(fig_location)
        tikzplotlib.save(os.path.join(folder, 'MSE_location.tex'))
        print('Saved location plot in {}'.format(folder))

    fig_cov, ax_cov = plt.subplots(1, 1, figsize=(6, 4))
    ax_cov.plot(trias_range, mse_covariance_mean, label='Covariance',
                marker='o', markersize=2, linestyle='--')
    ax_cov.set_xlabel('Number of samples')
    ax_cov.set_ylabel('MSE')
    ax_cov.set_title(
            'MSE as a function of the number of samples: covariance')
    ax_cov.set_xscale('log')
    ax_cov.set_yscale('log')

    if save:
        plt.savefig(os.path.join(folder, 'MSE_covariance.pdf'),
                    bbox_inches='tight')
        tikzplotlib_fix_ncols(fig_cov)
        tikzplotlib.save(os.path.join(folder, 'MSE_covariance.tex'))
        print('Saved covariance plot in {}'.format(folder))


if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument('--storage_path', type=str,
                        default='data/',
                        help='Path to the data folder where '
                        'results.pkl is located.')
    parser.add_argument('--aggregate', action='store_true', default=False,
                        help='Aggregate results from different folders')
    parser.add_argument('--save', action='store_true', default=False,
                        help='Save the plot as pdf and LaTeX code')
    args = parser.parse_args()

    # Check if subfolders with name "group_" exist
    # Which means that several parameters have been
    # estimated and stored in different folders
    if os.path.isdir(os.path.join(args.storage_path, 'group_0')):
        folders = [os.path.join(args.storage_path, f) for f in
                   os.listdir(args.storage_path) if 'group_' in f
                   and os.path.isdir(os.path.join(args.storage_path, f))]
    else:
        folders = [args.storage_path]

    # We aggregate the restults from all the folders if wanted
    if args.aggregate:
        mse_location_mean = []
        mse_covariance_mean = []
        mse_location_std = []
        mse_covariance_std = []
        trials_per_group = []
        for folder in folders:

            # Load results
            with open(os.path.join(folder, 'results.pkl'), 'rb') as f:
                results = pickle.load(f)

            # Aggregate results
            mse_location_mean.append(results['mse_location_mean'])
            mse_covariance_mean.append(results['mse_covariance_mean'])
            mse_location_std.append(results['mse_location_std'])
            mse_covariance_std.append(results['mse_covariance_std'])
            trias_range = results['trials_range']
            trials_per_group.append(trias_range[1] - trias_range[0] + 1)

        # Compute the weighted average
        mse_location_mean = np.average(mse_location_mean, axis=0,
                                       weights=trials_per_group)
        mse_covariance_mean = np.average(mse_covariance_mean, axis=0,
                                         weights=trials_per_group)

        # Compute the weighted standard deviation
        # TODO: VERIFY THIS FORMULA!!!!!!!
        mse_location_std = np.sqrt(np.average(
            (mse_location_std**2 + mse_location_mean**2), axis=0,
            weights=trials_per_group) - mse_location_mean**2)
        mse_covariance_std = np.sqrt(np.average(
            (mse_covariance_std**2 + mse_covariance_mean**2), axis=0,
            weights=trials_per_group) - mse_covariance_mean**2)

        # Plotting
        generate_figure(mse_location_mean,
                        mse_location_std,
                        mse_covariance_mean,
                        mse_covariance_std,
                        trias_range,
                        args.storage_path)

    else:
        # We plot the results from each folder
        for folder in folders:
            # Load results
            with open(os.path.join(folder, 'results.pkl'), 'rb') as f:
                results = pickle.load(f)

            # Plotting
            generate_figure(results['mse_location_mean'],
                            results['mse_location_std'],
                            results['mse_covariance_mean'],
                            results['mse_covariance_std'],
                            results['trials_range'],
                            folder,
                            args.save)

    plt.show()
