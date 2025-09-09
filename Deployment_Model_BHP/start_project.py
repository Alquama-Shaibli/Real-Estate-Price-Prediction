import subprocess
import webbrowser
import time
import os

# Start Flask backend
backend_dir = os.path.join(os.path.dirname(__file__), 'Server')
backend_process = subprocess.Popen([
    'python', 'server.py'
], cwd=backend_dir)

# Wait a moment for backend to start
print("Starting backend...")
time.sleep(2)

# Start simple HTTP server for frontend
frontend_dir = os.path.join(os.path.dirname(__file__), 'Client')
frontend_process = subprocess.Popen([
    'python3', '-m', 'http.server', '8000'
], cwd=frontend_dir)

# Wait a moment for frontend server to start
print("Starting frontend server...")
time.sleep(2)

# Open frontend in default browser
webbrowser.open('http://localhost:8000/index.html')

print("Both backend and frontend are running.")

try:
    backend_process.wait()
except KeyboardInterrupt:
    print("Shutting down...")
    backend_process.terminate()
    frontend_process.terminate()
