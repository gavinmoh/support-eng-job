class TaskDisplay {
  constructor(tasks) {
    this.tasks = tasks;
  }

  displayTasks() {
    if (!this.tasks) {
      return;  // Should return ""
    }
    return this.tasks.map(task => `${task.id}: ${task.title} (${task.priority})`).join("\n");
  }

  filterByPriority(priority) {
    // ensure both priority and task.priority are lowercased for case-insensitive comparison
    return this.tasks.filter(task => task.priority.toLowerCase() === priority.toLowerCase());
  }

  getTaskCount() {
    return this.tasks.length;
  }
}

module.exports = TaskDisplay;
