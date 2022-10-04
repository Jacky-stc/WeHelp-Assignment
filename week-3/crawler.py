import urllib.request as req
import bs4
start=9500
number=10
end=start-number
for i in range(start, end, -1):
    url="https://www.ptt.cc/bbs/movie/index"+str(i)+".html"
    request=req.Request(url, headers={
        "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36"
    })

    with req.urlopen(request) as response:
        data=response.read().decode("utf-8")

    
    root=bs4.BeautifulSoup(data, "html.parser")
    titles=root.find_all("div", class_="title")
    
    with open("movie.txt", "a", encoding="utf-8") as file:
        for title in titles:
            if title.a != None:
                if "[好雷]" in title.a.string:
                    file.write(title.a.string+"\n")

for i in range(start, end, -1):
    url="https://www.ptt.cc/bbs/movie/index"+str(i)+".html"
    request=req.Request(url, headers={
        "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36"
    })

    with req.urlopen(request) as response:
        data=response.read().decode("utf-8")

    
    root=bs4.BeautifulSoup(data, "html.parser")
    titles=root.find_all("div", class_="title")
    
    with open("movie.txt", "a", encoding="utf-8") as file:
        for title in titles:
            if title.a != None:
                if "[普雷]" in title.a.string:
                    file.write(title.a.string+"\n")
for i in range(start, end, -1):
    url="https://www.ptt.cc/bbs/movie/index"+str(i)+".html"
    request=req.Request(url, headers={
        "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36"
    })

    with req.urlopen(request) as response:
        data=response.read().decode("utf-8")

    
    root=bs4.BeautifulSoup(data, "html.parser")
    titles=root.find_all("div", class_="title")
    
    with open("movie.txt", "a", encoding="utf-8") as file:
        for title in titles:
            if title.a != None:
                if "[負雷]" in title.a.string:
                    file.write(title.a.string+"\n")
    
    
# 還沒解決如何一次輸入三種不同標題進去
   