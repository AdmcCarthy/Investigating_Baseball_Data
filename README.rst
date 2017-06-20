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

^^^^^^^^^^^^^^^
Data processing
^^^^^^^^^^^^^^^

MASTER.csv is a key dataset to lookup playerID along with a number of key attributes needed for investigating where a player is from.

CollegePlaying.csv and Schools.csv will need to be manipulated to give the location of the school. This will lead to city, state and country for each school.

Files are all csv files. 

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