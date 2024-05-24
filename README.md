## Introduction

Requirement 2: Use a common message broker (e.g., Centrifuge, RabbitMQ) to handle the following scenario:

- There is a list of tasks, each task involves editing a picture or an audio file. At any given time, only one person A can receive and edit a particular task. 
- During the time a file is being edited by A, others (person B, C, D, etc) can view but cannot edit it. 
- Only when the task is completed, the others can open and edit it. 

## Setup

### Start RabbitMQ using Docker

```bash
docker run -it --rm --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:3.13-management
```

### Create python virtual environment

```bash
python -m venv venv
```

### Activate venv

```bash
source venv/bin/activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

## Usage

### Create a subcriber for receive new task

```bash
python src/task_subscriber.py
```

### Create subcribers of other people B, C, D in 3 different terminal windows:

```bash
python src/status_subscriber.py
```

### Create task

```bash
python src/create_task.py [task_name]
```

For example:

```bash
python src/create_task.py task_1 
```

After this command is executed, the task subcriber will log:

```
New task: task_1
```

### Assign task

```
python src/publish_status.py [task_name] [person] [status]
```

`status` includes `in_progress`, `completed`

For example:

```
python src/publish_status.py task_1 person_a in_progress
```

After this command is executed, 3 status subcribers will log:

```
Task task_1 is in_progress
Only person_a can edit this task, others can view it
```

### Complete task

Change the task status to completed. For example:

```
python src/publish_status.py task_1 person_a completed
```

After this command is executed, 3 status subcribers will log:

```
Task task_1 is completed
This task is open for editing by anyone
```
