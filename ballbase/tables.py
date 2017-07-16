#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
    tables
    ~~~~~~

    This module provides plotted tables of values.
"""
import matplotlib.pyplot as plt
from matplotlib import gridspec
import pandas as pd
import seaborn as sns


def table_central_tend(data, axs, f=2):
    """Returns a plotted table on an axs.

    Based on statistics for central tendancy, can
    take one column or more.

    Requires an matplot lib `axs` as input to be used.

    Parameters
    ----------
    data : DataFrame object
        Pandas DataFrame containing columns to be used
        for statistics.
    axs : matplotlib axs object
        axs (e.g. subplot object) from matplotlib in which
        the plot shall be created.
    f : int
        Interger to set the rounding position to be presented in
        the table.

    See Also
    --------
    descriptive_table : function which plots a group of tables together
    """

    # Central tendacy
    v_mean = round(data.mean(), f)
    v_median = round(data.median(), f)

    # Use built in tex only, no depandancy needed
    sample_mean_str = "mean, " + r' $\bar x$ '
    sample_median_str = "median"

    # Concatenate the statistics and symbols
    symbols = pd.DataFrame([sample_mean_str, sample_median_str])
    val = pd.DataFrame([v_mean, v_median])
    data = pd.concat([symbols, val], axis=1)

    # Plot onto matplotlib axs
    central_tend = axs.table(
                             cellText=data.values,
                             loc='center',
                             cellLoc="center",
                             colLoc='center',
                             # xmin, ymin, width, height
                             bbox=(0, 0, 1, 1),
                             edges=""      # No line
                             )

    title_color = '#9099A2'  # Dark grey
    axs.set_title(
                  ('Central Tendancy'),
                  fontsize=12,
                  color=title_color
                  )

    table_settings(axs, central_tend)


def table_disperssion(data, axs, f=2):
    """Returns a plotted table on an axs.

    Based on statistics for disperssion, can
    take one column or more.

    Requires an matplot lib `axs` as input to be used.

    Parameters
    ----------
    data : DataFrame object
        Pandas DataFrame containing columns to be used
        for statistics.
    axs : matplotlib axs object
        axs (e.g. subplot object) from matplotlib in which
        the plot shall be created.
    f : int
        Interger to set the rounding position to be presented in
        the table.

    See Also
    --------
    descriptive_table : function which plots a group of tables together
    """

    # Measures of disperssion
    v_bessel_sd = round(data.std(), f)
    v_var = round(data.var(), f)
    v_range = round((data.max()-data.min()), f)
    v_iqr = round((data.quantile(0.75)-data.quantile(0.25)), f)
    v_mad = round(data.mad(), f)

    # Use built in tex only, no depandancy needed
    sample_std_str = "stan. dev." + r' $s$ '
    sample_var_str = "variance, " + '$s^2$'
    sample_range_str = "range"
    sample_iqr_str = "$IQR$"
    sample_mad_str = "mean abs. dev."

    symbols = pd.DataFrame(
                        [sample_std_str, sample_iqr_str,
                         sample_mad_str, sample_var_str,
                         sample_range_str]
                        )
    val = pd.DataFrame(
                    [v_bessel_sd,  v_iqr,
                     v_mad, v_var, v_range]
                     )
    data = pd.concat([symbols, val], axis=1)

    disperssion = axs.table(
                            cellText=data.values,
                            loc='center',
                            cellLoc="center",
                            colLoc='right',
                            # xmin, ymin, width, height
                            bbox=(0, 0, 1, 1),
                            edges="")  # No line

    title_color = '#9099A2'  # Dark Grey
    axs.set_title(
                  ('Disperssion'),
                  fontsize=12,
                  color=title_color)

    table_settings(axs, disperssion)


def table_distribution(data, axs, f=2):
    """Returns a plotted table on an axs.

    Based on statistics for distribution, can
    take one column or more.

    Requires an matplot lib `axs` as input to be used.

    Parameters
    ----------
    data : DataFrame object
        Pandas DataFrame containing columns to be used
        for statistics.
    axs : matplotlib axs object
        axs (e.g. subplot object) from matplotlib in which
        the plot shall be created.
    f : int
        Interger to set the rounding position to be presented in
        the table.

    See Also
    --------
    descriptive_table : function which plots a group of tables together
    """

    # Measures of distribution
    v_max = round(data.max(), f)
    v_95 = round((data.quantile(0.95)), f)
    v_90 = round((data.quantile(0.9)), f)
    v_75 = round((data.quantile(0.75)), f)
    v_50 = round((data.quantile(0.5)), f)
    v_25 = round((data.quantile(0.25)), f)
    v_10 = round((data.quantile(0.1)), f)
    v_05 = round((data.quantile(0.05)), f)
    v_min = round(data.min(), f)

    # pandas quantile returns a series which needs to be recombined
    # hence reset_index and transpose used in this case.
    quantiles = pd.concat(
                          [v_max, v_95, v_90,
                           v_75, v_50, v_25,
                           v_10, v_05, v_min],
                          axis=1
                          ).transpose().reset_index()
    quantiles.drop('index', axis=1, inplace=True)

    # Use built in tex only, no depandancy needed
    sample_max_str = r"maximum"
    sample_95_str = r"$Q(0.95)$"
    sample_90_str = r"$Q(0.90)$"
    sample_75_str = r"$Q(0.75)$"
    sample_50_str = r"$Q(0.50)$"
    sample_25_str = r"$Q(0.25)$"
    sample_10_str = r"$Q(0.10)$"
    sample_05_str = r"$Q(0.05)$"
    sample_min_str = r"minimum"

    symbols = pd.DataFrame([sample_max_str, sample_95_str, sample_90_str,
                            sample_75_str, sample_50_str, sample_25_str,
                            sample_10_str, sample_05_str, sample_min_str])

    data = pd.concat([symbols, quantiles], axis=1)

    distribution = axs.table(
                             cellText=data.values,
                             loc='center',
                             cellLoc="center",
                             colLoc='right',
                             # xmin, ymin, width, height
                             bbox=(0, 0, 1, 1),
                             edges="")

    title_color = '#9099A2'
    axs.set_title(
                  ('Distribution'),
                  fontsize=12,
                  color=title_color)

    table_settings(axs, distribution)


def table_top(data, name, axs):
    """Returns a plotted table on an axs.

    Simpy creates a small table with the count of samples
    and column headers.

    Intended to act as the top of a set of tables.

    Requires an matplot lib `axs` as input to be used.

    Parameters
    ----------
    data : DataFrame object
        Pandas DataFrame containing columns to be used
        for statistics.
    name : list
        List of strings containing the names intended for
        each column header. Rather than extracting this from a
        column header this gives precision in what the name will
        be called.
    axs : matplotlib axs object
        axs (e.g. subplot object) from matplotlib in which
        the plot shall be created.

    See Also
    --------
    descriptive_table : function which plots a group of tables together
    """

    # Count
    v_count = []
    for i in name:
        v_col_size = data[i].size
        v_count.append(v_col_size)

    # Use built in tex only, no depandancy needed
    sample_count_str = "samples, " + r' $n$ '

    symbols = pd.DataFrame([sample_count_str])
    val = pd.DataFrame([v_count])
    data = pd.concat([symbols, val], axis=1)

    # Get column names out of list
    labels = [""]
    for i in name:
        labels.append(i)

    top = axs.table(
                    cellText=data.values,
                    colLabels=labels,
                    loc='center',
                    cellLoc="center",
                    colLoc='center',
                    # xmin, ymin, width, height
                    bbox=(0, 0, 1, 1),
                    edges="")

    table_settings(axs, top)

    # As the above table_settings function sets black
    # line on top overwrite that setting
    axs.spines['top'].set_color('white')


def table_settings(axs_num, table_name):
    """Sets style settings on a table.

    Requires an matplot lib `axs` as input to be used.

    Enforces style settings onto that axs.

    Parameters
    ----------
    axs_num : matplotlib axs object
        axs (e.g. subplot object) from matplotlib in which
        will have style settings applied to it.
    table_name : axs_plot
        A plotted matplotlib image on an axs.

    See Also
    --------
    descriptive_table : function which plots a group of tables together
    """

    table_props = table_name.properties()
    table_cells = table_props['child_artists']  # matplotlib setting
    # iterate through cells of a table to change properties
    for cell in table_cells:
            cell._text.set_fontsize(15)
            cell._text.set_color('#192231')  # Light grey

    # Set axis tick labels off, i.e. empty [].
    axs_num.set_yticklabels([])
    axs_num.set_xticklabels([])

    # Seaborn settings
    sns.set_style("whitegrid")
    sns.set_style({'axes.grid': False})
    sns.set_context(
                    "poster",
                    rc={'font.sans-serif': 'Gill Sans MT'}
                    )

    sns.despine(offset=2, top=False, trim=False, left=True, bottom=True)

    # Leave one line on top to break up the table
    axs_num.spines['top'].set_color('#9099A2')

    # Set tick labels to white in case they still are showing,
    # perhaps redudent but this is not perfect.
    plt.setp(
             [axs_num.get_xticklines(), axs_num.get_yticklines()],
             color="white"
            )


def descriptive_table(data, column_name, fig_size=(8, 8)):
    """Creates a plotted table of descriptive statistics.

    Parameters
    ----------
    data : DataFrame
        pandas DataFrame containing data corresponding to column
        names. Only select columns to be displayed in table.
    column_name : list
        List of strings for column names. Not selected by
        column header in DataFrame this sets it.
    fig_size : tuple
        Two ints/floats to set the figure size. First value is
        width, second value is height.

    See Also
    --------
    descriptive_table : function which plots a group of tables together
    """

    # Set up figure dimensions and sub components.
    sheet, axs = plt.subplots(4, 1, figsize=fig_size)

    # Heights ratio is based on the number of rows in each
    # table, this relates to the number of statistics each
    # sub table will show.
    gs = gridspec.GridSpec(4, 1, height_ratios=[2, 2, 5, 9])

    # Assign all subplots based on figure dimensions.
    ax0 = plt.subplot(gs[0])
    ax1 = plt.subplot(gs[1])
    ax2 = plt.subplot(gs[2])
    ax3 = plt.subplot(gs[3])

    title_color = '#9099A2'  # Dark grey
    plt.suptitle(
                 'Descriptive Statistics',
                 fontsize=16,
                 color=title_color,
                 x=0.25
                 )

    table_top(data, column_name, ax0)
    table_central_tend(data, ax1)
    table_disperssion(data, ax2)
    table_distribution(data, ax3)

    # Adjust the spacing so the title fits correctly.
    sheet.subplots_adjust(hspace=0.2, top=0.95)
