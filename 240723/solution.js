document.addEventListener('DOMContentLoaded', (event) => {
  const taskInput = document.getElementById('taskInput');
  const addTaskBtn = document.getElementById('addTaskBtn');
  const taskList = document.getElementById('taskList');

  // Load tasks from localStorage
  const loadTasks = () => {
      const tasks = JSON.parse(localStorage.getItem('tasks')) || [];
      tasks.forEach(task => addTaskToDOM(task));
  };

  // Add task to DOM
  const addTaskToDOM = (task) => {
      const li = document.createElement('li');
      li.className = 'task-item';
      li.textContent = task;

      const removeBtn = document.createElement('button');
      removeBtn.textContent = 'Remove';
      removeBtn.onclick = () => removeTask(task, li);

      li.appendChild(removeBtn);
      taskList.appendChild(li);
  };

  // Add task to localStorage
  const addTask = () => {
      const task = taskInput.value.trim();
      if (task) {
          addTaskToDOM(task);
          let tasks = JSON.parse(localStorage.getItem('tasks')) || [];
          tasks.push(task);
          localStorage.setItem('tasks', JSON.stringify(tasks));
          taskInput.value = '';
      }
  };

  // Remove task from localStorage and DOM
  const removeTask = (task, element) => {
      let tasks = JSON.parse(localStorage.getItem('tasks')) || [];
      tasks = tasks.filter(t => t !== task);
      localStorage.setItem('tasks', JSON.stringify(tasks));
      element.remove();
  };

  // Event listener for the add task button
  addTaskBtn.addEventListener('click', addTask);

  // Load tasks when the page loads
  loadTasks();
});