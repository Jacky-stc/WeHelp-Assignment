const jsonUrl="https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json"

let jsonData= {};
let place;
let end;
fetch(jsonUrl, {method: "get"})
    .then((response) =>{
        return response.json();
    }).then((data) =>{
        jsonData= data.result.results;
        
        for(let i = 0; i<jsonData.length; i++){
            end=jsonData[i]["file"].toLowerCase().indexOf("jpg", 0);
            place=[jsonData[i]["stitle"],jsonData[i]["file"].substring(0,end+3)];
            // console.log(jsonData[i]["file"].substring(0,end+3));
            // console.log(place.length);
            // console.log(typeof(place));
            // console.log(place[0]);
            // console.log(place[1]);
            // console.log(i);
            // console.log(typeof(i));
            let myDiv = document.getElementById('description'+i.toString());
            let newDiv = document.createElement("div");
            let textNode = document.createTextNode(place[0]);
            newDiv.appendChild(textNode);
            myDiv.appendChild(newDiv);
            document.getElementById("image"+i.toString()).style.backgroundImage = "url(" + place[1] + ")";
        }
        
    })

function change(){
    let show = document.querySelectorAll('#hid');
    for(let i =0;i<show.length;i++){
        show[i].style.display=('');
    }
    let noshow = document.getElementById('btn');
    noshow.style.display = ("none");
    let nextbt = document.getElementById('btn1');
    nextbt.style.display = ('');
}
function change1(){
    let show = document.querySelectorAll('#hid1');
    for(let i =0;i<show.length;i++){
        show[i].style.display=('');
    }
    let noshow = document.getElementById('btn1');
    noshow.style.display = ("none");
    let nextbt = document.getElementById('btn2');
    nextbt.style.display = ('');
}
function change2(){
    let show = document.querySelectorAll('#hid2');
    for(let i =0;i<show.length;i++){
        show[i].style.display=('');
    }
    let noshow = document.getElementById('btn2');
    noshow.style.display = ("none");
    let nextbt = document.getElementById('btn3');
    nextbt.style.display = ('');
}
function change3(){
    let show = document.querySelectorAll('#hid3');
    for(let i =0;i<show.length;i++){
        show[i].style.display=('');
    }
    let noshow = document.getElementById('btn3');
    noshow.style.display = ("none");
    let nextbt = document.getElementById('btn4');
    nextbt.style.display = ('');
}
function change4(){
    let show = document.querySelectorAll('#hid4');
    for(let i =0;i<show.length;i++){
        show[i].style.display=('');
    }
    let noshow = document.getElementById('btn4');
    noshow.style.display = ("none");
    let nextbt = document.getElementById('btn5');
    nextbt.style.display = ('');
}
function change5(){
    let show = document.querySelectorAll('#hid5');
    for(let i =0;i<show.length;i++){
        show[i].style.display=('');
    }
    let noshow = document.getElementById('btn5');
    noshow.style.display = ("none");
}
// let mylist = document.getElementById("mylist");
// let newList = document.createElement("li");
// let textNode = document.createTextNode("Hello world!");
// newList.appendChild(textNode);
// mylist.appendChild(newList);
// https://img.freepik.com/free-photo/cherry-blossoms-spring-chureito-pagoda-fuji-mountain-japan_335224-177.jpg?w=1380&t=st=1663679681~exp=1663680281~hmac=c4dfbe6650d7a4222d1dfa050ac98bb055c033a5d33940f514d92c84a8fd2577

// document.querySelector(".description").textContent="Japan";

