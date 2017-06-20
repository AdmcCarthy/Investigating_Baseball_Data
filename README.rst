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

MASTER.csv also contains, birthCountry, birthState, birthCity which will be useful to investigate this question.

Schools and CollegePlaying are interesting candidates for this investigation.

schoolCity, schoolState, schoolID are all values to explore.

CollegePlaying.csv gives the data, while Schools.csv gives the lookup to what the values in schoolID mean.

Salaries, AwardsPlayers, AllStarFull and/or HallofFame could be used to give an indication to the quality of the player.

===============
Data processing
===============

Files are all csv files of high quality. playerID acts as a common key across different csv files.

^^^^^^
Master
^^^^^^

MASTER.csv is a key dataset to lookup playerID along with a number of key attributes needed for investigating where a player is from.

------------------
Location of player
------------------

CollegePlaying.csv and Schools.csv will need to be manipulated to give the location of the school. This will lead to city, state and country for each school.

-----------------
Quality of player
-----------------

To see if there are any relationships between relatively better or worse players some form of attribute will be needed to qualify quality.

^^^^^^^^
Salaries
^^^^^^^^

Salaries is one option, this data is delivered on a yearly basis. This would need to be manipulated into a single value, e.g. mean yearly salary. However this will not compare well over time so would need to be compared to other salaries in that year.

^^^^^^^^^^^^^
AwardsPlayers
^^^^^^^^^^^^^

AwardsPlayers gives a value that could be manipulated into a number of awards per player.

^^^^^^^^^^^
AllStarFull
^^^^^^^^^^^

AllStarFull could also give a number of times present in the All Star game classifier.

^^^^^^^^^^
HallofFame
^^^^^^^^^^

HallofFame can also give a qualifier to compare to.

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