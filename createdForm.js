<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Task List</title>
</head>
<body>

    <h2>Task List</h2>

    <form id="taskForm">
        <input type="text" id="newTask" placeholder="Enter a new task">
        <button type="submit" id="submitBtn" disabled>Submit</button>
    </form>

    <ul id="taskList"></ul>

    <script>
        // Query for the submit button and input task field
        
        const submitBtn = document.getElementById('submitBtn');
        const newTaskInput = document.getElementById('newTask');

        // Listen for input to be typed into the input field
        newTaskInput.addEventListener('input', () => {
            submitBtn.disabled = !newTaskInput.value.trim();
        });

        // Listen for submission of form
        document.getElementById('taskForm').addEventListener('submit', (event) => {
            // Prevent the default form submission
            event.preventDefault();

            // Find the task the user just submitted
            const newTaskText = newTaskInput.value.trim();

            // Create a list item for the new task and add the task to it
            const newTaskItem = document.createElement('li');
            newTaskItem.textContent = newTaskText;

            // Add new element to our unordered list
            document.getElementById('taskList').appendChild(newTaskItem);

            // Clear the input field
            newTaskInput.value = '';

            // Disable the submit button again after submission
            submitBtn.disabled = true;
        });

        // At the end of the script, add the line return false.
        // This prevents the default submission of the form.
        return false;
    </script>

</body>
</html>
