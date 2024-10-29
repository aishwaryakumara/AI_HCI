# Mini Coding Assignment 2 (API Integration)

This project is my submission for HCI for AI Mini Coding Assignment 2. It is a simple "Hello World" application using the OpenAI API. 
This application generates a creative "Hello World" message using the GPT model and displays the result in the console. 

The project is written in Python and includes setup instructions.

## Table of Contents
- [Project Overview](#project-overview)
- [Technologies Used](#technologies-used)
- [Setup and Installation](#setup-and-installation)
- [Usage](#usage)
- [File Structure](#file-structure)

## Project Overview

This project is an application that uses APIs to generate a creative Hello World message. I have used OpenAI's GPT API and selected the gpt-4o-mini model. It makes a basic call to the API and displays the result in console. To make the response creative, I have prompted the system to converse like Professor Dumbledore from Harry Potter. I have loaded my API key from a `.env` file to maintain security.

## Technologies Used

- **Python**: Programming language used to build the project.
- **OpenAI API**: Used to generate a creative response.
- **Dotenv**: For managing environment variables securely.

## Setup and Installation

### Prerequisites

- Python 3.6 or higher
- OpenAI API key 
- `python-dotenv` package to load environment variables

### Installation Steps

1. **(Optional) Create a Virtual Environment**

I created a virtual environment to maintain versions and particular requiremnts separate from other projects

   Run the following commands in your terminal to create a virtual environment:

   ```bash
   python -m venv env_hciai
   source env_hciai/bin/activate  # On macOS/Linux
   env_hciai\Scripts\activate     # On Windows

1. **Clone the Repository**

   ```bash
   git clone https://github.com/aishwaryakumara/AI_HCI.git

2. **Install Dependencies**

I have used a few packages like load_dotenv and os to loads environment variables from a .env file into Python’s environment. This is to keep sensitive information from being pushed to GitHub.

   ```bash
   pip install -r requirements.txt


3. **(Optional) Set Up .env File**
You can choose to setup a .env file to maintain your API keys and load into into the python environment. Alternatively, you can also directly use the API key in the code

Create a .env file in the root directory to store your API key securely:
   ```bash
        OPENAI_API_KEY="your_api_key_here"

To prevent accidental sharing of the .env file, add it to .gitignore:
Create a .gitignore file and add .env


4. **Run the Script**
Excute using run button on IDE or run following command
   ```bash
   python miniproject.py


5. **Output**
The script will output a creative "Hello World" message in the console.
