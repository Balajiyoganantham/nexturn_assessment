
function addTask() {
    let taskInput = document.getElementById("taskInput");
    let taskText = taskInput.value;
    if (taskText.trim() !== "") {
        let taskList = document.getElementById("taskList");
        let newTask = document.createElement("li");
        newTask.innerHTML = `
            <span>${taskText}</span>
            <button class="remove-btn" onclick="removeTask(this)">Remove</button>
        `;
        newTask.addEventListener('click', function () {
            newTask.classList.toggle("completed");
        });
        taskList.appendChild(newTask);
        taskInput.value = "";
    }
}
function removeTask(taskButton) {
    let taskToRemove = taskButton.parentElement;
    taskToRemove.remove();
}
