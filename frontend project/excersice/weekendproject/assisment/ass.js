const questions = [
    {
        text: "Which tag is used to create a hyperlink in HTML?",
        options: ["<a>", "<link>", "<href>", "<hyperlink>"],
        correct: 0
    },
    {
        text: "Which CSS property is used to change the text color?",
        options: ["font-color", "text-color", "color", "background-color"],
        correct: 2
    },
    {
        text: "What does DOM stand for in JavaScript?",
        options: ["Document Object Model", "Data Object Manipulation", "Document Object Management", "Data Orientation Model"],
        correct: 0
    },
    {
        text: "Which of the following is used to add JavaScript to a webpage?",
        options: ["<style>", "<script>", "<js>", "<javascript>"],
        correct: 1
    },
    {
        text: "Which of the following CSS frameworks is widely used for responsive design?",
        options: ["Foundation", "Bulma", "Bootstrap", "Tailwind"],
        correct: 2
    }
];

let currentQuestionIndex = 0;
let score = 0;
let timerInterval;

function loadQuestion() {
    if (currentQuestionIndex >= questions.length) {
        showResult();
        return;
    }

    const question = questions[currentQuestionIndex];
    document.getElementById("question-text").innerText = question.text;

    const optionsForm = document.getElementById("options-form");
    optionsForm.innerHTML = ''; 

    question.options.forEach((option, index) => {
        const optionDiv = document.createElement('div');
        optionDiv.className = 'form-check';

        const radioInput = document.createElement('input');
        radioInput.className = 'form-check-input';
        radioInput.type = 'radio';
        radioInput.name = 'option';
        radioInput.id = `option${index}`;
        radioInput.value = index;

        const label = document.createElement('label');
        label.className = 'form-check-label';
        label.htmlFor = `option${index}`;
        label.innerText = option;

        optionDiv.appendChild(radioInput);
        optionDiv.appendChild(label);
        optionsForm.appendChild(optionDiv);
    });

    startTimer(120); 
}

function startTimer(seconds) {
    clearInterval(timerInterval);
    let timeRemaining = seconds;
    document.getElementById("timer").innerText = formatTime(timeRemaining);
    
    timerInterval = setInterval(() => {
        timeRemaining--;
        document.getElementById("timer").innerText = formatTime(timeRemaining);
        
        if (timeRemaining <= 0) {
            clearInterval(timerInterval);
            nextQuestion();
        }
    }, 1000);
}

function formatTime(seconds) {
    const minutes = Math.floor(seconds / 60);
    const secondsRemaining = seconds % 60;
    return `${minutes.toString().padStart(2, '0')}:${secondsRemaining.toString().padStart(2, '0')}`;
}

function submitAnswer() {
    const selectedOption = document.querySelector('input[name="option"]:checked');
    
    if (!selectedOption) {
        alert("Please select an answer before submitting!");
        return;
    }

    const selectedIndex = parseInt(selectedOption.value);
    const correctAnswer = questions[currentQuestionIndex].correct;
    
    if (selectedIndex === correctAnswer) {
        score++;
    }
    
    nextQuestion();
}

function nextQuestion() {
    currentQuestionIndex++;
    loadQuestion();
}

function showResult() {
    document.getElementById("question-container").classList.add("d-none");
    document.getElementById("result-container").classList.remove("d-none");
    document.getElementById("final-score").innerText = `${score} / ${questions.length}`;
}

function restartQuiz() {
    score = 0;
    currentQuestionIndex = 0;
    document.getElementById("result-container").classList.add("d-none");
    document.getElementById("question-container").classList.remove("d-none");
    loadQuestion();
}


window.onload = loadQuestion;
