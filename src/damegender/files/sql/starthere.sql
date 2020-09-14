

drop database dame;
create database if not exists dame;
use dame;


CREATE TABLE Countries (
    CountryId int NOT NULL AUTO_INCREMENT,
    Name_en varchar(255),
    Locale varchar(255) NOT NULL,
    PRIMARY KEY (CountryId)
);

insert into Countries values (1, 'au');
insert into Countries values (2, 'be');
insert into Countries values (3, 'ca');
insert into Countries values (4, 'es');
insert into Countries values (5, 'fi');
insert into Countries values (6, 'ie');
insert into Countries values (7, 'is');
insert into Countries values (8, 'it');
insert into Countries values (9, 'nz');
insert into Countries values (10, 'pt');
insert into Countries values (11, 'uk');
insert into Countries values (12, 'us');
insert into Countries values (13, 'uy');

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


