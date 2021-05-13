cities = open('dests.txt',encoding='utf-8')
import json
import requests
data=dict()
farTest=dict()
for line in cities:
    url="https://maps.googleapis.com/maps/api/distancematrix/json?units=imperial&origins=%D7%AA%D7%9C%25%D7%90%D7%91%D7%99%D7%91&"
    dest="destinations="+line
    key="&key=AIzaSyBkwLXCBFrBHBUMOt0naYIOYqRlCEz_mAA" 
    response = requests.get(url+dest+key)
    res= response.content.decode('utf-8')  
    info = json.loads(res)
    city = info['destination_addresses'][0]
    info = info['rows'][0]['elements'][0]
    distance = info['distance']['value']
    duration = info['duration']['text']
    distance = float(distance)/1000
    #distance = str(distance)+' KM'
    
    if 'day' in duration:
        space = duration.find(" ")
        end = duration.find("h")
        hour = duration[end-3:end-1]
        hour = int(hour)
        days = duration[:space]
        days = int(days)*24
        totaltime = days + hour
        duration = str(totaltime) + ' hours'
    secUrl="https://maps.googleapis.com/maps/api/geocode/json?address="
    response = requests.get(secUrl+line+key)
    response= response.content.decode('utf-8')
    response = json.loads(response)
    lng = response['results'][0]['geometry']['location']['lng']
    lat = response['results'][0]['geometry']['location']['lat']
    tap = (distance,duration,lng,lat)
    farTest[city]=distance
    data[city]=tap
print(data) 
far = sorted(farTest)
maxfar = far[:3]  