Sure! Here's a clean and concise `README.md` file **without** any code blocks, focusing purely on what the project does, how it works, and how to use it:

---

# Python Script Output Monitoring with Ansible Callback Plugin

## Overview

This project demonstrates how to **monitor and stream output** from a Python script during an Ansible playbook run using a **custom Ansible callback plugin**.

The use case focuses on tasks that dynamically generate output (e.g., writing to a file), and how that output can be captured and displayed in real-time while the Ansible playbook is running.

---

## Components

- **Ansible Playbook**: Executes a Python script and wraps it between two debug messages.
- **Python Script**: Appends lines to a monitored file at regular intervals.
- **Callback Plugin**: A custom Ansible plugin that watches the monitored file and streams any new content to the console.

---

## How It Works

1. The playbook runs a Python script which writes new lines to a file every few seconds.
2. A custom callback plugin detects any task with "monitor" in its name.
3. When such a task begins, the plugin starts monitoring the file.
4. As the Python script appends new lines to the file, the plugin reads and displays them in near real-time.
5. When the task completes, the plugin stops monitoring.

---

## Folder Structure

- `write-lines.py`: The Python script that generates output.
- `monitored_file.txt`: The output file being monitored.
- `callback_plugins/prepend_name.py`: The custom callback plugin.
- `playbook.yml`: The Ansible playbook that triggers the script and the plugin.

---

## Requirements

- Python 3
- Ansible
- Basic understanding of Ansible playbooks and plugins

---

## Usage

1. Place all files in the same directory structure.
2. Ensure Ansible is configured to recognize the `callback_plugins` directory.
3. Run the Ansible playbook.
4. Observe real-time output streaming from the Python script while the playbook runs.

---

Let me know if you want a version of this README with code examples included!
