from fastapi import FastAPI
import uvicorn
import json
import pandas as pd
import http3
from datetime import datetime
import mysql.connector
import nest_asyncio
nest_asyncio.apply()


app=FastAPI(debug=True)
client = http3.AsyncClient()

##connection with api countries
async def call_api(url: str):
    r = await client.get(url)
    return r.text
## Create dataframe with important data like name,area and population
def obtain_important_data(result):
    countries=pd.DataFrame(columns=['Common_name', 'Official_name', 'Area', 'Population'])

    for i in range(len(result)):
        countries=countries.append({'Common_name':result[i]["name"]["common"], 'Official_name':result[i]["name"]["official"], 'Area':result[i]["area"], 'Population':result[i]["population"]},ignore_index=True)
    return countries

## Obtain density according to population/area
def obtain_density_countries(countries):
    countries["Density"]=0.0
    for i in range(len(countries)):
        countries["Density"][i]=countries["Population"][i]/countries["Area"][i]
    return countries

##Sort dataframe by density column
def obtain_sort_density(countries):
    countries= countries.sort_values('Density',ascending=False)
    countries= countries.reset_index(drop=True)
    return countries

## get only 5 countries with highest density
def obtain_countries_highest_density(countries):
    countries=countries.iloc[0:5]
    return countries

def connect_database(cedula,nombre,resultado_consulta):
    now = datetime.now()
    fecha = now.strftime("%Y-%m-%d")
    hora=now.strftime("%H:%M:%S")

    countries1 = resultado_consulta.to_dict()
    countries1=json.dumps(countries1)
    ## connection with mysql
    connection = mysql.connector.connect(
    user = "admin",
    passwd = "3112500689holmaN",
    port="3306",
    db="mydb",
    host = "db-prueba-analista.cj6owpmygvga.us-east-1.rds.amazonaws.com")
    cursor=connection.cursor()
    query1=(" INSERT INTO logs (cedula,nombre,fecha,hora,resultado_consulta) VALUES (%s, %s,%s, %s,%s)")
    val=(cedula,nombre,fecha,hora,countries1)
    cursor.execute(query1,val)
    connection.commit()

@app.get("/")
async def get_countries(cedula:int,nombre:str):
    try:
        ##result in string of countries api
        result = await call_api('https://restcountries.com/v3.1/all')
        ## convert string result to json
        result= json.loads(result)
    except Exception as e:
        return {"error": e}
    try:
        countries=obtain_important_data(result)
        countries_density=obtain_density_countries(countries)
        countries_sort_density=obtain_sort_density(countries_density)
        countries_highest_density=obtain_countries_highest_density(countries_sort_density)
        connect_database(cedula,nombre,countries_highest_density)
    except Exception as e:
        return {"error": e}
    return countries_highest_density

if __name__=="__main__":
    uvicorn.run(app,host="127.0.0.1",port="8000")
