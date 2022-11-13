INSERT INTO users SELECT MAX(id) + 1,"Darya Akimova","akimdar@yandex.ru","female","2022-11-13","student" FROM users;
INSERT INTO users SELECT MAX(id) + 1,"Sergey Akaykin","akserg@gmail.com","male","2022-11-13","student" FROM users;
INSERT INTO users SELECT MAX(id) + 1,"Alexey Artamonov","javaboss@vk.com","male","2022-11-13","student" FROM users;
INSERT INTO users SELECT MAX(id) + 1,"Anna Bugreyeva","bugrann@yandex.ru","female","2022-11-13","student" FROM users;
INSERT INTO users SELECT MAX(id) + 1,"Yana Venedictova","venedictova@yandex.ru","female","2022-11-13","student" FROM users;

INSERT INTO movies SELECT MAX(id) + 1, "The Black Phone", 2021 FROM movies;
INSERT INTO movies SELECT MAX(id) + 1, "The Little Things", 2021 FROM movies;
INSERT INTO movies SELECT MAX(id) + 1, "Memory", 2022 FROM movies;

INSERT INTO movies_genres SELECT NULL, m.id, g.id FROM movies m INNER JOIN genres g ON g.genre = "Horror" WHERE m.title = "The Black Phone";
INSERT INTO movies_genres SELECT NULL, m.id, g.id FROM movies m INNER JOIN genres g ON g.genre = "Thriller" WHERE m.title = "The Black Phone";
INSERT INTO movies_genres SELECT NULL, m.id, g.id FROM movies m INNER JOIN genres g ON g.genre = "Thriller" WHERE m.title = "The Little Things";
INSERT INTO movies_genres SELECT NULL, m.id, g.id FROM movies m INNER JOIN genres g ON g.genre = "Film-Noir" WHERE m.title = "The Little Things";
INSERT INTO movies_genres SELECT NULL, m.id, g.id FROM movies m INNER JOIN genres g ON g.genre = "Drama" WHERE m.title = "Memory";

INSERT OR IGNORE INTO tags_content SELECT MAX(id) + 1, "Breathtaking" FROM tags_content;
INSERT OR IGNORE INTO tags_content SELECT MAX(id) + 1, "Very detailed" FROM tags_content;
INSERT OR IGNORE INTO tags_content SELECT MAX(id) + 1, "Didn't watch actually" FROM tags_content;

INSERT INTO tags SELECT NULL, v.id, m.id, t.id, 1668339445 FROM tags INNER JOIN users v ON v.name = "Akimova Darya" INNER JOIN movies m ON m.title = "The Black Phone" INNER JOIN tags_content t ON t.tag = "Breathtaking";
INSERT INTO tags SELECT NULL, v.id, m.id, t.id, 1668340358 FROM tags INNER JOIN users v ON v.name = "Akimova Darya" INNER JOIN movies m ON m.title = "The Little Things" INNER JOIN tags_content t ON t.tag = "Very detailed";
INSERT INTO tags SELECT NULL, v.id, m.id, t.id, 1668340528 FROM tags INNER JOIN users v ON v.name = "Akimova Darya" INNER JOIN movies m ON m.title = "Memory" INNER JOIN tags_content t ON t.tag = "Didn't watch actually";
