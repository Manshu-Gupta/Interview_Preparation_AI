const API = "https://interview-preparation-ai-pxyj.onrender.com";

let currentQuestion = null;
let currentTopic = null;

async function startInterview() {
    const resume = document.getElementById("resume").value;

    await fetch(API + "/interview/start", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            resume: resume
        })
    });

    alert("Interview started successfully!");
}

async function getQuestion() {
    const response = await fetch(API + "/interview/next-question");
    const data = await response.json();

    currentQuestion = data.question;
    currentTopic = data.topic;

    document.getElementById("questionBox").innerText =
        `Topic: ${data.topic}\n\nQuestion: ${data.question}`;
}

async function submitAnswer() {
    const answer = document.getElementById("answer").value;

    const response = await fetch(API + "/interview/submit-answer", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            topic: currentTopic,
            question: currentQuestion,
            answer: answer
        })
    });

    const result = await response.json();

    document.getElementById("output").innerText =
        JSON.stringify(result, null, 2);
}
