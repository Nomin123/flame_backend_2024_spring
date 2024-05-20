create table professor(
    prof_id integer primary key,
    prof_lname varchar(50),
    prof_fname varchar(50)
);
create table student(
    stud_id integer primary key,
    stud_fname varchar(50),
    stud_lname varchar(50),
    stud_street varchar(255),
    stud_city varchar(50),
    stud_zip varchar(10)
);
create table course(
    course_id integer primary key,
    course_name varchar(255)
 );
create table class(

<!-- dasgal 1 -->
<!-- 1. Категори бүрийн нийт ĸиног нь харуулна уу. category table-ээс film болон film_category
table-руу холбогдоод хийнэ үү. -->

select category.name ,avg(film.rental_duration)  as avg_rental_duration from category left join film_category on category.category_id=film_category.category_id left join film on film_category.film_id=film.film_id group by category.name;
<!-- 2. film-ийн дундаж rental_duration-аар нь харуулна уу. film, category table-ээс
rental_duration-ийг олоод AVG фунĸц ашиглана уу. -->

select category.name ,avg(film.rental_duration)  as avg_rental_duration from category left join film_category on category.category_id=film_category.category_id left join film on film_category.film_id=film.film_id group by category.name;

<!-- 3. film table-ээс rental_rate, rental_duration-аар total_revenue-г олно уу.
total_revenue-г film-ийн title-аар хувааж харуулна уу. -->

SELECT film.title, sum(rental_rate*rental_duration) as total_revenue from film group by film.title;