from .db import db
import datetime
import sqlite3
import pandas as pd
# import bcrypt



#функция входа===========================
def login(login: str, passw: str):

	value = db.execute(f'''
		SELECT id_users, login, password, dol, start_day FROM users 
		WHERE login='{login}' AND password='{passw}'; 
	''').fetchone()

	

	if value:
		return {
        	'id_users': value[0],
            'login': value[1],
            'dol': value[3],
            'start_day': value[4],
        }
	raise Exception(f'Unauthorized: User with login "{login}" not found or wrong password')

#===============================================================================


def register(login, passw):
	value = db.execute(f'''
		SELECT * FROM users 
		WHERE login='{login}'; 
	''').fetchall()
	if value:
		raise Exception("User with this login already exists")

	db.execute(f"INSERT INTO users (login, password) VALUES ('{login}', '{passw}')")
	db.commit()
 
def get_all_users():  
    value = db.execute('SELECT * FROM users;').fetchall()
    return value

#=================================================================================
def start_day(login, passw):
    value = db.execute(f'''
		SELECT id_users, login, password, dol, start_day FROM users 
		WHERE login='{login}' AND password='{passw}'; 
	''').fetchone()
    
    if not value:
        raise Exception("Пользователь не найден")

    formatted_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    db.execute("UPDATE users SET start_day = ? WHERE login = ?", (formatted_time, login))
    db.commit()
#==============================================================================

def end_day(login, passw):
    value = db.execute(f'''
		SELECT id_users, login, password, dol, start_day, end_day FROM users 
		WHERE login='{login}' AND password='{passw}'; 
	''').fetchone()
    
    if not value:
        raise Exception("Пользователь не найден")

    formatted_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    db.execute("UPDATE users SET end_day = ? WHERE login = ?", (formatted_time, login))
    db.execute("UPDATE users SET end_day = ? WHERE login = ?", (formatted_time, login))
    db.commit()

#==================================================================================
def exel():
    try:
        conn = sqlite3.connect('db/time_tracking.db')
        df = pd.read_sql('SELECT * FROM users', conn)
        df.to_excel(r'd:/games/result.xlsx', index=False)
    except Exception as e:
        print(f"Произошла ошибка: {e}")
    finally:
        conn.close()
#====================================================================================

# def hash_password(passw):
#     # Генерация соли
#     salt = bcrypt.gensalt()
#     # Хэширование пароля
#     hashed_password = bcrypt.hashpw(passw.encode('utf-8'), salt)
#    return hashed_password



if __name__ == "__main__":
    user_login = "admin"  
    user_password = "admin_password"
    try:
        user = login("admin", "admin_password")
        print("Logged in user data:", user)  
        user_login = user['login']
        print("User login:", user_login)  

        
        print(f"Calling start_day with login: {user_login}")
        start_day(user_login)

    except Exception as e:  
        print(f"Error occurred: {e}")