#!/usr/bin/python
from influxdb import InfluxDBClient

client = InfluxDBClient('46.101.235.75', 8086, 'root', 'root', 'GardenPi')


def writeHumAndTemp(temp, hum):
    json_body = [
    {
        "measurement": "temp",
        "fields" : {
            "value" : temp
        }
    }]
    client.write_points(json_body)
