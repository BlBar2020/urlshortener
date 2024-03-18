import subprocess
import webbrowser
import time

def main():
    # Start Django development server
    subprocess.Popen(["python", "manage.py", "runserver", "8080"])

    # Wait for a few seconds to make sure the server has started
    time.sleep(3)

    # Open web browser and go to the Django dev server URL
    webbrowser.open("http://127.0.0.1:8080/")

if __name__ == "__main__":
    main()
