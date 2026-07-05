
const API="https://interview-preparation-ai-pxyj.onrender.com";

async function startInterview(){
 const resume=document.getElementById("resume").value;
 await fetch(API+"/interview/start",{
 method:"POST",
 headers:{"Content-Type":"application/json"},
 body:JSON.stringify({resume})
 });
 alert("Interview started!");
}

async function getQuestion(){
 let r=await fetch(API+"/interview/next-question");
 let txt=await r.text();
 document.getElementById("questionBox").innerText=txt;
}

async function submitAnswer(){
 const answer=document.getElementById("answer").value;
 let r=await fetch(API+"/interview/submit-answer",{
 method:"POST",
 headers:{"Content-Type":"application/json"},
 body:JSON.stringify({answer})
 });
 document.getElementById("output").innerText=await r.text();
}
