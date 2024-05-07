from daikinapi import Daikin

API = Daikin("172.16.2.106")
print(API)
print(API.target_temperature)