import mysql.connector
import pandas as pd
import matplotlib.pyplot as plt

# Подключение к базе данных
conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='марк_3'
)

# Выполнение запроса для получения данных о друзьях
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

# Выполнение запроса для получения данных о группах
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

# Выполнение запроса для получения данных о весе
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

# Закрытие соединения с базой данных
conn.close()

# Визуализация данных

# 1. График количества друзей
plt.figure(figsize=(10, 6))
plt.bar(df_friends['ФИО'], df_friends['Количество_друзей'], color='skyblue')
plt.xlabel('ФИО')
plt.ylabel('Количество друзей')
plt.title('Количество друзей каждого жителя')
plt.xticks(rotation=90)
plt.tight_layout()

# 2. График количества участников в группах
plt.figure(figsize=(10, 6))
plt.pie(df_groups['Количество_участников'], labels=df_groups['Название'], autopct='%1.1f%%', startangle=140)
plt.title('Распределение участников по группам')

# 3. Гистограмма распределения весов жителей
plt.figure(figsize=(10, 6))
plt.hist(df_weight['ВЕС'], bins=100, color='green', edgecolor='black')
plt.xlabel('Вес')
plt.ylabel('Частота')
plt.title('Распределение весов жителей')
plt.tight_layout()


def get_top_n_users_by_messages(n):
    # Подключение к базе данных
    conn = mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='марк_3'
    )

    # Выполнение запроса для получения данных о количестве сообщений
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

    # Закрытие соединения с базой данных
    conn.close()

    return df_messages


# Количество пользователей для отображения
n = 4

# Получение данных для топ n пользователей по количеству сообщений
df_messages = get_top_n_users_by_messages(n)
# 4. График топ n пользователей по количеству сообщений
plt.figure(figsize=(10, 6))
plt.bar(df_messages['ФИО'], df_messages['Количество_сообщений'], color='purple')
plt.xlabel('ФИО')
plt.ylabel('Количество сообщений')
plt.title(f'Топ {n} пользователей по количеству сообщений')
plt.xticks(rotation=90)
plt.tight_layout()
# Показать графики
plt.show()