#!/usr/bin/python

import matplotlib.pyplot as plt
import seaborn as sns


def univariate(x, univariate_name, bin_n=None):
    """Make a univariate distribution
    of a variable.

    Returns an object to be plotted.
    """

    sns.set_style("whitegrid")
    sns.set_style("ticks", {'axes.grid': True, 'grid.color': '.99', 'ytick.color': '.4', 'xtick.color': '.4'})
    sns.set_context("poster", font_scale=0.8, rc={"figure.figsize": (12, 6)})

    ax = sns.distplot(x, bins=bin_n, rug=True,
                      hist_kws={"histtype": "bar", "linewidth": 1, "alpha": 1, "color": '#D5D5D5', 'label': 'Histogram'},
                      kde_kws={"color": '#9099A2', "lw": 3, "label": "KDE"},
                      rug_kws={"color": '#6D7993', 'lw': 0.3, "alpha": 0.5, 'label': 'rug plot', 'height': 0.05})

    sns.despine(offset=2, trim=True, left=True, bottom=True)

    ax.set_title('Univariate distribution of {0}, with rug plot'.format(univariate_name))
    ax.set_ylabel('Frequency of {0}'.format(univariate_name))
    ax.set_xlabel('{0}'.format(univariate_name))

    return ax
