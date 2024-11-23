import sqlite3

# Укажите путь для сохранения базы данных
db_path = "movies_database_extended_v2.db"  # Файл будет создан в текущей папке проекта

# Подключение или создание базы данных
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Создание таблицы фильмов
cursor.execute("""
CREATE TABLE IF NOT EXISTS movies (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    year INTEGER,
    genre TEXT,
    director TEXT,
    rating FLOAT,
    box_office INTEGER
)
""")

# Расширенный список фильмов
movies_data = [
    ("The Shawshank Redemption", 1994, "Drama", "Frank Darabont", 9.3, 28341469),
    ("The Godfather", 1972, "Crime", "Francis Ford Coppola", 9.2, 134966411),
    ("The Dark Knight", 2008, "Action", "Christopher Nolan", 9.0, 1004558444),
    ("Inception", 2010, "Sci-Fi", "Christopher Nolan", 8.8, 836848102),
    ("Forrest Gump", 1994, "Romance", "Robert Zemeckis", 8.8, 678222284),
    ("The Matrix", 1999, "Sci-Fi", "Lana Wachowski, Lilly Wachowski", 8.7, 466364845),
    ("Interstellar", 2014, "Sci-Fi", "Christopher Nolan", 8.6, 677471339),
    ("Parasite", 2019, "Thriller", "Bong Joon Ho", 8.5, 263117249),
    ("Whiplash", 2014, "Drama", "Damien Chazelle", 8.5, 133329998),
    ("The Lion King", 1994, "Animation", "Roger Allers, Rob Minkoff", 8.5, 968511805),
    ("Joker", 2019, "Crime", "Todd Phillips", 8.4, 1074251311),
    ("Avengers: Endgame", 2019, "Action", "Anthony Russo, Joe Russo", 8.4, 2797501328),
    ("Toy Story", 1995, "Animation", "John Lasseter", 8.3, 373554033),
    ("Spider-Man: No Way Home", 2021, "Action", "Jon Watts", 8.3, 1921649637),
    ("Dune", 2021, "Sci-Fi", "Denis Villeneuve", 8.2, 400671789),
    ("No Time to Die", 2021, "Action", "Cary Joji Fukunaga", 7.8, 774153007),
    ("Encanto", 2021, "Animation", "Byron Howard, Jared Bush", 7.6, 256786742),
    ("The Batman", 2022, "Action", "Matt Reeves", 8.1, 770837849),
    ("The Green Mile", 1999, "Drama", "Frank Darabont", 8.6, 286801374),
    ("Pulp Fiction", 1994, "Crime", "Quentin Tarantino", 8.9, 213928762),
    ("Saving Private Ryan", 1998, "War", "Steven Spielberg", 8.6, 482349603),
    ("Gladiator", 2000, "Action", "Ridley Scott", 8.5, 460583960),
    ("The Wolf of Wall Street", 2013, "Biography", "Martin Scorsese", 8.2, 392000694),
    ("Titanic", 1997, "Romance", "James Cameron", 7.9, 2187463944),
    ("Avatar", 2009, "Sci-Fi", "James Cameron", 7.9, 2847246203),
    ("Frozen", 2013, "Animation", "Chris Buck, Jennifer Lee", 7.4, 1280802282),
    ("Black Panther", 2018, "Action", "Ryan Coogler", 7.3, 1346913161),
    ("The Avengers", 2012, "Action", "Joss Whedon", 8.0, 1518812988),
    ("The Hunger Games", 2012, "Adventure", "Gary Ross", 7.2, 694394724),
    ("Shrek", 2001, "Animation", "Andrew Adamson, Vicky Jenson", 7.9, 487853320),
    ("The Social Network", 2010, "Biography", "David Fincher", 7.8, 224920315),
    ("The Grand Budapest Hotel", 2014, "Comedy", "Wes Anderson", 8.1, 173082836),
    ("The Revenant", 2015, "Adventure", "Alejandro G. Iñárritu", 8.0, 533000000),
    ("Mad Max: Fury Road", 2015, "Action", "George Miller", 8.1, 374736354),
    ("La La Land", 2016, "Musical", "Damien Chazelle", 8.0, 447407695),
    ("Harry Potter and the Sorcerer's Stone", 2001, "Fantasy", "Chris Columbus", 7.6, 974755371),
    ("Star Wars: The Force Awakens", 2015, "Sci-Fi", "J.J. Abrams", 7.9, 2068223624),
    ("The Lord of the Rings: The Fellowship of the Ring", 2001, "Adventure", "Peter Jackson", 8.8, 897690072),
    ("The Lord of the Rings: The Two Towers", 2002, "Adventure", "Peter Jackson", 8.7, 951227416),
    ("The Lord of the Rings: The Return of the King", 2003, "Adventure", "Peter Jackson", 8.9, 1146030912)
]

# Вставка данных в таблицу
cursor.executemany("""
INSERT INTO movies (title, year, genre, director, rating, box_office)
VALUES (?, ?, ?, ?, ?, ?)
""", movies_data)

# Сохранение изменений
conn.commit()
conn.close()

print(f"Расширенная база данных создана: '{db_path}'")
