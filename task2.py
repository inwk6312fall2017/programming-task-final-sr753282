from weather import Weather
weather = Weather()
def lookuplocation(city):
    location = weather.lookup_by_location(city)
    print(location)
    condition = location.condition() 

    

    forecast1 = location.forecast()
    while len(forecast1) > 5:
        forecast1.pop()
    
 

    temp = []
    for item in forecast1:
        high_temp = item['high']
        temp.append(int(high_temp))



    for item in forecast1:
        if int(item['high']) == max(temp):
            print("The higest tempeture will be on : %s " % (item['date']))
            print("The higest tempeture in next 5 days is : %s " % (item['high']))
            print("The weather on the higest tempeture day : %s " % (item['text']))

    for item in forecast1:
        if int(item['high']) == min(temp):
            print("The lowest tempeturewii be on : %s " % (item['date']))
            print("The lowest tempeture in next 5 days is : %s " % (item['high']))
            print("The weather onthe  lowest tempeture days : %s " % (item['text']))
        elif item['text'] == 'rain':
            print("The day that will be rainy is " % (item['date']))




lookuplocation('halifax')
