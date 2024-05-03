CREATE  table contacts (
	id integer Primary key,
	first_name text not null,
	last_name text not null,
	email text not null unique,
	phone text not null unique
);
INSERT INTO contacts (id, first_name, last_name, email,phone)
values(1,"Bataa","Chimgee","chimgeeBataa@gmail.com","99112233");

INSERT INTO contacts (id, first_name, last_name, email,phone)
values(2,"Boldoo","tulgaa","boldoo1@gmail.com","99115467");

INSERT INTO contacts (id, first_name, last_name, email,phone)
values(3,"Tsetsegee","Boldoo","tsetsegee123@gmail.com","99113355");

select * from contacts;

create table movie(
	id integer primary key,
	movie_name varchar(255) not null,
	release_date date
);

select *from movie;

ALTER table movie 
rename to movies;

alter table movies
add column director_name varchar(255);

alter table movies
add column movie_type varchar(255);

alter table movies
add column t varchar(255);

INSERT into movies (id ,movie_name, release_date, director_name, movie_type, t )

values(1, "Lalalaland","2020-10-01","Robert Santiago","romcom","150min");


INSERT into movies (id ,movie_name, release_date, director_name, movie_type, t )

values(2,"Star is born", "2019-03-01","Steven Spielberg","drama","120min")

select * from movies;

DELETE from movies where id=1;

drop table movies;