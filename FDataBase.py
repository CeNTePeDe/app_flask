import math, time
import sqlite3


class FDataBase:
    def __init__(self, db):
        self.__db = db
        self.__cur = db.cursor()

    def getMenu(self):
        sql = """ SELECT * FROM mainmenu """
        try:
            self.__cur.execute(sql)
            res = self.__cur.fetchall()
            if res: return res
        except:
            print('ошибка чтения ДБ')
        return []

    def addPost(self, title, text):
        try:
            tm = math.floor(time.time())
            self.__cur.execute("INSERT INTO posts VALUES (NULL, ?,?,?)", (title, text, tm))
            self.__db.commit()
        except sqlite3.Error as r:
            print('Ощибка добавления статьи в БД'+str(r))
            return False
        return True

    def getPost(self, post_id):
        try:
            self.__cur.execute(f"SELECT title, text FROM posts WHERE id = {post_id} LIMIT 1")
            res = self.__cur.fetchone()
            if res:
                return res
        except sqlite3.Error as r:
            print('Ощибка добавления статьи в БД' + str(r))
        return (False, False)

    def getPostsAnonce(self):

        try:
            self.__cur.execute(f'SELECT id, title, text FROM posts ORDER BY time DESC')
            res = self.__cur.fetchall()
            if res: return res
        except sqlite3.Error as r:
            print('Ощибка добавления статьи в БД' + str(r))
        return []
