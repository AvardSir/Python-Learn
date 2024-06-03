import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLineEdit, QLabel, QMessageBox
from PyQt5.QtWidgets import QInputDialog
import mysql.connector
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

class DatabaseApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.layout = QVBoxLayout()

        self.label = QLabel("Введите ID жителя для просмотра его друзей:")
        self.layout.addWidget(self.label)

        self.id_input = QLineEdit(self)
        self.layout.addWidget(self.id_input)

        self.view_friends_button = QPushButton('Просмотр друзей', self)
        self.view_friends_button.clicked.connect(self.view_friends)
        self.layout.addWidget(self.view_friends_button)

        self.most_friendly_button = QPushButton('Найти самого дружелюбного жителя', self)
        self.most_friendly_button.clicked.connect(self.find_most_friendly)
        self.layout.addWidget(self.most_friendly_button)

        self.group_counts_button = QPushButton('Посмотреть количество участников в каждой группе', self)
        self.group_counts_button.clicked.connect(self.find_group_member_counts)
        self.layout.addWidget(self.group_counts_button)

        self.influential_users_button = QPushButton('Найти влиятельных пользователей', self)
        self.influential_users_button.clicked.connect(self.find_influential_users)
        self.layout.addWidget(self.influential_users_button)

        self.max_weight_diff_button = QPushButton('Найти макс. разницу в весе', self)
        self.max_weight_diff_button.clicked.connect(self.find_max_weight_difference)
        self.layout.addWidget(self.max_weight_diff_button)

        self.top_5_lightest_button = QPushButton('Найти топ 5 самых худых пользователей', self)
        self.top_5_lightest_button.clicked.connect(self.find_top_5_lightest_users)
        self.layout.addWidget(self.top_5_lightest_button)

        self.top_group_creator_button = QPushButton('Найти создателя наиб. числа групп', self)
        self.top_group_creator_button.clicked.connect(self.find_top_group_creator)
        self.layout.addWidget(self.top_group_creator_button)

        self.friend_groups_button = QPushButton('Посмотреть группы друзей', self)
        self.friend_groups_button.clicked.connect(self.get_friend_groups)
        self.layout.addWidget(self.friend_groups_button)

        self.messages_button = QPushButton('Посмотреть сообщения', self)
        self.messages_button.clicked.connect(self.get_messages)
        self.layout.addWidget(self.messages_button)

        # Новые кнопки для графиков
        self.view_friends_chart_button = QPushButton('График количества друзей', self)
        self.view_friends_chart_button.clicked.connect(self.view_friends_chart)
        self.layout.addWidget(self.view_friends_chart_button)

        self.view_group_counts_chart_button = QPushButton('График количества участников в группах', self)
        self.view_group_counts_chart_button.clicked.connect(self.view_group_counts_chart)
        self.layout.addWidget(self.view_group_counts_chart_button)

        self.view_weight_distribution_chart_button = QPushButton('График распределения весов', self)
        self.view_weight_distribution_chart_button.clicked.connect(self.view_weight_distribution_chart)
        self.layout.addWidget(self.view_weight_distribution_chart_button)

        self.view_top_messages_chart_button = QPushButton('График топ n пользователей по сообщениям', self)
        self.view_top_messages_chart_button.clicked.connect(self.view_top_messages_chart)
        self.layout.addWidget(self.view_top_messages_chart_button)

        self.setLayout(self.layout)
        self.setWindowTitle('Database App')
        self.setGeometry(300, 300, 400, 600)

    def execute_procedure(self, procedure_name, args=()):
        try:
            connection = mysql.connector.connect(
                host='localhost',
                database='марк_3',
                user='root',
                password=''
            )
            cursor = connection.cursor()
            cursor.callproc(procedure_name, args)
            for result in cursor.stored_results():
                return result.fetchall()
        except mysql.connector.Error as err:
            QMessageBox.critical(self, 'Database Error', f"Error: {err}")
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()

    def view_friends(self):
        resident_id = self.id_input.text()
        if not resident_id.isdigit():
            QMessageBox.warning(self, 'Input Error', 'Please enter a valid ID')
            return
        results = self.execute_procedure('GetFriends', (resident_id,))
        if results:
            friends = "\n".join([str(row) for row in results])
            QMessageBox.information(self, 'Friends', f"Friends of resident {resident_id}:\n{friends}")

    def find_most_friendly(self):
        results = self.execute_procedure('FindMostFriendlyResident')
        if results:
            most_friendly = "\n".join([str(row) for row in results])
            QMessageBox.information(self, 'Most Friendly Resident', f"Most Friendly Resident:\n{most_friendly}")

    def find_group_member_counts(self):
        results = self.execute_procedure('FindGroupMemberCounts')
        if results:
            counts = "\n".join([str(row) for row in results])
            QMessageBox.information(self, 'Group Counts', f"Group counts:\n{counts}")

    def find_influential_users(self):
        results = self.execute_procedure('FindInfluentialUsers')
        if results:
            influential_users = "\n".join([str(row) for row in results])
            QMessageBox.information(self, 'Influential Users', f"Influential users:\n{influential_users}")

    def find_max_weight_difference(self):
        results = self.execute_procedure('FindMaxWeightDifference')
        if results:
            max_weight_diff = "\n".join([str(row) for row in results])
            QMessageBox.information(self, 'Max Weight Difference', f"Max weight difference:\n{max_weight_diff}")

    def find_top_5_lightest_users(self):
        results = self.execute_procedure('FindTop5LightestUsers')
        if results:
            top_5_lightest = "\n".join([str(row) for row in results])
            QMessageBox.information(self, 'Top 5 Lightest Users', f"Top 5 lightest users:\n{top_5_lightest}")

    def find_top_group_creator(self):
        results = self.execute_procedure('FindTopGroupCreator')
        if results:
            top_group_creator = "\n".join([str(row) for row in results])
            QMessageBox.information(self, 'Top Group Creator', f"Top group creator:\n{top_group_creator}")

    def get_friend_groups(self):
        resident_id = self.id_input.text()
        if not resident_id.isdigit():
            QMessageBox.warning(self, 'Input Error', 'Please enter a valid ID')
            return
        results = self.execute_procedure('GetFriendGroups', (resident_id,))
        if results:
            friend_groups = "\n".join([str(row) for row in results])
            QMessageBox.information(self, 'Friend Groups', f"Friend groups of resident {resident_id}:\n{friend_groups}")

    def get_messages(self):
        results = self.execute_procedure('GetMessages')
        if results:
            messages = "\n".join([str(row) for row in results])
            QMessageBox.information(self, 'Messages', f"Messages:\n{messages}")

    # Функции для отображения графиков
    def view_friends_chart(self):
        conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='марк_3'
        )

        query_friends = """
        SELECT 
            a.`idАнкета`,
            a.`ФИО`,
            COUNT(d.`Друг`) AS Количество_друзей
        FROM 
            `марк_3`.`друзья` d
        JOIN 
            `марк_3`.`анкета` a ON d.`Кому_друг` = a.`idАнкета` OR d.`Друг` = a.`idАнкета`
        GROUP BY 
            a.`idАнкета`, a.`ФИО`
        ORDER BY 
            Количество_друзей DESC;
        """
        df_friends = pd.read_sql(query_friends, conn)
        conn.close()

        plt.figure(figsize=(10, 6))
        plt.bar(df_friends['ФИО'], df_friends['Количество_друзей'], color='skyblue')
        plt.xlabel('ФИО')
        plt.ylabel('Количество друзей')
        plt.title('Количество друзей каждого жителя')
        plt.xticks(rotation=90)
        plt.tight_layout()
        plt.show()

    def view_group_counts_chart(self):
        conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='марк_3'
        ) 

        query_groups = """
        SELECT 
            g.`Название`, 
            COUNT(gr.`Кто_подписан`) AS Количество_участников
        FROM 
            `марк_3`.`группы` gr
        JOIN 
            `марк_3`.`группа` g ON gr.`Группа` = g.`idГруппа`
        GROUP BY 
            g.`Название`
        ORDER BY 
            Количество_участников DESC;
        """
        df_groups = pd.read_sql(query_groups, conn)
        conn.close()

        plt.figure(figsize=(10, 6))
        plt.pie(df_groups['Количество_участников'], labels=df_groups['Название'], autopct='%1.1f%%', startangle=140)
        plt.title('Распределение участников по группам')
        plt.show()

    def view_weight_distribution_chart(self):
        conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='марк_3'
        )

        query_weight = """
        SELECT 
            a.`idАнкета`,
            a.`ФИО`,
            a.`ВЕС`
        FROM 
            `марк_3`.`анкета` a
        ORDER BY 
            a.`ВЕС` ASC;
        """
        df_weight = pd.read_sql(query_weight, conn)
        conn.close()

        plt.figure(figsize=(10, 6))
        plt.hist(df_weight['ВЕС'], bins=100, color='green', edgecolor='black')
        plt.xlabel('Вес')
        plt.ylabel('Частота')
        plt.title('Распределение весов жителей')
        plt.tight_layout()
        plt.show()

    def view_top_messages_chart(self):
        n, ok = QInputDialog.getInt(self, 'Input Dialog', 'Введите количество пользователей для отображения:')
        if not ok:
            return

        conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='марк_3'
        )

        query_messages = f"""
        SELECT 
            a.`idАнкета`,
            a.`ФИО`,
            COUNT(m.`idСообщения`) AS Количество_сообщений
        FROM 
            `марк_3`.`сообщения` m
        JOIN 
            `марк_3`.`анкета` a ON m.`Кто` = a.`idАнкета`
        GROUP BY 
            a.`idАнкета`, a.`ФИО`
        ORDER BY 
            Количество_сообщений DESC
        LIMIT {n};
        """
        df_messages = pd.read_sql(query_messages, conn)
        conn.close()

        plt.figure(figsize=(10, 6))
        plt.bar(df_messages['ФИО'], df_messages['Количество_сообщений'], color='purple')
        plt.xlabel('ФИО')
        plt.ylabel('Количество сообщений')
        plt.title(f'Топ {n} пользователей по количеству сообщений')
        plt.xticks(rotation=90)
        plt.tight_layout()
        plt.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = DatabaseApp()
    ex.show()
    sys.exit(app.exec_())
