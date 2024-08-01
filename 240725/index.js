document.addEventListener("DOMContentLoaded", () => {
  const inputText = document.getElementById("inputText");
  const addTaskBtn = document.getElementById("addTaskBtn");
  const taskList = document.getElementById("taskList");

  const loadTasks = () => {
    tasks = JSON.parse(localStorage.getItem("tasks"));
    tasks.forEach((task) => addTaskToDOM(task));
  };

  const addTaskToDOM = (task) => {
    const li = document.createElement("li");
    li.className = "task-item";
    li.textContent = task;

    const removeBtn = document.createElement("button");
    removeBtn.textContent = "remove";
    removeBtn.className = "task-button";
    removeBtn.onclick = () => removeTask(task, li);

    li.appendChild(removeBtn);
    taskList.appendChild(li);
  };

  const addTask = () => {
    const task = inputText.value.trim();
    if (task) {
      addTaskToDOM(task);
      let tasks = JSON.parse(localStorage.getItem("tasks"));
      tasks.push(task);
      localStorage.setItem("tasks", JSON.stringify(tasks));
      inputText.value = "";
    }
  };

  const removeTask = (task, element) => {
    let tasks = JSON.parse(localStorage.getItem("tasks"));
    tasks = tasks.filter((t) => {t !== task})
    localStorage.setItem("tasks", JSON.stringify(tasks));
    element.remove();
  };

  addTaskBtn.addEventListener("click", addTask);

  inputText.addEventListener("keydown", (event) => {
    if (event.key === "Enter") {
      addTask();
    }
  });

  loadTasks();
});
