#!/usr/bin/python

import matplotlib.pyplot as plt
import seaborn as sns

# Color schemes
b_and_w = ['#D5D5D5', '#9099A2', '#6D7993', '#96858F']
ToddTerje = ['#F24C4E', '#EAB126', '#1FB58F', '#1B7B34']
cool_blue = ['#99D3DF','#88BBD6','#CDCDCD', '#E9E9E9']
custom = ['#192231','#3C3C3C','#CDCDCD', '#494E6B']


def common_set_up(ax_size):
    """Common plot set up to be
    re-used in other figures.
    """
    
    sns.set_style("whitegrid")
    sns.set_style("ticks", {'axes.grid': True, 'grid.color': '.99', 'ytick.color': '.4', 'xtick.color': '.4'})
    sns.set_context("poster", font_scale=0.8, rc={"figure.figsize": ax_size, 'font.sans-serif': 'Gill Sans MT'})


def univariate(x, univariate_name, color_set=custom, bin_n=None, ax_size=(12, 6), funky=False):
    """Make a univariate distribution
    of a variable.

    Returns an object to be plotted.
    """

    if funky:
        color_set = ToddTerje

    common_set_up(ax_size) # Apply basic plot style

    ax = sns.distplot(x, bins=bin_n, rug=True,
                      hist_kws={"histtype": "bar", "linewidth": 1, "alpha": 1, "color": color_set[2], 'label': 'Histogram'},
                      kde_kws={"color": color_set[0], "lw": 3, "label": "KDE"},
                      rug_kws={"color": color_set[1], 'lw': 0.3, "alpha": 0.5, 'label': 'rug plot', 'height': 0.05})

    sns.despine(offset=2, trim=True, left=True, bottom=True)

    title_color = '#192231'
    font_colour = '#9099A2'
    ax.set_title('Univariate distribution of {0}, with rug plot'.format(univariate_name),
                  fontsize=20, color=title_color)
    ax.set_ylabel('Frequency of {0}'.format(univariate_name),
                   color=font_colour)
    ax.set_xlabel('{0}'.format(univariate_name),
                   color=font_colour)

    return ax


def boolean_bar(data, name, color_set=custom, ax_size=(2, 5), funky=False):
    """Make a univariate distribution
    of a variable.

    Returns an object to be plotted.
    """

    if funky:
        color_set = ToddTerje

    common_set_up(ax_size) # Apply basic plot style

    ax = sns.countplot(data, saturation=1,
                       color=color_set[2], label=name
                      )

    sns.despine(offset=2, trim=True, left=True, bottom=True)

    # Set title and axes
    title_color = '#192231'
    ax.set_title('{0}'.format(name),
                 fontsize=20, color=title_color)
    ax.set_ylabel('')
    ax.set_xlabel('')

    # Percentage annotation
    total = float(len(data))
    for p in ax.patches:
        ax.annotate('{:.2f}'.format((p.get_height()/total)), # Value to be anootated
                    (
                        p.get_x()+p.get_width()/2.,          # X position
                        p.get_height()-1300                  # y position
                    ),
                    ha='center', label='Fraction',
                    color=color_set[0])

    return ax


def count_bar(data, name, color_set=custom, ax_size=(20, 6), funky=False, highlight=None):
    """Make a univariate distribution
    of a variable.

    Returns an object to be plotted.
    """

    if funky:
        color_set = ToddTerje

    common_set_up(ax_size) # Apply basic plot style

    ax = sns.countplot(data, saturation=1,
                       color=color_set[2], label=name,
                      )

    sns.despine(offset=2, trim=True, left=True, bottom=True)

    # Set title and axes
    title_color = '#192231'
    font_colour = '#9099A2'
    ax.set_title('{0}'.format(name),
                 fontsize=20, color=title_color)
    ax.set_ylabel('Frequency',
                   color=font_colour)
    ax.set_xlabel('{0}'.format(name),
                   color=font_colour)
    
    if highlight:
        bars = ax.patches
        bars[highlight].set_color(color_set[1])
    
    return ax
