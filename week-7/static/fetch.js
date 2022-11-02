// 查詢會員
const result = document.getElementById("search_form");
let search_name = document.createElement("div");
let username;
function get_name(){
    let user_account = search_form.username.value.toString();
    let url =  "http://127.0.0.1:3000/api/member?username=" + user_account ;
    fetch(url, {method: "GET"})
    .then((response) =>{
        return response.json();
    })
    .then((data) =>{
        if (data.data == null){
            search_name.textContent =  "查無此用戶"
        }else{
            username = data.data['name'];
            search_name.textContent = username + `( ${user_account} )`;
        }
        result.appendChild(search_name);
        document.getElementById("name").value = "";
    })
}
// 更改姓名
const updated = document.getElementById("alter_form")
let update_message = document.createElement("div")
function alter_name(){
    let content = {"name": alter_form.alter.value.toString()};
    fetch("http://127.0.0.1:3000/api/member", {
        method: 'PATCH',
        headers: {
            'Content-type' :'application/json; charset=UTF-8',
            'Accept':'application/jason'
        },
        body: JSON.stringify(content)
    }).then((response) =>{
        return response.json();
    }).then((data) =>{
        if(data['ok']== true){
            update_message.textContent = "更新成功"
        }else{
            update_message.textContent = "更新失敗"
        }
        update_message.setAttribute("id", "congrat")
        updated.appendChild(update_message)
        document.getElementById("alter").value = "";
        setTimeout(() => {
            updated.removeChild(update_message)
        }, 5000);
    })
}