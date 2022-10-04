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
        if all(i not in place["xpostDate"] for i in ["2013", "2014"]):
            file.write(place["stitle"]+","+place["address"][5:8]+","+ 
            place["longitude"]+","+place["latitude"]+","+place["file"][0:end+3]+"\n")

# 為什麼這樣不行？
# with open("data.txt", "w", encoding="utf-8") as file:
#     for place in viewlist:
#         if "2014" not in place["xpostDate"] or "2013" not in place["xpostDate"]:
#             file.write(place["stitle"]+","+place["address"][5:8]+","+ 
#             place["longitude"]+","+place["latitude"]+","+place["xpostDate"]+"\n")
# ans:因為當成是執行到"2014"是否不在字串中時，回傳值為true，就會直接執行下面的程式，不會再確認"2013"是否也不在字串中
# 
# 還沒解決要怎麼同時查找兩個子字串的問題
# end=place["file"].find("jpg") 