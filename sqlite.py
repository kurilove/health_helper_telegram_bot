import sqlite3 as sq


async def db_start():
    global db, cursor

    db = sq.connect("profiles.db")
    cursor = db.cursor()

    # cursor.execute("""DROP TABLE profile""")

    cursor.execute(
        "CREATE TABLE IF NOT EXISTS profile(user_id TEXT PRIMARY KEY,username TEXT,name TEXT,surname TEXT,age TEXT ,sub INTEGER DEFAULT 0,calory TEXT DEFAULT 'Не определено')")

    db.commit()


async def create_profile(user_id):
    cursor.execute(f"INSERT INTO profile  (user_id) VALUES({user_id})")
    db.commit()


async def edit_profile(state, user_id):
    async with state.proxy() as data:
        print(data['username'])
        # cursor.execute("DELETE FROM profile WHERE rowid = 1")
        cursor.execute(
            f"""UPDATE profile SET username = '{data['username']}', name = '{data['name']}', surname = '{data['surname']}',age = '{data['age']}' , calory = '{data['calory']}' WHERE user_id LIKE {user_id} """)

        db.commit()


async def get_profile(user_id):
    print("get_profile")

    cursor.execute(f"""
        SELECT name, surname, age, calory,sub FROM profile WHERE user_id = {user_id}
        """)

    value = cursor.fetchall()
    values = value[0]
    name = values[0]
    surname = values[1]
    age = values[2]
    calory = float(values[3])
    sub = values[4]

    if sub == 0:
        sub_text = "Подписка не активирована"
    else:
        sub_text = "Подписка активна"

    message = f"""<b>
Вот твой профиль:
Ваше имя: {name} 
Ваша фамилия: {surname} 
Ваш возраст: {age} 
Базовый обмен: {round(calory)} калорий

Состояние подписки:
{sub_text}</b>

    """

    return message
