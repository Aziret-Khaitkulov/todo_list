document.addEventListener('DOMContentLoaded', () => {
    const taskForm = document.getElementById('task-form');
    const taskList = document.getElementById('task-list');

    // Fetch and display tasks
    async function fetchTasks() {
        const response = await fetch('/tasks');
        const tasks = await response.json();
        taskList.innerHTML = '';
        tasks.forEach(task => {
            const taskItem = createTaskItem(task);
            taskList.appendChild(taskItem);
        });
    }

    // Create a task item element
    function createTaskItem(task) {
        const li = document.createElement('li');
        li.className = task.completed ? 'completed' : '';
        li.innerHTML = `
            <span>${task.title}</span>
            <button class="delete-btn">Delete</button>
        `;
        li.querySelector('.delete-btn').addEventListener('click', async (e) => {
            e.stopPropagation();
            await deleteTask(task.id);
        });
        li.addEventListener('click', () => toggleTaskCompletion(task.id));
        return li;
    }

    // Add a new task
    taskForm.addEventListener('submit', async (e) => {
        e.preventDefault();
        const title = document.getElementById('task-title').value;
        const description = document.getElementById('task-description').value;
        const response = await fetch('/tasks', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ title, description })
        });
        const newTask = await response.json();
        const taskItem = createTaskItem(newTask);
        taskList.appendChild(taskItem);
        taskForm.reset();
    });

    // Toggle task completion
    async function toggleTaskCompletion(taskId) {
        const response = await fetch(`/tasks/${taskId}`);
        const task = await response.json();
        const updatedTask = { ...task, completed: !task.completed };
        await fetch(`/tasks/${taskId}`, {
            method: 'PUT',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(updatedTask)
        });
        fetchTasks();
    }

    // Delete a task
    async function deleteTask(taskId) {
        await fetch(`/tasks/${taskId}`, {
            method: 'DELETE'
        });
        fetchTasks();
    }

    // Initial fetch of tasks
    fetchTasks();
});