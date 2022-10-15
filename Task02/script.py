import pandas as pd
import datetime
import sqlite3
import re

# try:
#   connect = sqlite3.connect("movies_rating.db")
# except:
#   print("movies_rating.db is exist")

sqlFile = open("db_init.sql", "w",encoding='utf-8')

sqlFile.writelines(
    [
        "drop table if exists movies;\n",
        "drop table if exists ratings;\n",
        "drop table if exists tags;\n",
        "drop table if exists users;\n",

        """
create table movies
(
    id integer(8) primary key,
    title  varchar(255),
    year int,
    genres varchar(255)
);
        """,

        """
create table ratings
(
    id integer primary key autoincrement,
    user_id  int,
    movie_id  int,
    rating    int,
    timestamp int
);
        """,

        """
create table tags
(
    id integer primary key autoincrement,
    user_id int,
    movie_id int,
    tag varchar(255),
    timestamp int
);
        """,

        """
create table users
(
    id integer primary key,
    name varchar(255),
    email varchar(255),
    gender varchar(255),
    register_date date,
    occupation varchar(255)
);
        """

    ]

)

# movies table
with open("movies.csv", encoding='utf-8') as file:
    lines = pd.read_csv(file)
    insert_str = "insert into movies values \n "
    for i in range(lines.shape[0]):
        if (i < lines.shape[0] - 1):
            if lines.iloc[i,0] == 7789:
                insert_str += "(" + str(lines.iloc[i, 0]) + ",\"" + "11'09'01 - September 11" + "\"," + str(
                    (str(lines.iloc[i, 1])[(len(str(lines.iloc[i, 1])) - 6):]))[1:5] + ",\"" + str(
                    lines.iloc[i, 2]) + "\"), \n"
            # elif lines.iloc[i, 0] == 58404:
            #     insert_str += "(" + str(lines.iloc[i, 0]) + ",\"" + (str(lines.iloc[i, 1])[:-7]).strip() + "\"," + str(2008) + ",\"" + str(
            #         lines.iloc[i, 2]) + "\"), \n"
            # elif lines.iloc[i, 0] == 58842:
            #     insert_str += "(" + str(lines.iloc[i, 0]) + ",\"" + (str(lines.iloc[i, 1])[:-7]).strip() + "\"," + str(2007) + ",\"" + str(
            #         lines.iloc[i, 2]) + "\"), \n"
            # elif lines.iloc[i, 0] == 27008:
            #     insert_str += "(" + str(lines.iloc[i, 0]) + ",\"" + (str(lines.iloc[i, 1])[:-7]).strip() + "\"," + str(
            #         1999) + ",\"" + str(
            #         lines.iloc[i, 2]) + "\"), \n"
            # elif lines.iloc[i, 0] == 94494:
            #     insert_str += "(" + str(lines.iloc[i, 0]) + ",\"" + (str(lines.iloc[i, 1])[:-7]).strip() + "\"," + str(2011) + ",\"" + str(
            #         lines.iloc[i, 2]) + "\"), \n"
            # elif lines.iloc[i, 0] == 95004:
            #     insert_str += "(" + str(lines.iloc[i, 0]) + ",\"" + (str(lines.iloc[i, 1])[:-7]).strip() + "\"," + str(2007) + ",\"" + str(
            #         lines.iloc[i, 2]) + "\"), \n"
            # else:
            # elif (lines.iloc[i, 0] == 140956) or (lines.iloc[i, 0] == 167570) or (lines.iloc[i,0] == 176601) or (lines.iloc[i,0] == 171891) or (lines.iloc[i,0] == 171631):
            #     insert_str += "(" + str(lines.iloc[i, 0]) + ",\"" + str(lines.iloc[i, 1]) + "\"," + "NULL" + ",\"" + str(
            #         lines.iloc[i, 2]) + "\"), \n"
            else:
                titleyear = str(lines.iloc[i, 1])
                titleyear = titleyear.strip()
                if re.search(r"(\d\d\d\d)", titleyear):
                    year = titleyear[len(titleyear) - 5:]
                    year = year[:4]
                    title = titleyear[0:len(titleyear) - 6]
                    title = title.strip()
                    insert_str += "(" + str(lines.iloc[i, 0]) + ",\"" + title + "\"," + year + ",\"" + str(lines.iloc[i, 2]) + "\"), \n"
                else:
                    insert_str += "(" + str(lines.iloc[i, 0]) + ",\"" + str(
                        lines.iloc[i, 1]) + "\"," + "NULL" + ",\"" + str(
                             lines.iloc[i, 2]) + "\"), \n"
        elif i == lines.shape[0] - 1:
            insert_str += "(" + str(lines.iloc[i, 0]) + ",\"" + (str(lines.iloc[i, 1])[:-7]).strip() + "\"," + str((str(lines.iloc[1, 1])[(len(str(lines.iloc[1, 1])) - 6):]))[1:5] + ",\"" + str(lines.iloc[i, 2]) + "\"); \n"
    insert_str += "\n \n"
    sqlFile.writelines(insert_str)

with open("ratings.csv", encoding='utf-8') as file:
    lines = pd.read_csv(file)
    insert_str = "insert into ratings values \n"

    for i in range(lines.shape[0]):
        if (i > 0) and (i < lines.shape[0] - 1):
            insert_str += "(" + "NULL," + str(lines.iloc[i, 0]) + "," + str(lines.iloc[i, 1]) + "," + str(lines.iloc[i, 2]) + "," + str(lines.iloc[i, 3]) + "), \n"
        elif i == lines.shape[0] - 1:
            insert_str += "(" + "NULL," + str(lines.iloc[i, 0]) + "," + str(lines.iloc[i, 1]) + "," + str(lines.iloc[i, 2]) + "," + str(lines.iloc[i, 3]) + "); \n"
    insert_str += "\n \n"
    sqlFile.writelines(insert_str)

with open("tags.csv", encoding='utf-8') as file:
    lines = pd.read_csv(file)
    insert_str = "insert into tags values \n"

    for i in range(lines.shape[0]):
        if i < lines.shape[0] - 1:
            insert_str += "(" + "NULL," + str(lines.iloc[i, 0]) + "," + str(lines.iloc[i, 1]) + ",\"" + (str(lines.iloc[i, 2])).strip("\"") + "\"," + str(lines.iloc[i, 3]) + "), \n"
        elif i == lines.shape[0] - 1:
            insert_str += "(" + "NULL," + str(lines.iloc[i, 0]) + "," + str(lines.iloc[i, 1]) + ",\"" + (str(lines.iloc[i, 2])).strip("\"") + "\"," + str(lines.iloc[i, 3]) + "); \n"
    insert_str += "\n \n"
    sqlFile.writelines(insert_str)

with open("users.txt", encoding='utf-8') as file:
    lines = pd.read_csv(file, sep="|")
    insert_str = "insert into users values \n"

    for i in range(lines.shape[0]):
        if i < lines.shape[0] - 1:
            insert_str += "(" + str(lines.iloc[i, 0]) + ",\"" + str(lines.iloc[i, 1]) + "\",\"" + str(lines.iloc[i, 2]) + "\",\"" + str(lines.iloc[i, 3]) + "\"," + str(lines.iloc[i, 4]) + ",\"" + str(lines.iloc[i, 5]) + "\"), \n"
        elif i == lines.shape[0] - 1:
            insert_str += "(" + str(lines.iloc[i, 0]) + ",\"" + str(lines.iloc[i, 1]) + "\",\"" + str(lines.iloc[i, 2]) + "\",\"" + str(lines.iloc[i, 3]) + "\"," + str(lines.iloc[i, 4]) + ",\"" + str(lines.iloc[i, 5]) + "\"); \n"
    insert_str += "\n \n"
    sqlFile.writelines(insert_str)


    #         insert_str += "("
    # for j in range(lines.shape[1]):

    # if j < (lines.shape[1] - 1):
    #     insert_str += str(lines.iloc[i, j]) + ","
    # else:
    #     insert_str += str(lines.iloc[i, j])
    # if (j != lines.shape[1] - 1) and (i != lines.shape[0] - 1):
    #     insert_str += "), \n"
    # else:
    #     insert_str += ");"
    # sqlFile.writelines(insert_str)

# for i in range(len(lines)):
#    line = []
#   for field in fields:
#       line.append(lines[field][i])

#     content = []

#      for elem in line:
#           try:
#               float(elem)
#              content.append("\t" + str(elem))
#          except:
#               elem = elem.replace("'", "")
#               elem = elem.replace(""", "")
#               content.append("\t'" + str(elem) + "'")

#        line = ",\n".join(content)

#       insert = """
# insert into %(table_name)s values (
# %(line)s
# );
#                """ % {
#           "line": line,
