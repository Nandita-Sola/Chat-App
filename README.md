ChatApp
A real-time chat application built using Django, Django Channels, and WebSockets.

Requirements
Before you begin, ensure that you have the following installed:

Python (version 3.x)
Django (version 5.1.5 or above)
Django Channels
Setup Instructions
Follow the steps below to set up and run the project locally.

1. Clone the repository
Clone the project repository to your local machine.

bash
Copy
git clone https://github.com/your-username/chatapp.git
Navigate to the project folder:

bash
Copy
cd chatapp
2. Set up a virtual environment
To avoid conflicts with other Python packages, it's recommended to use a virtual environment. You can create and activate a virtual environment by following these steps:

For Windows:
bash
Copy
python -m venv myenv
myenv\Scripts\activate
For macOS/Linux:
bash
Copy
python3 -m venv myenv
source myenv/bin/activate
3. Install dependencies
Once the virtual environment is activated, install the required dependencies using pip:

bash
Copy
pip install -r requirements.txt
If you don't have a requirements.txt file, you can install the dependencies manually:

bash
Copy
pip install django
pip install channels
4. Set up the database
Run the following commands to set up the database:

bash
Copy
python manage.py makemigrations
python manage.py migrate
This will apply the necessary migrations to create the database tables for your project.

5. Run the development server
Now, you can run the Django development server:

bash
Copy
python manage.py runserver
This will start the development server at http://127.0.0.1:8000/.

6. Open in Browser
Open your browser and navigate to http://127.0.0.1:8000/.

You will see a page with a button to "Enter the General Chat Room."
Clicking the button will take you to the General Chat Room, where you can start chatting with other users.
File Structure Overview
Here's a brief overview of the project files:

graphql
Copy
chatapp/
├── chat/
│   ├── consumers.py      # WebSocket consumer logic
│   ├── routing.py        # WebSocket URL routing
│   ├── urls.py           # Regular URL routing for views
│   ├── views.py          # Regular Django views for pages
│   ├── templates/
│   │   └── chat/
│   │       ├── index.html  # Home page template
│   │       └── room.html   # Chat room template
│   ├── static/            # Static files (JavaScript, CSS, etc.)
│   └── ...
├── chatapp/
│   ├── asgi.py            # ASGI configuration for WebSockets
│   ├── settings.py        # Django settings
│   ├── urls.py            # Main project URL routing
│   ├── wsgi.py            # WSGI entry point for deployment
│   └── ...
└── manage.py              # Django manage.py command-line utility
Troubleshooting
If you run into issues, check the following:

WebSocket connection issues:

Ensure that the WebSocket URL is correct: ws://127.0.0.1:8000/ws/chat/<room_name>/.
Open your browser's Developer Tools (F12) and check the "Console" and "Network" tabs for WebSocket errors.
Missing Static Files:

Ensure your static files (CSS, JS, etc.) are correctly placed under the static/ folder in your chat app.
