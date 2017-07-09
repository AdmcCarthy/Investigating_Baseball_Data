===========================
Investigating Baseball Data
===========================


Problem definition
------------------

Where do the best baseball players come from?

Are there relationships between where baseball players comes from and their salary, awards, or all star status?


Approach to answer question
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Take the MASTER.csv table and use this as a central source for unique playerID, this will relate to many other tables.

Attributes will be needed to describe the location each player is from. 

MASTER.csv also contains, birthCountry, birthState, birthCity which will be useful to investigate this question.

Schools and CollegePlaying are interesting candidates for this investigation.

schoolCity, schoolState, schoolID are all values to explore.

CollegePlaying.csv gives the data, while Schools.csv gives the lookup to what the values in schoolID mean.

These will give a variety of values about where the player came from.

Salaries, AwardsPlayers, AllStarFull and/or HallofFame can be used to give an indication to the quality of the player.


Data Analysis
-------------

Consider raw.io as a way to make some quick d3.js plots.


Data Review
-----------

Overall the dataset is well organised.

Some datasets display issues regarding population.

.. figure:: resources\images\Weight_all_data.png
   :scale: 100 %

   Fig._. Distribution of Weight in pounds for entire dataset

Weight highlights this well. The three figures above are of the same dataset,
by reducing the bin numbers to the number of unique values it can be seen that
common weight measurements are taken every 5 pounds. The lowermost figure
limits the x-axis to highlight this further. Some values are populate according to
a higher granualarity. A solution to this issue would be to bin weight or similar issues.

Some extreme outliers occur within the data

.. figure:: resources\images\Weight_2_all_data.png
   :scale: 100 %

   Fig._. Distribution of Weight in pounds for entire dataset

Using weight again, but now with a rug plot to highlight where values occur
the minimum weight value can be viewed (see annotation). The minimum weight
is 65 pounds which is dramatically different than the rest of the sample.

This value can be found to be paired to a height of 43 inches, and corresponds to
Eddie Gaedel. This extreme outlier is a real occurence!

https://en.wikipedia.org/wiki/Eddie_Gaedel

It is beyond the scope of this investigation to do a complete
audit of all data in this database.

Data Cleaning Plan
~~~~~~~~~~~~~~~~~~

Identify causes

Define Operations

Test, Iterate & Review


Data processing
---------------

Files are all csv files of high quality. playerID acts as a common key across different csv files.

Each file will be concatenated into the index of College Location, therefore reducing the dataset only to areas where
College information is available.

.. figure:: resources\images\Distribution_of_Birth_Year_All_data.png
   :scale: 100 %

   Fig.1. Distribution of Birth Year for entire dataset

The above figure shows the distribution of birth year for all data values with this number.
The total number of values which have birth data are 18973 out of an original .....
The minimum is 1820. The mean is 1931

After selecting only data with information about which college was attended there are now only
6575 values and a difference in the distribution.

.. figure:: resources\images\Distribution_of_birth_year_final_data.png
   :scale: 100 %

   Fig.2. Distribution of Birth Year for data used here

The mean has moved up to 1947 with the data now more skewed towards more recent times.

This is a common theme within the data that different investigations will subset the dataset in different
ways. For example salary data is only available after 1985.

Master
~~~~~~

MASTER.csv is a key dataset to lookup playerID along with a number of key attributes needed for investigating where a player is from.


College location
----------------

CollegePlaying.csv and Schools.csv will need to be manipulated to give the location of the school. This will lead to city, state and country for each school.

One person can attend more than one school. For brevity it is better to reduce this to one selection.

For simplicity this is choosen alphabetically. So given a tie, tulane is selected over vandy.
This will create a bias in the selection criteria but is good enough for the moment.

Each players selected school's city, state and country will be appended to the player from Schools.csv

Some errors occur when trying to match schoolID from CollegePlaying.csv to Schools.csv. At least one occurence
was found where it could not find a value from CollegePlaying.csv in Schools.csv. When this occured the current
solution is to replace the value with 'NAN'.


Quality of player - Dependent variables
---------------------------------------

To see if there are any relationships between relatively better or worse players some form of attribute will be needed to qualify quality.

These will form a variety of variables that could be dependent on other variables.


Salaries
~~~~~~~~

Salaries is one option, this data is delivered on a yearly basis. This would need to be manipulated into a single value, e.g. mean yearly salary. However this will not compare well over time so would need to be compared to other salaries in that year.

Salary data has only been collected since 1985. Given that salary changes over time due to a combination of factors it is difficult to
compare one year to another year.

Processing includes standardizing salary annually to see which players
earn more than others for each year.

To be able to make some simple comparissons each players career salary information needs to be compressed into single values.
Min, max and mean have been choosen, for annually standardized and unstandardized.


AwardsPlayers
~~~~~~~~~~~~~

AwardsPlayers gives a value that could be manipulated into a number of awards per player.

Processed to find the number of times a player has recieved an award.

Awards go back to 1877, however the occurence of awards varies over time as the number of awards
given out per year changes.


AllStarFull
~~~~~~~~~~~

AllStarFull could also give a number of times present in the All Star game classifier.

Processed to find the number of times a player has played in an all star game.

Data only begins at 1933. The highest number of occurences in all star games is 25 by aaronha01.


HallofFame
~~~~~~~~~~

HallofFame can also give a qualifier to compare to.

Processed to find all inducted members within the hall of fame.

Data only begins at 1933. There are 250 players in the hall of fame. 


Other
~~~~~

There are a number of limitations to these approaches related to how each of these have changed through time.

Performance statistics like Batting or Fielding could be used but will be left out for this analysis.


Modules
-------


getdata
~~~~~~~

Contains a method to download the Sean Lahman Baseball database
directly from the website.

.. code-block:: python

    getdata.download_file()


pre_process
~~~~~~~~~~~

Pre-process data to wrangle it into a usable format for a specific problem.


Resources used
~~~~~~~~~~~~~~

PandasAPI_.

.. _PandasAPI: https://pandas.pydata.org/pandas-docs/stable/api.html

Seaborn Tutorial

https://seaborn.pydata.org/tutorial/distributions.html

How to change x and y limits with seaborn

https://stackoverflow.com/questions/25212986/how-to-set-some-xlim-and-ylim-in-seaborn-lmplot-facetgrid

matplotlib api

https://matplotlib.org/api/index.html

reStructeredText style guide.

http://docs.python-guide.org/en/latest/notes/styleguide/

StackOverFlow for number of times a value occurs in a column query - Link_

.. _Link: https://stackoverflow.com/questions/22391433/count-the-frequency-that-a-value-occurs-in-a-dataframe-column
 
StackOverflow how to transpose a dataset using groupby query - Link_

.. _Link: https://stackoverflow.com/questions/38369424/groupby-transpose-and-append-in-pandas

Code block for download_progress_hook() was taken from Udacity Tensorflow Example notebook.

https://github.com/tensorflow/tensorflow/blob/master/tensorflow/examples/udacity/1_notmnist.ipynb

Color choice for charts

https://designschool.canva.com/blog/website-color-schemes/