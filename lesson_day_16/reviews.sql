select * from reviews_review ;

insert into reviews_review (Comment, Author, Dates)
values("Unuudur jndkjsnjks","Bataa","2024-04-22");
values("Today knckjsncksj","Boldoo","2023-04-12");
values("Today is Nice Day","Chimgee","2022-04-10");

UPDATE  reviews_review set comment="updated comment" WHERE  id=2;

DELETE FROM reviews_review WHERE  id=3;

