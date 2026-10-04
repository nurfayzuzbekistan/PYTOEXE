<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>PYTOEXE Demo</title>
    <style>
      :root {
        --bg: #0f172a;
        --card: #111827;
        --card-2: #1f2937;
        --primary: #22c55e;
        --primary-2: #16a34a;
        --text: #e5e7eb;
        --muted: #94a3b8;
        --danger: #ef4444;
        --shadow: rgba(0, 0, 0, 0.35);
      }

      * {
        box-sizing: border-box;
      }

      body {
        margin: 0;
        min-height: 100vh;
        display: grid;
        place-items: center;
        background: linear-gradient(135deg, var(--bg), #111827 40%, #0b1120);
        color: var(--text);
        font-family: Arial, Helvetica, sans-serif;
      }

      .app {
        width: min(92vw, 560px);
        background: rgba(17, 24, 39, 0.95);
        border: 1px solid rgba(148, 163, 184, 0.18);
        border-radius: 20px;
        padding: 24px;
        box-shadow: 0 20px 50px var(--shadow);
      }

      h1 {
        text-align: center;
        margin: 0 0 22px;
        font-size: clamp(1.8rem, 3vw, 2.5rem);
        color: #f8fafc;
      }

      .form {
        display: flex;
        gap: 10px;
        margin-bottom: 18px;
      }

      input[type="text"] {
        flex: 1;
        background: #0f172a;
        color: var(--text);
        border: 1px solid rgba(148, 163, 184, 0.25);
        border-radius: 12px;
        padding: 12px 14px;
        font-size: 1rem;
        outline: none;
      }

      input[type="text"]:focus {
        border-color: var(--primary);
        box-shadow: 0 0 0 2px rgba(34, 197, 94, 0.2);
      }

      button {
        border: none;
        border-radius: 12px;
        padding: 12px 18px;
        font-weight: 700;
        cursor: pointer;
        transition: transform 0.15s ease, opacity 0.15s ease;
      }

      button:hover {
        transform: translateY(-1px);
      }

      .add-btn {
        background: linear-gradient(135deg, var(--primary), var(--primary-2));
        color: white;
      }

      .clear-btn {
        background: rgba(239, 68, 68, 0.12);
        color: #fca5a5;
        border: 1px solid rgba(239, 68, 68, 0.25);
      }

      ul {
        list-style: none;
        padding: 0;
        margin: 0;
        display: flex;
        flex-direction: column;
        gap: 10px;
      }

      li {
        display: flex;
        align-items: center;
        justify-content: space-between;
        gap: 12px;
        background: var(--card-2);
        border: 1px solid rgba(148, 163, 184, 0.12);
        border-radius: 12px;
        padding: 12px 14px;
      }

      .task-main {
        display: flex;
        align-items: center;
        gap: 10px;
        flex: 1;
      }

      .task-main input[type="checkbox"] {
        width: 18px;
        height: 18px;
        accent-color: var(--primary);
        cursor: pointer;
      }

      .task-text {
        word-break: break-word;
        color: var(--text);
      }

      .task-text.done {
        text-decoration: line-through;
        opacity: 0.55;
      }

      .delete-btn {
        background: transparent;
        color: var(--danger);
        border: 1px solid rgba(239, 68, 68, 0.25);
        padding: 8px 10px;
        border-radius: 8px;
      }

      .status {
        margin-top: 16px;
        font-size: 0.95rem;
        color: var(--muted);
        text-align: center;
      }
    </style>
  </head>
  <body>
    <div class="app">
      <h1>PYTOEXE Demo</h1>

      <div class="form">
        <input id="taskInput" type="text" placeholder="Write a task..." />
        <button class="add-btn" id="addTask">Add</button>
      </div>

      <ul id="taskList"></ul>

      <div style="display: flex; justify-content: flex-end; margin-top: 15px;">
        <button class="clear-btn" id="clearDone">Clear Done</button>
      </div>

      <div id="status" class="status">Ready</div>
    </div>

    <script>
      const taskInput = document.getElementById('taskInput');
      const taskList = document.getElementById('taskList');
      const addTaskBtn = document.getElementById('addTask');
      const clearDoneBtn = document.getElementById('clearDone');
      const status = document.getElementById('status');

      const storageKey = 'pytoexe-tasks';

      function loadTasks() {
        const saved = localStorage.getItem(storageKey);
        return saved ? JSON.parse(saved) : [];
      }

      function saveTasks(tasks) {
        localStorage.setItem(storageKey, JSON.stringify(tasks));
      }

      function renderTasks() {
        const tasks = loadTasks();
        taskList.innerHTML = '';

        if (tasks.length === 0) {
          status.textContent = 'No tasks yet';
          return;
        }

        tasks.forEach((task, index) => {
          const li = document.createElement('li');

          const main = document.createElement('div');
          main.className = 'task-main';

          const checkbox = document.createElement('input');
          checkbox.type = 'checkbox';
          checkbox.checked = task.done;
          checkbox.addEventListener('change', () => {
            const items = loadTasks();
            items[index].done = checkbox.checked;
            saveTasks(items);
            renderTasks();
          });

          const text = document.createElement('span');
          text.className = `task-text ${task.done ? 'done' : ''}`;
          text.textContent = task.text;

          main.appendChild(checkbox);
          main.appendChild(text);

          const deleteBtn = document.createElement('button');
          deleteBtn.className = 'delete-btn';
          deleteBtn.textContent = 'Delete';
          deleteBtn.addEventListener('click', () => {
            const items = loadTasks();
            items.splice(index, 1);
            saveTasks(items);
            renderTasks();
          });

          li.appendChild(main);
          li.appendChild(deleteBtn);
          taskList.appendChild(li);
        });

        status.textContent = `${tasks.filter(task => task.done).length} done / ${tasks.length} total`;
      }

      function addTask() {
        const value = taskInput.value.trim();
        if (!value) {
          status.textContent = 'Please enter a task';
          taskInput.focus();
          return;
        }

        const tasks = loadTasks();
        tasks.push({ text: value, done: false });
        saveTasks(tasks);
        taskInput.value = '';
        taskInput.focus();
        renderTasks();
      }

      addTaskBtn.addEventListener('click', addTask);

      taskInput.addEventListener('keydown', (event) => {
        if (event.key === 'Enter') {
          addTask();
        }
      });

      clearDoneBtn.addEventListener('click', () => {
        const items = loadTasks().filter(task => !task.done);
        saveTasks(items);
        renderTasks();
      });

      renderTasks();
    </script>
  </body>
</html>
