import telebot
import sqlite3

# Вставьте ваш токен от BotFather
TOKEN = "8086671611:AAEbJz5DCiFRtK-cH-g0DtKY54n_0KeDbEo"
bot = telebot.TeleBot(TOKEN)

# Путь к базе данных
DB_PATH = "movies_database_extended.db"

# Команда /start
@bot.message_handler(commands=['start'])
def start_command(message):
    bot.send_message(
        message.chat.id,
        "👋 Привет! Я профессиональный бот для анализа фильмов. Вот что я умею: \n\n"
        "Введите /help, чтобы увидеть доступные команды."
    )

# Команда /help
@bot.message_handler(commands=['help'])
def help_command(message):
    help_text = (
        "📚 *Доступные команды:*\n\n"
        "🎬 /all_movies - Показать все фильмы\n"
        "🔍 /find_movie <название> - Найти фильм по названию\n"
        "⭐ /popular_movie - Показать самый популярный фильм\n"
        "🎭 /movies_by_genre <жанр> - Найти фильмы по жанру\n"
        "📅 /movies_by_year <год> - Найти фильмы по году\n"
        "➕ /add_movie <название>,<год>,<жанр>,<режиссёр>,<рейтинг>,<сборы> - Добавить новый фильм"
    )
    bot.send_message(message.chat.id, help_text, parse_mode="Markdown")

# Команда /popular_movie
@bot.message_handler(commands=['popular_movie'])
def popular_movie_command(message):
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute("SELECT title, rating FROM movies ORDER BY rating DESC LIMIT 1")
        movie = cursor.fetchone()
        conn.close()

        if movie:
            response = f"⭐ Самый популярный фильм: *{movie[0]}* с рейтингом _{movie[1]}_"
        else:
            response = "Не удалось найти популярный фильм."
    except Exception as e:
        response = f"⚠️ Ошибка при работе с базой данных: {e}"

    bot.send_message(message.chat.id, response, parse_mode="Markdown")

# Команда /movies_by_genre
@bot.message_handler(commands=['movies_by_genre'])
def movies_by_genre_command(message):
    try:
        genre = message.text[len("/movies_by_genre "):].strip()
        if not genre:
            bot.send_message(
                message.chat.id,
                "🎭 Пожалуйста, укажите жанр после команды /movies_by_genre.\nНапример: /movies_by_genre Drama"
            )
            return

        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute("SELECT title, year, rating FROM movies WHERE genre LIKE ?", (f"%{genre}%",))
        movies = cursor.fetchall()
        conn.close()

        if movies:
            response = f"🎥 *Фильмы жанра {genre}:*\n" + "\n".join(
                [f"• {title} ({year}) - ⭐ {rating}" for title, year, rating in movies]
            )
        else:
            response = f"❌ Фильмы жанра '{genre}' не найдены."
    except Exception as e:
        response = f"⚠️ Ошибка при работе с базой данных: {e}"

    bot.send_message(message.chat.id, response, parse_mode="Markdown")

# Команда /movies_by_year
@bot.message_handler(commands=['movies_by_year'])
def movies_by_year_command(message):
    try:
        year = message.text[len("/movies_by_year "):].strip()
        if not year.isdigit():
            bot.send_message(message.chat.id, "📅 Укажите корректный год после команды /movies_by_year.\nНапример: /movies_by_year 1994")
            return

        year = int(year)
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute("SELECT title, genre, rating FROM movies WHERE year = ?", (year,))
        movies = cursor.fetchall()
        conn.close()

        if movies:
            response = f"📅 *Фильмы {year} года:*\n" + "\n".join(
                [f"• {title} - {genre}, ⭐ {rating}" for title, genre, rating in movies]
            )
        else:
            response = f"❌ Фильмы {year} года не найдены."
    except Exception as e:
        response = f"⚠️ Ошибка при работе с базой данных: {e}"

    bot.send_message(message.chat.id, response, parse_mode="Markdown")

# Запуск бота
bot.polling()
