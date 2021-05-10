# Overview
Name / Title: General Esports Data
Link to Data: "https://www.kaggle.com/rankirsh/esports-earnings"
Source / Origin:
Author or Creator: Ran.Kirsh
Publication Date: 2020/07
Publisher: Ran.Kirsh
Version or Data Accessed: Vision8
License: CC0: Public Domain
Can You Use this Data Set for Your Intended Use Case? Yes
Col Name(Type): Game(String); ReleaseDate(Int);Genre(String);TotalEarning(Float);TotalPlayer(Int);TotalToutnaments(Int)

# Table Design
No Null value(At least I thinkt)
Name value as the primary key
Name value as char(100); ReleaseData as numeric; Genre as char; TotalEarning as numeric;TotalPlayer as numeric; TotalTournaments as numeric;

# Import
One of the most important issue I have is that I am unable to import the csv file due to the wrong location I have. To solve this, I change the location of the file to the most default location so that now it works.

# Database Information
1.show all of databases in your postgres instance
                                                 List of databases
    Name    |  Owner   | Encoding |          Collate           |           Ctype            |   Access privileges
------------+----------+----------+----------------------------+----------------------------+-----------------------
 homework06 | postgres | UTF8     | English_United States.1252 | English_United States.1252 |
 postgres   | postgres | UTF8     | English_United States.1252 | English_United States.1252 |
 template0  | postgres | UTF8     | English_United States.1252 | English_United States.1252 | =c/postgres          +
            |          |          |                            |                            | postgres=CTc/postgres
 template1  | postgres | UTF8     | English_United States.1252 | English_United States.1252 | =c/postgres          +
            |          |          |                            |                            | postgres=CTc/postgres
(4 rows)

2.(making sure you're connected to homework06 database) show all of the tables in your database
          List of relations
 Schema |  Name   | Type  |  Owner
--------+---------+-------+----------
 public | esport  | table | postgres
 public | esport3 | table | postgres
 public | esport4 | table | postgres
 public | esports | table | postgres
(4 rows)

3.finally, show some information about the table you created and imported data into: find a way to show its columns, types and constraints
                           Table "public.esport"
      Column      |          Type          | Collation | Nullable | Default
------------------+------------------------+-----------+----------+---------
 game_name        | character varying(100) |           | not null |
 release_date     | numeric                |           | not null |
 genre            | character varying(50)  |           | not null |
 total_earning    | numeric                |           | not null |
 total_player     | numeric                |           | not null |
 total_tournament | numeric                |           | not null |
 is_game          | integer                |           |          | 1
Indexes:
    "esport_pkey" PRIMARY KEY, btree (game_name)

# Query Results
1. the total number of rows in the database
count
-------
   512
(1 row)

2. show the first 15 rows, but only display 3 columns (your choice)
                   row
-----------------------------------------
 ("Age of Empires",Strategy,1997)
 ("Age of Empires II",Strategy,1999)
 ("Age of Empires III",Strategy,2005)
 ("Age of Empires Online",Strategy,2011)
 ("Age of Mythology",Strategy,2002)
 ("Among Us",Strategy,2018)
 ("Auto Chess",Strategy,2019)
 ("Brawl Stars",Strategy,2018)
 (Chess.com,Strategy,2007)
 (chess24,Strategy,2014)
 ("Clash of Clans",Strategy,2012)
 ("Clash Royale",Strategy,2016)
 ("Command & Conquer 3",Strategy,2007)
 ("Company of Heroes 2",Strategy,2013)
 (ComPet,Strategy,2016)
(15 rows)

3. do the same as above, but chose a column to sort on, and sort in descending order
                               row
------------------------------------------------------------------
 (VALORANT,"First-Person Shooter",2020)
 ("SLAYERS FOR HIRE","Fighting Game",2020)
 ("Escape from Tarkov","First-Person Shooter",2020)
 ("Halo: Infinite","First-Person Shooter",2020)
 ("Kirby Fighters 2","Fighting Game",2020)
 (Schwarzerblitz,"Fighting Game",2020)
 ("Call of Duty: Black Ops Cold War","First-Person Shooter",2020)
 (Diabotical,"First-Person Shooter",2020)
 (Prophecy,Strategy,2020)
 ("Iron Harvest",Strategy,2020)
 ("Call of Duty: Warzone","First-Person Shooter",2020)
 ("Hyper Scape","Multiplayer Online Battle Arena",2020)
 ("WarCraft III: Reforged",Strategy,2020)
 ("Maiden & Spell","Fighting Game",2020)
 ("Street Fighter V: Champion Edition","Fighting Game",2020)
(15 rows)
4. add a new column without a default value
ALTER TABLE
5. set the value of that new column
ALTER TABLE
6. show only the unique (non duplicates) of a column of your choice
 release_date
--------------
         2000
         1989
         2012
         2011
         2003
         2016
         2010
         1993
         2015
         2007
         2001
         2005
         2013
         2008
         2017
         2006
         1996
         2004
         1981
         2018
         1998
         2009
         1994
         1997
         2019
         1995
         2002
         2014
         2020
         1999
(30 rows)
7.group rows together by a column value (your choice) and use an aggregate function to calculate something about that group 
 release_date |     sum
--------------+--------------
         2000 |  13764721.96
         1989 |     26426.38
         2012 | 115286364.11
         2011 |   2154498.62
         2003 |   1262452.80
         2016 |  49372583.83
         2010 |  44760635.87
         1993 |      4638.56
         2015 |  75697407.08
         2007 |  12241863.61
         2001 |   3666793.85
         2005 |   2156165.95
         2013 | 235365800.17
         2008 |   3230388.97
         2017 | 148105234.82
         2006 |   1041683.27
         1996 |     104741.7
         2004 |  12108029.57
         1981 |            0
         2018 |  23030728.96
         1998 |   8417662.18
         2009 |  82046551.94
         1994 |     32725.21
         1997 |    339571.06
         2019 |  18785008.44
         1995 |     13381.19
         2002 |   7372909.41
         2014 |  40769756.46
         2020 |   7750862.51
         1999 |   3135152.82
(30 rows)
8. now, using the same grouping query or creating another one, find a way to filter the query results based on the values for the groups 
 release_date |     sum
--------------+--------------
         2000 |  13764721.96
         2012 | 115286364.11
         2016 |  49372583.83
         2010 |  44760635.87
         2015 |  75697407.08
         2007 |  12241863.61
         2013 | 235365800.17
         2017 | 148105234.82
         2004 |  12108029.57
         2018 |  23030728.96
         2009 |  82046551.94
         2019 |  18785008.44
         2014 |  40769756.46
(13 rows)
9. find the order of average income of the game after 2000
release_date |     sum
--------------+--------------
         2013 | 235365800.17
         2017 | 148105234.82
         2012 | 115286364.11
         2009 |  82046551.94
         2015 |  75697407.08
         2016 |  49372583.83
         2010 |  44760635.87
         2014 |  40769756.46
         2018 |  23030728.96
         2019 |  18785008.44
         2007 |  12241863.61
         2004 |  12108029.57
         2020 |   7750862.51
         2002 |   7372909.41
         2001 |   3666793.85
         2008 |   3230388.97
         2005 |   2156165.95
         2011 |   2154498.62
         2003 |   1262452.80
         2006 |   1041683.27
(20 rows)
10. find the order of avg of income of the game before 2000
 release_date |          avg
--------------+------------------------
         1998 |   1202523.168571428571
         1999 |    261262.735000000000
         1997 |     84892.765000000000
         1989 |     26426.380000000000
         1996 |     26185.425000000000
         1994 |  8181.3025000000000000
         1995 |  3345.2975000000000000
         1993 |  2319.2800000000000000
         1981 | 0.00000000000000000000
(9 rows)
11. add a new column get earning per player
ALTER TABLE
12. calculate the result
UPDATE 465