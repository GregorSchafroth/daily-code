const taskInput = document.getElementById("taskInput");
const addTaskBtn = document.getElementById("addTaskBtn");
const taskList = document.getElementById("taskList");

const addTask = () => {
  task = taskInput.value.trim();
  if (task) {
    addTaskToDOM(task);
  }
}

const addTaskToDOM = (task) => {
  const li = document.createElement('li');
  li.textContent = task;

  const removeButton = document.createElement('button');
  removeButton.textContent = 'remove';
  removeButton.onclick = () => removeTask(li);

  li.appendChild(removeButton)
  taskList.appendChild(li);
}

const removeTask = (element) => {
  element.remove();
}

addTaskBtn.addEventListener('click', addTask);