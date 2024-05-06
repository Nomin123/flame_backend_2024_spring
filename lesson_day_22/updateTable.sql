create table lesson_day_22.courses(
	course_id serial primary key,
	course_name varchar(255) not null,
	price decimal(10,2) not null,
	description varchar(500),
	published_date date
);

INSERT INTO courses( course_name, price, description, published_date)
VALUES
('PostgreSQL for Developers', 299.99, 'A complete PostgreSQL for Developers', '2020-07-13'),
('PostgreSQL Admininstration', 349.99, 'A PostgreSQL Guide for DBA', NULL),
('PostgreSQL High Performance', 549.99, NULL, NULL),
('PostgreSQL Bootcamp', 777.99, 'Learn PostgreSQL via Bootcamp', '2013-07-11'),
('Mastering PostgreSQL', 999.98, 'Mastering PostgreSQL in 21 Days', '2012-06-30');

select *from courses c ;

update table

update courses 
set published_date ='2020-08-01'
where course_id =3;

update lesson_day_22.courses 
set published_date ='2020-07-01'
where course_id =2
returning *;

update lesson_day_22.courses 
set description ='PostgreSQL High Performance'
where course_id =3
returning *;

update lesson_day_22.courses 
set price=price*1.5
returning *;

