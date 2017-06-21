===========================
Investigating Baseball Data
===========================

------------------
Problem definition
------------------

Where do baseball players come from?

Are there relationships between where baseball players comes from?


^^^^^^^^^^^^^^^^^^^^^^^^^^^
Approach to answer question
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Take the MASTER.csv table and use this as a central source for unique playerID, this will relate to many other tables.

Attributes will be needed to describe the location each player is from. 

MASTER.csv also contains, birthCountry, birthState, birthCity which will be useful to investigate this question.

Schools and CollegePlaying are interesting candidates for this investigation.

schoolCity, schoolState, schoolID are all values to explore.

CollegePlaying.csv gives the data, while Schools.csv gives the lookup to what the values in schoolID mean.

These will give a variety of values about where the player came from.

Salaries, AwardsPlayers, AllStarFull and/or HallofFame can be used to give an indication to the quality of the player.

===============
Data processing
===============

Files are all csv files of high quality. playerID acts as a common key across different csv files.

^^^^^^
Master
^^^^^^

MASTER.csv is a key dataset to lookup playerID along with a number of key attributes needed for investigating where a player is from.

----------------
College location
----------------

CollegePlaying.csv and Schools.csv will need to be manipulated to give the location of the school. This will lead to city, state and country for each school.

One person can attend more than one school. For brevity it is better to reduce this to one selection.

For simplicity this is choosen alphabetically. So given a tie, tulane is selected over vandy.
This will create a bias in the selection criteria but is good enough for the moment.

Each players selected school's city, state and country will be appended to the player from Schools.csv

-----------------
Quality of player
-----------------

To see if there are any relationships between relatively better or worse players some form of attribute will be needed to qualify quality.

^^^^^^^^
Salaries
^^^^^^^^

Salaries is one option, this data is delivered on a yearly basis. This would need to be manipulated into a single value, e.g. mean yearly salary. However this will not compare well over time so would need to be compared to other salaries in that year.

Salary data has only been collected since 1985. Given that salary changes over time due to a combination of factors it is difficult to
compare one year to another year.

Processing includes standardizing salary annually to see which players
earn more than others for each year.

To be able to make some simple comparissons each players career salary information needs to be compressed into single values.
Min, max and mean have been choosen, for annually standardized and unstandardized.

^^^^^^^^^^^^^
AwardsPlayers
^^^^^^^^^^^^^

AwardsPlayers gives a value that could be manipulated into a number of awards per player.

Processed to find the number of times a player has recieved an award.

Awards go back to 1877, however the occurence of awards varies over time as the number of awards
given out per year changes.

^^^^^^^^^^^
AllStarFull
^^^^^^^^^^^

AllStarFull could also give a number of times present in the All Star game classifier.

Processed to find the number of times a player has played in an all star game.

Data only begins at 1933. The highest number of occurences in all star games is 25 by aaronha01.

^^^^^^^^^^
HallofFame
^^^^^^^^^^

HallofFame can also give a qualifier to compare to.

Processed to find all inducted members within the hall of fame.

Data only begins at 1933. There are 250 players in the hall of fame. 

^^^^^
Other
^^^^^

There are a number of limitations to these approaches related to how each of these have changed through time.

Performance statistics like Batting or Fielding could be used but will be left out for this analysis.

-------
Modules
-------

^^^^^^^
getdata
^^^^^^^

Contains a method to download the Sean Lahman Baseball database
directly from the website.

.. code-block:: python

    getdata.download_file()

^^^^^^^^^^^
pre_process
^^^^^^^^^^^

Pre-process data to wrangle it into a usable format for a specific problem.

--------------
Resources used
--------------

Pandas API
https://pandas.pydata.org/pandas-docs/stable/api.html

StackOverflow for number of times a value occurs in a column
https://stackoverflow.com/questions/22391433/count-the-frequency-that-a-value-occurs-in-a-dataframe-column

StackOverflow how to transpose a dataset using groupby
https://stackoverflow.com/questions/38369424/groupby-transpose-and-append-in-pandas