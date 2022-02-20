import mysql.connector

connection = mysql.connector.connect(
    user = "admin",
    passwd = "3112500689holmaN",
    port="3306",
    host = "db-prueba-analista.cj6owpmygvga.us-east-1.rds.amazonaws.com")

cursor=connection.cursor()

#sql='''create database mydb'''
#cursor.execute(sql)

sql='''use mydb'''
cursor.execute(sql)

sql='''
create table logs(
id int not null auto_increment primary key,
cedula int(20),
nombre varchar(50),
fecha date,
hora time
resultado_consulta varchar(500)
)
'''
cursor.execute(sql)
