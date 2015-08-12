#!/usr/bin/python
from influxdb import InfluxDBClient 
from influxdb.client import InfluxDBClientError
 
client = InfluxDBClient('46.101.235.75', 8086, 'root', 'root', 'GardenPi')

def write_temp_and_hum((temp, hum)):
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
    _make_request(json_body)

def write_soil_hum(hum):
    json_body = [{
        "measurement": "soil_hum",
        "tags": {
            "host": "tomato-1"
        },
        "fields": {
            "hum" : hum
        }
    }]
    _make_request(json_body)

def write_watering(secs):
    json_body = [{
        "measurement": "watering",
        "tags": {
            "host": "tomato-1"
        },
        "fields": {
            "secs" : secs
        }
    }]
    _make_request(json_body)

def _make_request(json_body):
    try:
        _check_result(client.write_points(json_body, 's'))
    except (InfluxDBClientError) as e:
        print('Couldnt connect probably');

def _check_result(result):
    if result:
        print("Successfully wrote time series to database.");
    else:
        print("Failed to write to database.");
