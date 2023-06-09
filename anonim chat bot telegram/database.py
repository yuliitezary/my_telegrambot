import sqlite3


class dbworker:
    def __init__(self,database_file):
        self.connection = sqlite3.connect(database_file)
        self.cursor = self.connection.cursor()

    def user_exists(self, user_id):
        with self.connection:
            result = self.cursor.execute('SELECT * FROM `users` WHERE `telegram_id` = ?', (user_id,)).fetchall()
            return bool(len(result))

    def add_user(self,telegram_username,telegram_id):
    	with self.connection:
    		return self.cursor.execute("INSERT INTO `users` (`telegram_username`, `telegram_id`) VALUES(?,?)", (telegram_username,telegram_id))

    def edit_sex(self,sex,telegram_id):
    	with self.connection:
    		self.cursor.execute('UPDATE `users` SET `sex` = ? WHERE `telegram_id` = ?',(sex,telegram_id))

    def search(self,sex):
        with self.connection:
            search = self.cursor.execute('SELECT `telegram_id` FROM `queue` WHERE `sex` = ?',(str(sex))).fetchone()
            return search

    def get_sex_user(self,telegram_id):
        with self.connection:
            result = self.cursor.execute('SELECT `sex` FROM `users` WHERE `telegram_id` = ?',(telegram_id,)).fetchone()
            return result

    def add_to_queue(self,telegram_id,sex):
        with self.connection:
            if sex == 1:
                sex = bool(0)
            else:
                sex = bool(1)
            self.cursor.execute("INSERT INTO `queue` (`telegram_id`, `sex`) VALUES(?,?)", (telegram_id,sex))

    def delete_from_queue(self, telegram_id):
        with self.connection:
            self.cursor.execute('DELETE FROM `queue` WHERE `telegram_id` = ?',(telegram_id,))

    def update_connect_with(self,connect_with,telegram_id):
        with self.connection:
            self.cursor.execute('UPDATE `users` SET `connect_with` = ? WHERE `telegram_id` = ?',(connect_with,telegram_id))

    def select_connect_with(self,telegram_id):
        with self.connection:
            return self.cursor.execute('SELECT `connect_with` FROM `users` WHERE `telegram_id` = ?',(telegram_id,)).fetchone()

    def select_connect_with_self(self, telegram_id):
        with self.connection:
            return self.cursor.execute('SELECT `telegram_id` FROM `users` WHERE `connect_with` = ?',(telegram_id,)).fetchone()

    def log_msg(self,telegram_id,msg):
        with self.connection:
            self.cursor.execute('INSERT INTO `all_messages` (`sender`,`message`) VALUES (?,?)',(telegram_id,msg))

    def queue_exists(self,telegram_id):
        with self.connection:
            result = self.cursor.execute('SELECT * FROM `queue` WHERE `telegram_id` = ?', (telegram_id,)).fetchall()
            return bool(len(result))

    def count_user(self):
        with self.connection:
            result = self.cursor.execute('SELECT COUNT(*) FROM `users`').fetchone()
            return result[0]

    def add_count_msg(self,telegram_id):
        with self.connection:
            self.cursor.execute('UPDATE `users` SET `all_msg` = `all_msg` + 1 WHERE `telegram_id` = ?',(telegram_id,))

    def top_rating(self):
        with self.connection:
            return self.cursor.execute('SELECT `telegram_id` FROM `users` ORDER BY `all_msg` DESC LIMIT 5').fetchall()

    def get_name_user(self,telegram_id):
        with self.connection:
            result = self.cursor.execute('SELECT `telegram_username` FROM `users` WHERE `telegram_id` = ?',(telegram_id,)).fetchone()
            return result[0]

    def get_count_all_msg(self,telegram_id):
        with self.connection:
            result = self.cursor.execute('SELECT `all_msg` FROM `users` WHERE `telegram_id` = ?',(telegram_id,)).fetchone()
            return result[0]
