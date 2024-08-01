document.addEventListener("DOMContentLoaded", () => {
  const inputText = document.getElementById("inputText");
  const addButton = document.getElementById("addButton");
  const itemList = document.getElementById("itemList");

  const loadItems = () => {
    const list = JSON.parse(localStorage.getItem("tasks")) || [];
    list.forEach((item) => addItemToDOM(item));
  };

  const addItemToDOM = (item) => {
    let li = document.createElement("li");
    li.textContent = item;

    const removeBtn = document.createElement("button");
    removeBtn.textContent = "remove";
    removeBtn.className = "remove-button";
    removeBtn.onclick = () => {
      removeItem(item, li);
    };

    li.appendChild(removeBtn);
    itemList.appendChild(li);
  };

  const addItem = () => {
    const input = inputText.value.trim();
    if (input) {
      addItemToDOM(input);
      const list = JSON.parse(localStorage.getItem("tasks"));
      list.push(input);
      localStorage.setItem("tasks", JSON.stringify(list));
      inputText.value = "";
    }
  };

  const removeItem = (task, element) => {
    let tasks = JSON.parse(localStorage.getItem("tasks"));
    tasks = tasks.filter((t) => {return t !== task}); 

    localStorage.setItem("tasks", JSON.stringify(tasks));
    element.remove();
  };

  loadItems();

  addButton.addEventListener("click", addItem);
});
