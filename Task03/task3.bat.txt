#!/bin/bash
chcp 65001

sqlite3 movies_rating.db < db_init.sql

echo "1. Составить список фильмов, имеющих хотя бы одну оценку. Список фильмов отсортировать по году выпуска и по названиям. В списке оставить первые 10 фильмов."
echo --------------------------------------------------
sqlite3 movies_rating.db -box -echo "SELECT movies.title, movies.year FROM movies INNER JOIN ratings ON ratings.movie_id=movies.id GROUP BY movies.title HAVING count(movie_id)>=1 ORDER BY movies.year, movies.title LIMIT 10;"
echo " "

echo "2. Вывести список всех пользователей, фамилии (не имена!) которых начинаются на букву 'A'. Полученный список отсортировать по дате регистрации. В списке оставить первых 5 пользователей."
echo --------------------------------------------------
sqlite3 movies_rating.db -box -echo "SELECT name FROM users WHERE SUBSTR(SUBSTR(name, INSTR(name, ' ')+1),1,1)='A' ORDER BY register_date LIMIT 5;"
echo " "

echo "3.Написать запрос, возвращающий информацию о рейтингах в более читаемом формате: имя и фамилия эксперта, название фильма, год выпуска, оценка и дата оценки в формате ГГГГ-ММ-ДД. Отсортировать данные по имени эксперта, затем названию фильма и оценке. В списке оставить первые 50 записей."
echo --------------------------------------------------
sqlite3 movies_rating.db -box -echo "SELECT name, title, year, rating, DATE(timestamp,'unixepoch') as date FROM ratings INNER JOIN movies on movies.id = ratings.movie_id INNER JOIN users on ratings.user_id = users.id ORDER BY users.name,title,year,rating,date LIMIT 50;"
echo ""

echo "4. Вывести список фильмов с указанием тегов, которые были им присвоены пользователями. Сортировать по году выпуска, затем по названию фильма, затем по тегу. В списке оставить первые 40 записей."
echo --------------------------------------------------
sqlite3 movies_rating.db -box -echo "SELECT title, tag FROM tags INNER JOIN movies ON movie_id=movies.id ORDER BY year, title, tag LIMIT 40;"
echo " "

echo "5. Вывести список самых свежих фильмов. В список должны войти все фильмы последнего года выпуска, имеющиеся в базе данных. Запрос должен быть универсальным, не зависящим от исходных данных (нужный год выпуска должен определяться в запросе, а не жестко задаваться)."
echo --------------------------------------------------
sqlite3 movies_rating.db -box -echo "SELECT title FROM movies WHERE year=(select max(year) FROM movies);"
echo " "

echo "6.Найти все комедии, выпущенные после 2000 года, которые понравились мужчинам (оценка не ниже 4.5). Для каждого фильма в этом списке вывести название, год выпуска и количество таких оценок. Результат отсортировать по году выпуска и названию фильма."
echo --------------------------------------------------
sqlite3 movies_rating.db -box -echo "SELECT title, year, count(title) FROM movies INNER JOIN ratings on movies.id=ratings.movie_id INNER JOIN users on users.id=ratings.user_id WHERE ratings.rating>=4.5 AND gender='male' AND INSTR(movies.genres, 'Comedy')!=0 and year>2000 GROUP BY year, title ORDER BY year, title;"
echo ""

echo "7.Провести анализ занятий (профессий) пользователей - вывести количество пользователей для каждого рода занятий. Найти самую распространенную и самую редкую профессию посетитетей сайта."
echo --------------------------------------------------
sqlite3 movies_rating.db -box -echo "SELECT users.occupation,count(users.occupation) as number_occupation FROM users GROUP BY occupation;
SELECT occupation,max(number_occupation) as most_common_profession FROM (SELECT users.occupation,count(users.occupation) as number_occupation FROM users GROUP BY occupation);
SELECT occupation,min(number_occupation) as rarest_profession FROM (SELECT users.occupation,count(users.occupation) as number_occupation FROM users GROUP BY occupation);"
echo ""