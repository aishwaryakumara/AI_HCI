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

Instructions:
   Run the following commands in your terminal to create a virtual environment:

   ```bash
   python -m venv env_hciai
   source env_hciai/bin/activate  # On macOS/Linux
   env_hciai\Scripts\activate     # On Windows
   ```

2. **Clone the Repository**

Instructions:
   ```bash
   git clone https://github.com/aishwaryakumara/AI_HCI.git
   ```

3. **Install Dependencies**

I have used a few packages like load_dotenv and os to loads environment variables from a .env file into Python’s environment. This is to keep sensitive information from being pushed to GitHub.

Instructions:
   ```bash
   pip install -r requirements.txt
   ```


4. **(Optional) Set Up .env File**
I have set a .env file to store my API Key Securely. I have included this env file in .gitignore so that it does not get added to Github when I push my code.

Instructions:
You can choose to setup a .env file to maintain your API keys and load into into the python environment. Alternatively, you can also directly use the API key in the code

Create a .env file in the root directory to store your API key securely:
   ```bash
    OPENAI_API_KEY="your_api_key_here"
```

To prevent accidental sharing of the .env file, add it to .gitignore:
Create a .gitignore file and add .env


5. **Run the Script**

Instructions:
Excute using run button on IDE or run following command
   ```bash
   python miniproject.py
   ```

5. **Output**
The script will output a creative "Hello World" message in the console.

## Reflection

This project was very valuable and gave me good experience in working with the OpenAI API. The following are the steps I followed while creating this application and my learning points:

- I began by reading the OpenAI documentation to understand the process of using the API. I created a new project and set up a virtual environment to keep my python version and dependencies isolated from other projects.

- I generated a project based API keys on OpenAI Setting and saved my secret key. Initially, I used the API key directly in the code to generate a basic "Hello World" message. 
- My prompt was - 
    Generate a creative Hello World message 

Here is a screenshot of the output:

 ![Basic Hello World Output](/images/basicss.png)

- I explored more prompting by instructing the API to respond as Dumbledore from Harry Potter. This approach generated a creative "Hello World" message. Here is a screenshot of the creative output:

- My prompt was - 

    messages=[{"role": "system", "content": "You are a creative writer who talks like Dumbledore from Harry Potter. Give me 5 sentences"},
            {"role": "user", "content": "Generate a creative Hello World message"}]

   ![Creative "Hello World" message as Dumbledore](/images/hpss.png)

- When I tried pushing the project to GitHub, the platform blocked it because my API key was exposed in the code. To resolve this, I created a `.env` file to store the API key securely and added `.env` to `.gitignore` to prevent it from being tracked by Git. This ensured that my sensitive information was secure.


