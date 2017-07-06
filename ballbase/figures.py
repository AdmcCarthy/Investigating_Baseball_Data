#!/usr/bin/python

import matplotlib.pyplot as plt
import seaborn as sns
from .transformation import (
                            log_10, sq_rt
                            )

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


def formatting_text_box(ax, parameters, formatting_right):
    """ Returns the ax(axes within figures) with an
    added text box describing all parameters used.
    """

    font_colour = '#9099A2'

    # Text box set up
    text_box_patch = dict(boxstyle='round', facecolor='white', alpha=0.5, edgecolor='white')

    # Text box position
    if formatting_right:
        box_vertical = 0.83
        box_horizontal = 0.845
    else:
        box_vertical = 0.83
        box_horizontal = 0.05

    ax.text(box_horizontal, box_vertical, parameters, transform=ax.transAxes, fontsize=12,
            verticalalignment='top', color=font_colour, bbox=text_box_patch)
    
    return ax


def annotation_text(ax, string, vert_pos, horz_pos, color_set=custom, strong_colour=True, font_size=12):
    """ Returns the ax(axes within figures) with an
    added text box displaying an annotation
    """

    if strong_colour:
        font_c = color_set[0]
    else:
        font_c = '#9099A2'  # Light pale grey

    # Text box set up
    text_box_patch = dict(boxstyle='round', facecolor='white', alpha=0.2, edgecolor='white')

    ax.text(horz_pos, vert_pos, string, transform=ax.transAxes, fontsize=font_size,
    verticalalignment='top', color=font_c, bbox=text_box_patch)

    return ax


def univariate(x, univariate_name, color_set=custom, bin_n='all_values', ax_size=(12, 6), funky=False, rug=True, formatting_right=True, x_truncation_upper=None, x_truncation_lower=None, ax=None):
    """Make a univariate distribution
    of a variable.

    Returns an object to be plotted.
    """

    if funky:
        color_set = ToddTerje
    
    common_set_up(ax_size) # Apply basic plot style

    if bin_n == 'all_values':
        x_max = x.max()
        x_min = x.min()
        bin_n = int(x_max)-int(x_min)

    ax = sns.distplot(x, bins=bin_n, rug=rug, ax=ax,
                      hist_kws={"histtype": "bar", "linewidth": 1, 'align': 'mid', 'log': False, 'edgecolor': 'white', "alpha": 1, "color": color_set[2], 'label': 'Histogram'},
                      kde_kws={"color": color_set[0], "lw": 3, "label": "KDE"},
                      rug_kws={"color": color_set[1], 'lw': 0.3, "alpha": 0.5, 'label': 'rug plot', 'height': 0.05})

    title_color = '#192231'
    font_colour = '#9099A2'

    # Title and axis set up
    if rug:
        rugstr = ', with rug plot'
    else:
        rugstr = ''

    # Do not add a title in a multi-figure plot.
    #
    # Title will be added to figure with all sub-plots
    # instead in this case
    if ax is None: 
        ax.set_title(('Distribution of {0}'.format(univariate_name) + rugstr),
                    fontsize=20, color=title_color)
    ax.set_xlabel('{0}'.format(univariate_name),
                color=font_colour)
    ax.set_ylabel('Frequency'.format(univariate_name),
                   color=font_colour)

    # Limit the x axis by truncating
    if x_truncation_upper or x_truncation_lower:
        axes = ax.axes
        axes.set_xlim(x_truncation_lower, x_truncation_upper)
        # To be communicated back in Formatting notes
        x_truncation_upper_str = 'x axis truncated by {0}\n'.format(x_truncation_upper)
        x_truncation_lower_str = 'x axis truncated after {0}\n'.format(x_truncation_lower)
    else:
        x_truncation_upper_str = ''
        x_truncation_lower_str = ''
    
    # Used to describe the format of plot
    if bin_n is None:
        bin_n_str = 'automatic'
    else:
        bin_n_str = bin_n

    # String within text box
    parameters = ('Formatting:\n'
                + x_truncation_lower_str
                + x_truncation_upper_str
                + 'bins = {0}'.format(bin_n_str))
    
    # Will not work on multiple subplots within a figure
    if ax is None:
        # Seaborn despine to remove boundaries around plot
        sns.despine(offset=2, trim=True, left=True, bottom=True)

    ax = formatting_text_box(ax, parameters, formatting_right)

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


def univariate_overdispersed(x, univariate_name, transform='log_10', color_set=custom, bin_n='all_values', ax_size=(12, 6), funky=False, rug=False, formatting_right=True, x_truncation_upper=None, x_truncation_lower=None,  ax=None):
    """Retrun plot using data transformation to correct
    for overdispersed data.
    """

    if bin_n == 'all_values':
        x_max = x.max()
        x_min = x.min()
        bin_n = int(x_max)-int(x_min)

    # The function applied to pandas objects are
    # from .transformation
    if transform == 'log_10':
        x = x.apply(log_10)
        univariate_name = univariate_name + ' log10'
    elif transform == 'sqrt':
        x = x.apply(sq_rt)
        univariate_name = univariate_name + ' square root'

    ax = univariate(x, univariate_name, color_set=custom, bin_n=bin_n, ax_size=ax_size, funky=funky, rug=rug, formatting_right=formatting_right, x_truncation_upper=x_truncation_upper, x_truncation_lower=x_truncation_lower, ax=ax)

    return ax


def dist_transform_plot(x, univariate_name, fig_size=(18, 16), color_set=custom, bin_n='all_values', ax_size=(12, 6), funky=False, rug=True, formatting_right=True, x_truncation_upper=None, x_truncation_lower=None, ax=None):
    """Returns a plot including
    three individual plots alligned
    as three rows based on two data
    transforms.
    """

    fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(fig_size), facecolor='white')
    fig.subplots_adjust(hspace=0.18, top=0.95)

    common_set_up(fig_size)

    univariate_overdispersed(x, univariate_name, transform=None, color_set=color_set, bin_n=bin_n, ax_size=ax_size, funky=funky, rug=rug, formatting_right=formatting_right, x_truncation_upper=x_truncation_upper, x_truncation_lower=x_truncation_lower, ax=ax1)
    univariate_overdispersed(x, univariate_name, transform='log_10', color_set=color_set, bin_n=bin_n, ax_size=ax_size, funky=funky, rug=rug, formatting_right=formatting_right, x_truncation_upper=x_truncation_upper, x_truncation_lower=x_truncation_lower, ax=ax2)
    univariate_overdispersed(x, univariate_name, transform='sqrt', color_set=color_set, bin_n=bin_n, ax_size=ax_size, funky=funky, rug=rug, formatting_right=formatting_right, x_truncation_upper=x_truncation_upper, x_truncation_lower=x_truncation_lower, ax=ax3)

    sns.despine(offset=2, trim=True, left=True, bottom=True)

    return fig
