drop table if exists students;
drop table if exists disciplines;
drop table if exists faculty;
drop table if exists curriculum;
drop table if exists ratings;

create table students
(
    id integer primary key autoincrement,
    full_name  varchar(255) NOT NULL,
    birthdate date NOT NULL,
    gender varchar(255) NOT NULL,
    group_number int
);
        
create table disciplines
(
    id integer primary key autoincrement,
    title varchar(255) NOT NULL,
    hours int NOT NULL,
    attestation varchar(255) NOT NULL,
    UNIQUE(title)
);
        
create table faculty
(
    id integer primary key autoincrement,
    direction varchar(255) NOT NULL,
    UNIQUE(direction)
);
        
create table curriculum
(
    id integer primary key autoincrement,
    direction_id int NOT NULL,
    discipline_id int NOT NULL,
    semester int NOT NULL,
    CHECK(semester <= 8)
);

create table ratings
(
    id integer primary key autoincrement,
    student_id int NOT NULL,
    discipline_id int NOT NULL,
    amount_of_mark_1 int NOT NULL,
    amount_of_mark_2 int NOT NULL,
    amount_of_mark_3 int NOT NULL,
    amount_of_mark_4 int NOT NULL,
    amount_of_mark_5 int NOT NULL,
    CHECK(amount_of_mark_1 + amount_of_mark_2 * 2 + amount_of_mark_3 * 3 + amount_of_mark_4 * 4 + amount_of_mark_5 * 5 <= 100)
);

INSERT INTO students VALUES
(1, "Akimova Darya Andreyevna", "2000-04-07", "female", 303),
(2, "Marvin Kopp Alexyevic", "1999-05-07", "male", 403),
(3, "Ivanov Ivan Ivanovich", "2001-04-07", "male", 302),
(4, "Marinova Marina Petrovna", "2001-04-07", "female", 101),
(5, "Zaikina Zinaida Petrovna", "2002-04-07", "female", 104),
(6, "Shabanov Ilya Nikolayevich", "2003-04-07", "male", 103);

INSERT INTO disciplines VALUES
(1, "Calculus", 180, "exam"),
(2, "Analytical geometry", 144, "exam"),
(3, "History", 144, "exam"),
(4, "Foreign language", 108, "credit"),
(5, "Differential equations", 108, "credit"),
(6, "Discrete maths", 108, "credit"),
(7, "Theory of mechanics", 144, "exam");

INSERT INTO faculty VALUES
(1, "Mathematics and computer science"),
(2, "Fundamental computer science and information technology"),
(3, "Applied math and informatics"),
(4, "Software engineering");

INSERT INTO curriculum VALUES
(1, 1, 1, 1),
(2, 1, 2, 1),
(3, 1, 3, 1),
(4, 1, 4, 1),
(5, 4, 5, 1),
(6, 3, 5, 3),
(8, 2, 7, 5),
(8, 3, 7, 5);

INSERT INTO ratings VALUES
(NULL, 1, 7, 0, 0, 0, 4, 14),
(NULL, 4, 1, 0, 2, 3, 10, 4),
(NULL, 4, 2, 3, 5, 3, 10, 3),
(NULL, 4, 3, 0, 0, 0, 10, 7),
(NULL, 5, 6, 0, 0, 0, 10, 10),
(NULL, 3, 7, 0, 0, 5, 20, 0);
