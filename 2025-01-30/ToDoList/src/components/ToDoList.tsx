import React, { useState } from "react";
import Button from "./Button";

const ToDoList = () => {
    const [task, setTask] = useState(""); 
    const [tasks, setTasks] = useState<string[]>([]); 
    const [editingIndex, setEditingIndex] = useState<number | null>(null); 
    const [editText, setEditText] = useState(""); 

    const handleInputChange = (event: React.ChangeEvent<HTMLInputElement>) => {
        setTask(event.target.value);
    };

    const addTask = () => {
        if (task.trim() !== "") {
            setTasks([...tasks, task]); 
            setTask(""); 
        }
    };

    const deleteTask = (index: number) => {
        

        const userResponse = window.confirm(
            "Are you sure you want to delete this?"
          );
          if (userResponse) {
            const updatedTasks = tasks.filter((_, i) => i !== index);
            setTasks(updatedTasks);
          }
    };

    const startEditing = (index: number) => {
        setEditingIndex(index);
        setEditText(tasks[index]);
    };

    const handleEditChange = (event: React.ChangeEvent<HTMLInputElement>) => {
        setEditText(event.target.value);
    };

    const saveEdit = (index: number) => {
        const updatedTasks = tasks.map((t, i) => (i === index ? editText : t));
        setTasks(updatedTasks);
        setEditingIndex(null); 
    };

    const cancelEdit = () => {
        setEditingIndex(null); 
    };

    return (
        <div className="app-container">
                <h2>To-Do List</h2>
                <div className="input-container">
                    <input 
                        type="text" 
                        value={task} 
                        onChange={handleInputChange} 
                        placeholder="Enter a task..."
                    />
                    <Button onClick={addTask} label="Add Task" />
                </div>
                <ul>
                    {tasks.map((t, index) => (
                        <li key={index}>
                        {editingIndex === index ? (
                            <>
                                <input 
                                    type="text" 
                                    value={editText} 
                                    onChange={handleEditChange} 
                                    className="edit-input"
                                />
                                <div className="button-group">
                                    <Button onClick={() => saveEdit(index)} label="Save" />
                                    <Button onClick={cancelEdit} label="Cancel" />
                                </div>
                            </>
                        ) : (
                            <>
                                {t}
                                <div className="action-buttons">
                                    <Button onClick={() => startEditing(index)} label="Edit" />
                                    <Button onClick={() => deleteTask(index)} label="Delete" />
                                </div>
                            </>
                        )}
                    </li>
                    ))}
                </ul>
            </div>
    );
}

export default ToDoList;