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
        print(result)
        if result:
            result = result[8]
            uren = int(result[0:2])
            minuten = int(result[3:5])
            wait = datetime.datetime(2000, 1, 1, uren, minuten, 0)
            wakeup1 = wait - datetime.timedelta(hours=9, minutes=15)
            wakeup2 = wait - datetime.timedelta(hours=7, minutes=45)
            alarm = "Your alarm is set to " + str(result)[0:5] + "."
            wakeup = "Try to go to sleep at " + str(wakeup1)[11:16] + " or " + str(wakeup2)[11:16] + "."
            return alarm, wakeup
        else:
            result = self.getAlarmTodayWeek()
            if result:
                result = result[8]
                uren = int(result[0:2])
                minuten = int(result[3:5])
                wait = datetime.datetime(2000, 1, 1, uren, minuten, 0)
                wakeup1 = wait - datetime.timedelta(hours=9, minutes=15)
                wakeup2 = wait - datetime.timedelta(hours=7, minutes=45)
                alarm = "Your alarm is set to " + str(result)[0:5] + "."
                wakeup = "Try to go to sleep at " + str(wakeup1)[11:16] + " or " + str(wakeup2)[11:16] + "."
                return alarm, wakeup
            else: return "You don't have an alarm set!", "Go to alarms to create a new alarm."


    def getAlarmUnique(self, alarmdate):
        self.__connection = connector.connect(**self.__dsn)
        self.__cursor = self.__connection.cursor()
        sqlQuery = "SELECT * FROM `shinedb`.`uniquealarm` inner JOIN `shinedb`.`alarms` ON `uniquealarm`.`alarms_idalarms` = `alarms`.`idalarms` WHERE `uniquealarm`.`date` = date(" + alarmdate + ");"
        self.__cursor.execute(sqlQuery)
        result = self.__cursor.fetchone()
        self.__cursor.close()
        return result

    def getAlarmWeek(self, alarmdate):
        self.__connection = connector.connect(**self.__dsn)
        self.__cursor = self.__connection.cursor()
        sqlQuery = "SELECT * FROM `shinedb`.`weekdayalarm` inner JOIN `shinedb`.`alarms` ON `weekdayalarm`.`alarms_idalarms` = `alarms`.`idalarms` inner JOIN `shinedb`.`weekday` ON `weekdayalarm`.`weekday_idweekday` = `weekday`.`idweekday` WHERE `weekdayalarm`.`weekday_idweekday` = weekday(" + alarmdate + ");"
        self.__cursor.execute(sqlQuery)
        result = self.__cursor.fetchone()
        self.__cursor.close()
        return result

    def getAlarmsMonth(self):
        month = datetime.datetime.now().month
        year = datatime.dateime.now().year
        print(month, year)
        for week in calendar.monthcalendar(year, month):
            pass


    def setAlarm(self, sunrise, snooze, soundid):
        self.__connection = connector.connect(**self.__dsn)
        self.__cursor = self.__connection.cursor()
        sqlQuery = "INSERT INTO `shinedb`.`alarms` (`sunrise`, `snooze`, `sound_idsound`, `earliest`, `ideal`, `latest`) VALUES ('" + sunrise + "', '" + snooze + "', '" + soundid + "', '07:00:00', '07:00:00', '08:00:00');"
        self.__cursor.execute(sqlQuery)
        self.__connection.commit()
        self.__cursor.close()


    def setUniqueAlarm(self, alarm, alarmdate):
        self.__connection = connector.connect(**self.__dsn)
        self.__cursor = self.__connection.cursor()
        sqlQuery = "INSERT INTO `shinedb`.`uniquealarm` (`ideal`, `latest`) VALUES ('" + str(alarm) + "', '1', '3', '07:00:00', '07:00:00', '08:00:00');"
        self.__cursor.execute(sqlQuery)
        self.__connection.commit()
        self.__cursor.close()


    def setAlarmWeek(self, alarm, weekdays):
        for i in range(7):
            if weekdays[i] == 1:
                self.__connection = connector.connect(**self.__dsn)
                self.__cursor = self.__connection.cursor()
                sqlQuery = "UPDATE `shinedb`.`weekdayalarm` SET `alarms_idalarms`='" + str(alarm) + "' WHERE `weekday_idweekday`='" + str(i) + "';"
                self.__cursor.execute(sqlQuery)
                self.__connection.commit()
                self.__cursor.close()