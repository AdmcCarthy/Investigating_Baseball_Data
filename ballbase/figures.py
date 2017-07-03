#!/usr/bin/python

import matplotlib.pyplot as plt
import seaborn as sns

b_and_w = ['#D5D5D5', '#9099A2', '#6D7993', '#96858F']
ToddTerje = ['#1FB58F', '#EAB126', '#F24C4E', '#1B7B34']
cool_blue = ['#99D3DF','#88BBD6','#CDCDCD', '#E9E9E9']
cccd = ['#FA7C92', '#6EC4DB', '#FFF7C0', '#66AB8C']
brandts = ['#252839', '#677077', '#f2b632', '#b5b5b7']
earthy = ['#49412c', '#97743a', '#262216', '#b0a18e']
custom = ['#192231','#3C3C3C','#CDCDCD', '#494E6B']

def common_set_up(fig_size):
    """Common plot set up to be
    re-used in other figures.
    """

    
    sns.set_style("whitegrid")
    sns.set_style("ticks", {'axes.grid': True, 'grid.color': '.99', 'ytick.color': '.4', 'xtick.color': '.4'})
    sns.set_context("poster", font_scale=0.8, rc={"figure.figsize": fig_size, 'font.sans-serif': 'Gill Sans MT'})


def univariate(x, univariate_name, color_set=custom, bin_n=None, fig_size=(12, 6)):
    """Make a univariate distribution
    of a variable.

    Returns an object to be plotted.
    """

    common_set_up(fig_size) # Apply basic plot style

    fig = sns.distplot(x, bins=bin_n, rug=True,
                      hist_kws={"histtype": "bar", "linewidth": 1, "alpha": 1, "color": color_set[2], 'label': 'Histogram'},
                      kde_kws={"color": color_set[0], "lw": 3, "label": "KDE"},
                      rug_kws={"color": color_set[1], 'lw': 0.3, "alpha": 0.5, 'label': 'rug plot', 'height': 0.05})

    sns.despine(offset=2, trim=True, left=True, bottom=True)

    title_color = '#192231'
    font_colour = '#9099A2'
    fig.set_title('Univariate distribution of {0}, with rug plot'.format(univariate_name),
                  fontsize=20, color=title_color)
    fig.set_ylabel('Frequency of {0}'.format(univariate_name),
                   color=font_colour)
    fig.set_xlabel('{0}'.format(univariate_name),
                   color=font_colour)

    return fig
