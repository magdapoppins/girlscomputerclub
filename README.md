# Girls Computer Club Homepage

## Getting started

This project uses Django and Python 3. To get started, set up a virtual environment in the repository and activate it:
```
python3 -m venv venv
source venv/bin/activate
```
You should see a `(venv)` text appear somewhere in your prompt to signify that the virtual environment is active. The venv can be deactivated once you are done by calling `deactivate`.

Then, run `pip install -r requirements.txt` to install Django.

Migrate the sqlite3 database: `python manage.py migrate` 

Start the application: `python manage.py runserver` 

Create a admin for the project: `python manage.py createsuperuser`  

You can now log into `http://127.0.0.1:8000/admin/` to modify the site.  

## Deployment

1. Make sure the code you want deployed is in `master`. 
2. Log in to our account on PythonAnywhere.
3. Open the projects bash console.
4. Change directory into `/www.girlscomputerclub.com`
5. Run `git pull`.
6. Collect the static files `python manage.py collectstatic`.
7. Check that everything looks ok! 🎉

## Contributing

You can contribute to this project by selecting a ticket from `Issues`. Then, fork the project, clone it to your computer, make your changes, commit them and when you're done, create a pull request back from the fork to this repository. 


