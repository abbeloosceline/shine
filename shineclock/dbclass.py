import mysql.connector as connector
import datetime


class DbClass:

    def __init__(self):
        self.__dsn = {
            "host": "localhost",
            "user": "root",
            "passwd": "root",
            "db": "shinedb"
        }

        self.__connection = connector.connect(**self.__dsn)
        self.__cursor = self.__connection.cursor()


    def getSounds(self):
        resultlist = []
        self.__connection = connector.connect(**self.__dsn)
        self.__cursor = self.__connection.cursor()
        sqlQuery = "SELECT * FROM shinedb.sound;"
        self.__cursor.execute(sqlQuery)
        result = self.__cursor.fetchall()
        self.__cursor.close()
        for element in result:
            text = str(element[1])
            if element[2]:
                text += " - " + str(element[2])
            resultlist.append(text)
        return resultlist


    def getAlarmTodayUnique(self):
        self.__connection = connector.connect(**self.__dsn)
        self.__cursor = self.__connection.cursor()
        sqlQuery = "SELECT * FROM `shinedb`.`uniquealarm` inner JOIN `shinedb`.`alarms` ON `uniquealarm`.`alarms_idalarms` = `alarms`.`idalarms` WHERE `uniquealarm`.`date` = (curdate()+1);"
        self.__cursor.execute(sqlQuery)
        result = self.__cursor.fetchone()
        self.__cursor.close()
        #hours in 7.8.9
        return result


    def getAlarmTodayWeek(self):
        self.__connection = connector.connect(**self.__dsn)
        self.__cursor = self.__connection.cursor()
        sqlQuery = "SELECT * FROM `shinedb`.`weekdayalarm` inner JOIN `shinedb`.`alarms` ON `weekdayalarm`.`alarms_idalarms` = `alarms`.`idalarms` inner JOIN `shinedb`.`weekday` ON `weekdayalarm`.`weekday_idweekday` = `weekday`.`idweekday` WHERE `weekdayalarm`.`weekday_idweekday` = weekday(curdate()+1);"
        self.__cursor.execute(sqlQuery)
        result = self.__cursor.fetchone()
        self.__cursor.close()
        return result


    def getAlarmToday(self):
        result = self.getAlarmTodayUnique()
        if result:
            return result
        else:
            result = self.getAlarmTodayWeek()
            if result:
                return result
            else: return False