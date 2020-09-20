-- Copyright (C) 2020  David Arroyo Menéndez
-- Author: David Arroyo Menéndez <davidam@gnu.org>
-- Maintainer: David Arroyo Menéndez <davidam@gnu.org>
-- You can share, copy and modify this software if you are a woman or you
-- are David Arroyo Menéndez and you include this note.


drop database damegender;
create database if not exists damegender;
use damegender;


CREATE TABLE Countries (
    CountryId int NOT NULL AUTO_INCREMENT,
    Locale varchar(255) NOT NULL,
    Name_en varchar(255),    
    PRIMARY KEY (CountryId)
);

insert into Countries values (1, 'au', 'Australia');
insert into Countries values (2, 'be', 'Belgium');
insert into Countries values (3, 'ca', 'Canada');
insert into Countries values (4, 'es', 'Spain');
insert into Countries values (5, 'fi', 'Finland');
insert into Countries values (6, 'ie', 'Ireland');
insert into Countries values (7, 'is', 'Island');
insert into Countries values (8, 'it', 'Italy');
insert into Countries values (9, 'nz', 'Norway');
insert into Countries values (10, 'pt', 'Portugal');
insert into Countries values (11, 'uk', 'United Kingdom');
insert into Countries values (12, 'us', 'United States of America');
insert into Countries values (13, 'uy', 'Uruguay');

CREATE TABLE Names (
    NameId int NOT NULL AUTO_INCREMENT,
    Name varchar(255) NOT NULL,    
    CountryId int NOT NULL,
    Frequency int NOT NULL,
    PRIMARY KEY (NameId),
    INDEX country (CountryId),    
    FOREIGN KEY (CountryId)
    	    REFERENCES Countries(CountryId)
	    ON DELETE CASCADE ON UPDATE CASCADE
);  


