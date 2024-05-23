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
Syntax: `add-contact *Name* *Phone*`
Example: `add-contact Oleksandr 0977654321`
Description: Adds a new contact with a specified name and phone number.

- `add-phone *Name* *Phone*`:
Syntax: `add-phone *Name* *Phone*`
Example: `add-phone Oleksandr 0971234567`
Description: Adds an additional phone number to an existing contact.

- `add-email *Name* *Email*`:
Syntax: `add-email *Name* *Email*`
Example: `add-email Oleksandr example@mail.com`
Description: Adds an email address to a contact.

- `add-address *Name* *Address*`:
Syntax: `add-address *Name* *Address*`
Example: `add-address Oleksandr WalkStreet 7`
Description: Adds an address to a contact.

- `add-birthday *Name* *Birthday*`:
Syntax: `add-birthday *Name* *Birthday*`
Example: `add-birthday Oleksandr 01.06.1999`
Description: Adds a birthday to a contact.

- `edit-contact *Name* new-*Name*`:
Syntax: `edit-contact *Name* new-*Name*`
Example: `edit-contact Oleksandr new-Yuriy`
Description: Use this command to edit the name of a contact. The first parameter is the current name of the contact, and the second parameter is the new name you want to set.

- `edit-phone *Name* *Phone* *new_phone*`:
Syntax: `edit-phone *Name* *Phone* *new_phone*`
Example: `edit-phone Oleksandr 0987654321 1234567890`
Description: Use this command to edit the phone number of a chosen contact. The first parameter is the name of the contact whose phone number you want to edit. The second parameter is the current phone number, and the third parameter is the new phone number. Note: The phone number value should be exactly 10 digits. Any other values would be invalid.

- `edit-address *Name* *Address* new-*Address*`: 
Syntax: `edit-address *Name* *Address* new-*Address*`
Example: `edit-address Oleksandr WalkStreet 7 new-OxfordStreet 12`
Description: Use this command to edit the address of a contact. Multiple addresses are allowed.


- `edit-email *Name* *Email* new-*Email*`:
Purpose: Edit the email address of a contact. Multiple emails are allowed.
Syntax: `edit-email *Name* *Email* new-*Email*`
Example: `edit-email Oleksandr example@mail.com new-goit@mail.com`

- `show-birthdays *days_to*`:
Purpose: Show upcoming birthdays within a specified number of days.
Syntax: `show-birthdays *days_to*`
Example: `show-birthdays 7`

- `edit-birthday *Name* *Birthday*`:
Purpose: Edit the birthday of a contact.
Syntax: `edit-birthday *Name* *Birthday*`
Example: `edit-birthday Oleksandr 25.09.1992`

-`birthdays`:
Syntax: `birthdays`
Example: `birthdays`
Description: Use this command to view upcoming birthdays.

- `show-contact *Name*`:
Purpose: Display information about a contact by name.
Syntax: `show-contact *Name*`
Example: `show-contact Oleksandr`

- `show-all-contacts`:
Purpose: Display information about all contacts by name.
Syntax: `show-all-contacts`
Example: s`how-all-contacts`

-`change *Name*`:
Purpose: Change the contact information of a contact.
Syntax: `change *Name*`
Example: `change Oleksandr`
Details: This command would allow you to change various contact details such as phone number, address, etc., depending on the implementation.

-`all`:
Syntax: `all`
Example: `all`
Description: Show all information or records available in the system.


## Note Commands 

-`note-add`:
Syntax: `note-add *Note*`
Example: `note-add Buy groceries before Monday`
Description: Add a new note.

-`note-change`:
Syntax: `note-change *Note_ID* *New_Note*`
Example: `note-change 123 Buy groceries before Tuesday`
Description: Change an existing note to a new one.

-`note-find`:
Syntax: `note-find *Keyword*`
Example: `note-find groceries`
Description: Find notes containing the specified keyword.

-`note-delete`:
Syntax: `note-delete *Note_ID*`
Example: `note-delete 123`
Description: Delete a note by its ID.

-`note-show-all`:
Syntax: `note-show-all`
Example: `note-show-all`
Description: Show all available notes.

(Include any additional note-related commands here.)

Tour Team is:<span style="color:blue">  Pystreet Boys :smile: