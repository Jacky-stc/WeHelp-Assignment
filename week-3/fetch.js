const jsonUrl="https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json"

let jsonData= {};
let place=[];
let end;
let result = [];

fetch(jsonUrl, {method: "get"})
    .then((response) =>{
        return response.json();
    }).then((data) =>{
        jsonData= data.result.results;
        for(let i = 0; i<10; i++){
            end=jsonData[i]["file"].toLowerCase().indexOf("jpg", 0);
            place=[jsonData[i]["stitle"],jsonData[i]["file"].substring(0,end+3)];
            let myDiv = document.getElementById('description'+i.toString());
            let newDiv = document.createElement("div");
            let textNode = document.createTextNode(place[0]);
            newDiv.appendChild(textNode);
            myDiv.appendChild(newDiv);
            document.getElementById("image"+i.toString()).style.backgroundImage = "url(" + place[1] + ")";
        }
        
    })


let srcnow = 10;
function createDiv(){
    let myDiv1 = document.querySelector(".mainArea"); //選取要插入的位置
    for(let i = srcnow; i<srcnow+8;i++){ 
        let newDiv1 = document.createElement("div"); //建立新的標籤div
        myDiv1.appendChild(newDiv1);
        newDiv1.className = "content";
        newDiv1.setAttribute("id","content"+i.toString());

        let newText = document.createElement("div");
        newDiv1.appendChild(newText);
        newText.className = "test";
        newText.setAttribute("id", "text"+i.toString());

        
    } //重複創立div8次

    fetch(jsonUrl, {method: "get"})
        .then((response) =>{
          return response.json();
      }).then((data) =>{
          jsonData= data.result.results;
        

        for(let i = srcnow; i<jsonData.length; i++){
            end=jsonData[i]["file"].toLowerCase().indexOf("jpg", 0);
            place=[jsonData[i]["stitle"],jsonData[i]["file"].substring(0,end+3)];//place儲存[地名,照片網址]
            document.querySelector("#content"+i.toString()).style.backgroundImage = "url(" + place[1] + ")";
            document.querySelector("#text"+i.toString()).innerText=place[0];
            srcnow++; //紀錄當前總資料數
            // console.log(srcnow);
            // console.log(jsonData.length);
            if(srcnow>=jsonData.length){
                let noshow = document.querySelector("#btn");
                noshow.style.display = ("none");
            }    
            
        }
        
    })
    
}




