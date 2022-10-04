from gettext import find
import urllib.request as request
import json
src="https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json"
with request.urlopen(src) as response:
    data=json.load(response) #利用json模組處理json資料格式
viewlist=data["result"]["results"]
with open("data.csv", "w", encoding="utf-8") as file:
    for place in viewlist:
        end=place["file"].lower().find("jpg") #因為網址裡包含大寫的JPG，所以先把網址列全部轉為小寫，再查找jpg第一次出現的位置。
        if int(place["xpostDate"][0:4])>=2015:
            file.write(place["stitle"]+","+place["address"][5:8]+","+ 
            place["longitude"]+","+place["latitude"]+","+place["file"][0:end+3]+"\n")


# 還沒解決要怎麼同時查找兩個子字串的問題
# end=place["file"].find("jpg") 
