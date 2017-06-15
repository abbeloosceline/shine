import mysql.connector as connector


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

    def getDataFromDatabase(self):
        # Query zonder parameters
        sqlQuery = "SELECT * FROM tablename"

        self.__cursor.execute(sqlQuery)
        result = self.__cursor.fetchall()
        self.__cursor.close()
        return result

    def getDataFromDatabaseMetVoorwaarde(self, voorwaarde):
        # Query met parameters
        sqlQuery = "SELECT * FROM tablename WHERE columnname = '{param1}'"
        # Combineren van de query en parameter
        sqlCommand = sqlQuery.format(param1=voorwaarde)

        self.__cursor.execute(sqlCommand)
        result = self.__cursor.fetchall()
        self.__cursor.close()
        return result

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


    def getUniqueAlarm(self, alarmdate):
        self.__connection = connector.connect(**self.__dsn)
        self.__cursor = self.__connection.cursor()
        sqlQuery = "SELECT * FROM `shinedb`.`uniquealarm` inner JOIN `shinedb`.`alarms` ON `uniquealarm`.`alarms_idalarms` = `alarms`.`idalarms` WHERE `uniquealarm`.`date` = date(" + alarmdate + ");"
        self.__cursor.execute(sqlQuery)
        result = self.__cursor.fetchone()
        self.__cursor.close()
        return result


    def setDataToDatabase(self, value1):
        # Query met parameters
        sqlQuery = "INSERT INTO tablename (columnname) VALUES ('{param1}')"
        # Combineren van de query en parameter
        sqlCommand = sqlQuery.format(param1=value1)

        self.__cursor.execute(sqlCommand)
        self.__connection.commit()
        self.__cursor.close()

    def setAlarm(self):
        self.__connection = connector.connect(**self.__dsn)
        self.__cursor = self.__connection.cursor()
        sqlQuery = "INSERT INTO `shinedb`.`alarms` (`idalarms`, `sunrise`, `snooze`, `sound_idsound`, `earliest`, `ideal`, `latest`) VALUES ('5', '1', '1', '3', '07:00:00', '07:00:00', '08:00:00');"
        self.__cursor.execute(sqlCommand)
        self.__connection.commit()
        self.__cursor.close()



hey = DbClass()
who = hey.getAlarmTodayUnique()
what = hey.getAlarmTodayWeek()
where = hey.getSounds()
print(who)
print(what)
print(where)

