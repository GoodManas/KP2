import sys
import os
from PySide6 import QtWidgets
from PySide6.QtWidgets import QApplication, QMainWindow, QDialog
from PySide6.QtWidgets import QMessageBox
from PySide6.QtGui import QStandardItemModel, QStandardItem


# Ваши импорты для CheckThread и Ui_MainWindow
from ui.ui_main import Ui_MainWindow
from ui.ui_Admin2 import Ui_Admin
from ui.rabotnok import UI_rabotnik
from ui.manager import Ui_manager
from api.user import login, register, get_all_users, start_day, end_day


def check_input(funct):
    def wrapper(self):
        for line_edit in self.base_lane_edit:
            if len(line_edit.text()) == 0: 
                return
        return funct(self)
    return wrapper

class Register(QMainWindow):
    def __init__(self):
        super(Register, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui_admin = Ui_Admin()
        self.ui.setupUi(self)
        
        self.ui.btn_login.clicked.connect(self.auth)
        self.ui.btn_register.clicked.connect(self.reg)
        
       
        self.base_lane_edit = [self.ui.lineEditLog, self.ui.lineEditPass]
        
    #авторизация и открытие окна 
    @check_input
        
    def auth(self):
        name = self.ui.lineEditLog.text()
        passw = self.ui.lineEditPass.text()
        
        try:
            user = login(name, passw)  
            print(user)
            
            position_id = user['dol']  
        
            
                    
            if position_id == 1:  # Например, 1 - это ID для администратора
                self.open_ui_admin()
            elif position_id == 2:  # 2 - это ID для работника
                self.open_ui_rabotnik()
            elif position_id == 3:  # 3 - это ID для менеджера
                self.open_ui_manager()
            else:
                QMessageBox.warning(self, "Ошибка", "Неизвестная должность")
    
        except Exception as e:
            print("Error occurred:", str(e))
            QMessageBox.warning(self, "Ошибка", str(e))
        
        
    
    
    #окно с админом =================================================================
    def open_ui_admin(self):
        print('открылось окно с админомм')
        
        dialog = QDialog(self)  # Создаем экземпляр QDialog
        self.dialog = Ui_Admin()  # Создаем экземпляр Ui_Dialog
        self.dialog.setupUi(dialog)  # Настраиваем интерфейс диалога
       
        #подключение Кнопок в ui админ 
        self.dialog.btn_end.clicked.connect(self.end)
        self.dialog.btn_otchet.clicked.connect(self.show_users)
        self.dialog.btn_start_day.clicked.connect(self.Startt_day)
        self.dialog.btn_end_day.clicked.connect(self.Endd_day)
        
        self.base_lane_edit = [self.ui.lineEditLog, self.ui.lineEditPass]
     
        
        dialog.exec() 
        
        #=============================================================================
        #Функция для показа отчета admin
    def show_users(self):
       
        users = get_all_users()
        
        #модель для QTableView
        model = QStandardItemModel(len(users), 6)  # Измените количество столбцов в соответствии с вашей таблицей
        model.setHorizontalHeaderLabels(["id", "login", "password", "dol", "start_day", "end_day"])  # Замените на ваши реальные названия столбцов
        
        for row_idx, row_data in enumerate(users):
            for col_idx, item in enumerate(row_data):
                model.setItem(row_idx, col_idx, QStandardItem(str(item)))  
        
        self.dialog.tableView.setModel(model)
        
    # #окно с рабом =================================================================
    
    def open_ui_rabotnik(self):
        rab = QDialog(self)
        self.rab =  UI_rabotnik()
        self.rab.setupUi(rab) 
        
        self.rab.btn_end.clicked.connect(self.end)
        
        rab.exec()
    
    
    #окно с менеджером =================================================================
    
    def open_ui_manager(self):
        manager = QDialog(self)
        self.manager =  Ui_manager()
        self.manager.setupUi(manager)    
        
        
        self.manager.btn_end.clicked.connect(self.end)# кнопка закрыть приложение 
        self.manager.btn_otchet.clicked.connect(self.show_users_manager)#кнопка отчет
        self.manager.btn_start_day.clicked.connect(self.Startt_day)
        self.manager.btn_end.clicked.connect(self.Endd_day)
        self.base_lane_edit = [self.ui.lineEditLog, self.ui.lineEditPass]
        
        manager.exec()
        
       
        
       # =================================================================
       # Функция для работы с QTableView из ui мэнеджер
    def show_users_manager(self):
        
        users = get_all_users()
        
        # модель для QTableView
        model = QStandardItemModel(len(users), 6)  # Измените количество столбцов в соответствии с вашей таблицей
        model.setHorizontalHeaderLabels(["id", "login", "password"])  # Замените на ваши реальные названия столбцов
        
        for row_idx, row_data in enumerate(users):
            for col_idx, item in enumerate(row_data):
                model.setItem(row_idx, col_idx, QStandardItem(str(item)))  
        
        self.manager.tableView.setModel(model)
        
    #====================================================================
    #регистрация
    
    @check_input 
    def reg(self):
        name = self.ui.lineEditLog.text()
        passw = self.ui.lineEditPass.text()
        register(name, passw)
        print('Autor')
        

    #====================================================================    
    #функция для закрытия окна 
    def end(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        self.close()
        
        
        
   #=====================================================================
   
   
    def Startt_day(self):
        name = self.ui.lineEditLog.text()
        passw = self.ui.lineEditPass.text()
        start_day(name, passw)

    #=====================================================================
    
    def Endd_day(self):
        name = self.ui.lineEditLog.text()
        passw = self.ui.lineEditPass.text()
        end_day(name, passw)
        
    #=====================================================================
        
        
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Register()
    window.show()   
    sys.exit(app.exec())