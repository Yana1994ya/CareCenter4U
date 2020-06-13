# Migrate the database:

To migrate the database structure to the latest version please run the following command:

`manage.py migrate`

# Load initial data:

To load the initial centers data please run the folowing command:

`manage.py loaddata centers/initial.json`

# Running the project:

Once migration and initial data load is complete , run the project using the following command:

`manage.py runserver`
