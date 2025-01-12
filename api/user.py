from .db import db
import datetime

# Получаем текущее время
current_time = datetime.datetime.now()
formatted_time = current_time.strftime('%Y-%m-%d %H:%M:%S')

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
	raise Exception('Unauthorized')
    

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
def start_day(login):
    print(f"Ищем пользователя с логином: {login}")  
    value = db.execute('SELECT * FROM users WHERE login = ?', (login,)).fetchone()
    
    if not value:
        raise Exception("Пользователь не найден")
    
   
    formatted_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    db.execute("UPDATE users SET start_day = ? WHERE login = ?", (formatted_time, login))
    db.commit()

#==============================================================================
if __name__ == "__main__":
    try:
        register("admin", "admin_password")
    except Exception as e:
        print("Registration error:", e)

try:
        
        user = login("admin", "admin_password")  
        
        
        user_login = user['login']
        
        
        start_day(user_login)  
        print("Start day updated for admin.")
        
except Exception as e:
        print("Error:", e)