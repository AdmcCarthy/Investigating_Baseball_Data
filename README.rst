===========================
Investigating Baseball Data
===========================

------------------
Problem definition
------------------

Where do baseball players come from?

Are there relationships between where a baseball player comes from?


^^^^^^^^^^^^^^^^^^^^^^^^^^^
Approach to answer question
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Take the MASTER.csv table and use this as a central source for unique playerID, this will relate to many other tables.

MASTER.csv also contains, birthCountry, birthState, birthCity which will be useful to investigate this question.

Schools and CollegePlaying are interesting candidates for this investigation.

schoolCity, schoolState, schoolID are all interesting candidates.

Salaries, AwardsPlayers, AllStarFull and/or HallofFame could be used to give an indication to the quality of the player.

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