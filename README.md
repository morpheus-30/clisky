# Clisky ⚡

AI-Powered Linux CLI Command Recommender

Clisky lets you turn natural language into Linux commands.

Example:

```
clisky "list all running docker containers"
```

Output:

```
docker ps
```

Optionally execute the command directly from the terminal.

---

## Features

- Natural language → Linux CLI commands
- Detects your Linux distribution automatically
- Secure API key setup
- Interactive command execution
- Lightweight CLI tool

---

## Installation

Clone the repository:

```
git clone https://github.com/YOUR_USERNAME/clisky.git
cd clisky
```

Install:

```
pip install .
```

For development mode:

```
pip install -e .
```

---

## Usage

Run:

```
clisky "find large files"
```

Example output:

```
Suggested Command:
find . -type f -size +100M
```

Then choose whether to execute the command.

---

## First Run Setup

On first run, Clisky will ask for your **Groq API key**.

Get one from:

https://console.groq.com/

The key will be stored locally.

---

## Example Commands

Find large files:

```
clisky "find large files in this folder"
```

Show open ports:

```
clisky "show open ports"
```

List hidden files:

```
clisky "list hidden files"
```

---

## Project Structure

```
clisky/
 ├── clisky/
 │   ├── __init__.py
 │   ├── cli.py
 │   └── model.py
 │
 ├── setup.py
 ├── requirements.txt
 └── README.md
```

---

## Tech Stack

- Python
- Click (CLI)
- Groq API
- OpenAI SDK compatibility

---

## Future Ideas

- Multiple command suggestions
- Streaming responses
- Shell auto-completion
- Command safety detection

---

## License

MIT License
