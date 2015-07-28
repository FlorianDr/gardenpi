#!/usr/bin/python
from influxdb import InfluxDBClient

client = InfluxDBClient('46.101.235.75', 8086, 'root', 'root', 'GardenPi')

def writeHumAndTemp(temp, hum):
    json_body = [{
        "measurement": "air_temp_hum",
        "tags": {
            "host": "tomato-1"
        },
        "fields": {
            "temp": temp,
            "hum" : hum
        }
    }]
    checkResult(client.write_points(json_body))

def writeSoilHum(hum):
    json_body = [{
        "measurement": "soil__hum",
        "tags": {
            "host": "tomato-1"
        },
        "fields": {
            "hum" : hum
        }
    }]
    checkResult(client.write_points(json_body))

def checkResult(result):
    if result:
        print("Wrote data to database");
    else:
        print("Failed to write data to database");
