order by

select first_name, last_name from public.customer c
order by c.first_name asc , c.last_name desc;

select 
	first_name,
	length(first_name) len
from
	public.customer 
order by
len desc;

select distinct 

select 
	distinct
	first_name
from
	public.customer 
order by first_name desc;

select * from film;

select 
	f.film_id,
	f.title,
	f.rental_rate
into table public.film_r
from 
	public.film f
where 
	f.rating='R'
and f.rental_duration =5
order by 
	f.title;

select * from film_r fr;

create table lesson_day_22.animal(
	animal_id serial primary key,
	race varchar(255),
	animal_age integer,
	gender varchar(10)
);

alter table lesson_day_22.animal add column can_fly smallint default 0;

select * from animal a;

insert into lesson_day_22.animal(race,animal_age, gender)
values('Mammalia',3 ,'male');

alter table lesson_day_22.animal add column test varchar;
alter table lesson_day_22.animal drop column test;

alter table lesson_day_22.animal rename column race to animal_race;

alter table lesson_day_22.animal  alter column can_fly set default 1;





	
