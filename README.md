# SimpleContact Project

SimpleContact is a user-friendly Python application designed to efficiently manage your contacts and notes in one place.

## Installation

**To correctly set up the application, follow these steps:**

 Open your terminal and navigate to the application's root directory.
 Create a virtual environment for the application using the following command:

<span style="color:blue">python3 -m venv .venv

 Activate your virtual environment (the specific command depends on your operating system).
 Install the required packages by running:

<span style="color:blue">pip install -r requirements.txt

**To launch the application, execute the following command in the terminal:**
 
<!-- python task3.py /path/to/target/log_file -->

For detailed information about a specific logging level, use the following command:

<!-- python task3.py /path/to/target/log_file *logging_level* -->
 Enjoy the result.

## General Commands

- `hello`: Greeting.
- `help`: Display a list of available commands.
- `close` or `exit`: Terminate the session.

## Contact Commands

- `add-contact *Name* *Phone*`:
add Oleksandr 0987654321
Add a new contact with a name and phone number

- `add-phone *Name* *Phone*`:
add Oleksandr 0987654321 1234567890
Add an additional phone number to an existing contact.

- `add-email *Name* *Email*`:
add-email Oleksandr example@mail.com 
Add an email address to a contact.

- `add-address *Name* *Address*`:
add-address Oleksandr WalkStreet 7  
Add an address to a contact.
- `add-birthday *Name* *Birthday*`:
add-birthday Oleksandr 01.06.1999
Add a birthday to a contact.
- `show-contact *Name*`:
show-contact Oleksandr 
Display information about a contact by name.
- `show-all-contacts`: 
Show all contacts.
- `show-birthdays *days_to*`: 
integer parameter days_to: Show upcoming birthdays within a specified number of days.
- `edit-contact *Name* new-*Name*`: 
Edit the name of a contact.

- `edit-phone *Name* *Phone* *new_phone*`:
edit-phone Oleksandr 0987654321 1234567890  
Edit the phone number for the chosen contact,
First parameter is name of the contact you want to edit phone number,
Second parameter is a phone number to change,
Note: value should be only 10 digits. Any other values would be invalid.

- `edit-email *Name* *Email* new-*Email*`: 
multiple emails allowed: Edit the email address of a contact.
- `edit-address *Name* *Address* new-*Address*`: 
multiple addresses allowed: Edit the address of a contact.
- `edit-birthday *Name* *Birthday*`: 
Edit the birthday of a contact.
- `delete-contact *Name*`: 
Delete a contact by name.

## Note Commands 

(Include any additional note-related commands here.)

Tour Team is:<span style="color:blue">  Pystreet Boys :smile: