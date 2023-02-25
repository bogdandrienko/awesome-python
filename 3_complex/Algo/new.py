# import getpass
# import oracledb
# import pyinstaller
import cx_Oracle
import time

# pyodbc.connect('DRIVER={Oracle in OraClient11g_home1};Direct=True;Host=172.30.23.16;Port=1521;Service
# Name=PITENEW;User ID=DISPATCHER;Password=disp')
# oracledb.init_oracle_client()
# connection = oracledb.connect(
#     # host="172.30.23.16",
#     # port=1521,
#     # service_name="PITENEW",
#     dsn="172.30.23.16/PITENEW",
#     user="DISPATCHER",
#     password="disp",
# )
# print("Successfully connected to Oracle Database")
# cursor = connection.cursor()
try:
    input("старт: ")
    cx_Oracle.init_oracle_client(lib_dir=r"./instantclient_21_9")
    connection = cx_Oracle.connect('DISPATCHER/disp@172.30.23.16/PITENEW')
    # connection = cx_Oracle.connect(
    #     user="DISPATCHER",
    #     password="Disp",
    #     # host="172.30.23.16",
    #     # port=1521,
    #     # service_name="PITENEW",
    #     dsn="172.30.23.16/PITENEW"
    # )

    cursor = connection.cursor()
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
                   AND VEHID = '139'
            ORDER  BY TIMELOAD DESC) 
    WHERE ROWNUM < 2
    
        """)
    rows = cursor.fetchall()
    print(rows)
    print(connection.version)
    connection.close()
    time.sleep(3.0)
    input("")
except Exception as error:
    print(error)
    time.sleep(3.0)
    input("")
# Create a table

# cursor.execute("""
#     begin
#         execute immediate 'drop table todoitem';
#         exception when others then if sqlcode <> -942 then raise; end if;
#     end;""")
#
# cursor.execute("""
#     create table todoitem (
#         id number generated always as identity,
#         description varchar2(4000),
#         creation_ts timestamp with time zone default current_timestamp,
#         done number(1,0),
#         primary key (id))""")
#
# # Insert some data
#
# rows = [ ("Task 1", 0 ),
#          ("Task 2", 0 ),
#          ("Task 3", 1 ),
#          ("Task 4", 0 ),
#          ("Task 5", 1 ) ]
#
# cursor.executemany("insert into todoitem (description, done) values(:1, :2)", rows)
# print(cursor.rowcount, "Rows Inserted")
#
# connection.commit()
#
# # Now query the rows back
# for row in cursor.execute('select description, done from todoitem'):
#     if (row[1]):
#         print(row[0], "is done")
#     else:
#         print(row[0], "is NOT done")
