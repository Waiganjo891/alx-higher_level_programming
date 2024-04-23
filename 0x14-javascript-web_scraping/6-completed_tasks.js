#!/usr/bin/node

const request = require('request');
function fetchTasks (url) {
  return new Promise((resolve, reject) => {
    request(url, { json: true }, (error, response, body) => {
      if (error) {
        reject(error);
      } else {
        resolve(body);
      }
    });
  });
}
function countCompletedTasks (tasks) {
  const userTasks = {};
  tasks.forEach(task => {
    if (task.completed) {
      const userId = task.userId.toString();
      if (!userTasks[userId]) {
        userTasks[userId] = 0;
      }
      userTasks[userId]++;
    }
  });
  return userTasks;
}
async function main (apiUrl) {
  try {
    const tasks = await fetchTasks(apiUrl);
    const completedTasks = countCompletedTasks(tasks);
    console.log(completedTasks);
  } catch (error) {
    console.error('Error fetching tasks:', error);
  }
}
const apiUrl = process.argv[2];
main(apiUrl);
