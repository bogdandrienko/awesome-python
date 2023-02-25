class Trip:
    class VehStatus:
        value = {
            "bad": 0.7,
            "middle": 0.9,
            "good": 1.0
        }

        @classmethod
        def bad(cls) -> float:
            return cls.value.get("bad", 0)

        @classmethod
        def middle(cls) -> float:
            return cls.value.get("middle", 0)

        @classmethod
        def good(cls) -> float:
            return cls.value.get("good", 0)

    def __init__(self, veh_status: float, speed_load: float, length: float, speed_move: float):
        self.__veh_status = veh_status
        self.__speed_load = speed_load
        self.__length = length
        self.__speed_move = speed_move

    def get_norm_time_load(self):
        return round(self.__speed_load * self.__veh_status, 3)

    def get_norm_time_path(self):
        return round(self.__length / self.__speed_move * 60, 3)

    def get_norm_time_unload(self):
        return round(1.0, 1)

    def get_norm_time_path_return(self):
        return round(self.__length / self.__speed_move * 60, 3)

    def get_norm_time_wait_load(self):
        return round(1.0, 1)

    def get_norm_time_full(self):
        return round(self.get_norm_time_load() + self.get_norm_time_path() + self.get_norm_time_unload() +
                     self.get_norm_time_path_return() + self.get_norm_time_wait_load(), 3)

    def get_equal_fact_with_norm(self, fact: float):
        return int(self.get_norm_time_full() / fact * 100)

    def print_all(self, fact: float):
        print("load: ", self.get_norm_time_load())
        print("path: ", self.get_norm_time_path())
        print("unload: ", self.get_norm_time_unload())
        print("path_return: ", self.get_norm_time_path_return())
        print("full: ", self.get_norm_time_full())
        print("result: ", self.get_equal_fact_with_norm(fact), "%\n")

def check():
    import oracledb
    import pyodbc
    # cnxn = pyodbc.connect('DRIVER={Devart ODBC Driver for Oracle};Direct=True;Host=172.30.23.16;Port=1521;Service Name=PITENEW;User ID=DISPATCHER;Password=disp')
    cnxn = pyodbc.connect('DRIVER={Oracle in OraClient11g_home1};Direct=True;Host=172.30.23.16;Port=1521;Service Name=PITENEW;User ID=DISPATCHER;Password=disp')
    # "Data Source=(DESCRIPTION=(ADDRESS=(PROTOCOL=tcp)(HOST=172.30.23.16)(PORT=1521))(CONNECT_DATA=(SERVICE_NAME=PITENEW))); User id=DISPATCHER; Password=disp"

    cursor = cnxn.cursor()
    # cursor.execute("INSERT INTO EMP (EMPNO, ENAME, JOB, MGR) VALUES (535, 'Scott', 'Manager', 545)")
    cursor = cnxn.cursor()
    cursor.execute("""

SELECT * 
FROM   (SELECT VEHID, 
               SHOVID, 
               UNLOADID, 
               WORKTYPE, 
               TIMELOAD, 
               TIMEUNLOAD, 
               TIME_INSERTING, 
               MOVETIME, 
               round((TIMEUNLOAD - TIMELOAD + (MOVETIME- TO_DATE('2000/01/01', 'yyyy/mm/dd')) / 1.65) * 24 * 60 , 1) TRIPTIME, 
               AREA, 
               FUELLOAD, 
               FUELUNLOAD, 
               WEIGHT, 
               AVSPEED, 
               LENGTH, 
               UNLOADLENGTH, 
               1 AS TripNum
        FROM VEHTRIPS vt
      WHERE  vt.TIMEUNLOAD BETWEEN GETPREDEFINEDTIMEFROM('за указанную смену', GETCURSHIFTNUM(0, SYSDATE), GETCURSHIFTDATE(0, SYSDATE)) AND GETPREDEFINEDTIMETO('за указанную смену', GETCURSHIFTNUM(0, SYSDATE), GETCURSHIFTDATE(0, SYSDATE))
               AND VEHID = :paramSelectTechId
        ORDER  BY TIMELOAD DESC) 
WHERE ROWNUM < 2

    """)
    rows = cursor.fetchall()
    print(rows)
    # for row in rows:
    #     print(row)
    # while row:
    #     print(row)
    #     row = cursor.fetchone()

if __name__ == "__main__":
    # todo Хороший самосвал, на разгрузку (скорость=18.9) от маленького экскаватора на расстояние 2.5 км, вскрыша
    Trip(
        speed_load=6.1,
        veh_status=Trip.VehStatus.good(),
        length=2.59,
        speed_move=18.9,
    ).print_all(fact=26.43)

    Trip(
        speed_load=4.5,
        veh_status=Trip.VehStatus.good(),
        length=1.80,
        speed_move=18.9,
    ).print_all(fact=08.59)

    check()