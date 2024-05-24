## SimpleContact Project

SimpleContact is a user-friendly Python application designed to efficiently manage your contacts and notes in one place.

## Installation

1. To correctly set up the application, follow these steps:
   Open your terminal and navigate to the application's root directory.
2. Create a virtual environment for the application using the following command:

    - python3 -m venv .venv</p>

3. Activate your virtual environment (the specific command depends on your operating system):

   On Windows:

    - .venv\Scripts\activate</p>

   On macOS/Linux:

    - source .venv/bin/activate</p>

4. Install the required packages by running:

- pip install -r requirements.txt</p>
  To launch the application, execute the following command in the

terminal:

- python app.py</p>

For detailed information about a specific logging level, use the
following command:

- python app.py --log-level DEBUG</p>

#### Enjoy the result.

## General Commands

1.`help`:

- **Function:** `lambda args, book: "help"`
- **Description:** Display a list of available commands and their descriptions.
- **Steps:**
  1.Use the command `help` without any additional parameters.
  Review the list of commands and their detailed descriptions.
  2.Use the information provided to understand how to use each command.
- **Syntax:** `help`
- **Example:** `help`
- **Explanation:** This command will display a comprehensive list of all available commands along with their syntax and
  examples, helping the user understand how to interact with the application.

2.`exit`:

- **Function:** `lambda args, book: "exit"`
- **Description:** Terminate the session and exit the application.
- **Steps:**
  1.Use the command `exit` without any additional parameters.
  2.Confirm that you want to exit the application (if prompted).
  3.The application will close and your session will end.
- **Syntax:** `exit`
- **Example:** `exit`
- **Explanation:** This command will terminate the current session and close the application, ensuring that any ongoing
  tasks are properly handled before shutdown.

## Contact Commands

1.`contact-add`:

- **Function:** `add_contact`
- **Description:** Add a new contact with a name and phone number.
- **Steps:**
  1.Use the command contact-add followed by the contact's name and phone number.
  2.Ensure the phone number is in the correct format (only digits).
- **Syntax:** `contact-add *Name* *Phone*`
- **Example:** contact-add Oleksandr 📱0987654321
- **Explanation:** This command adds a new contact named Oleksandr with the phone number 📱0987654321 to your contact
  list.

2.`contact-add-phone`:

- **Function:** `add_phone`
- **Description:** Add a phone number to an existing contact.
- **Steps:**
  1.Use the command `contact-add-phone` followed by the contact's name and the new phone number.
  2.Ensure the contact already exists.
  3.Ensure the new phone number is in the correct format (only digits).
- **Syntax:** `contact-add-phone *Name* *Phone*`
- **Example:** contact-add-phone Oleksandr 📱0974567890
- **Explanation:** This command adds a second phone number 📱0974567890 to the contact named Oleksandr.

3.`contact-add-birthday`:

- **Function:** `add_birthday`
- **Description:** Add a birthday to a contact.
- **Steps:**
  1.Use the command `contact-add-birthday` followed by the contact's name and their birthday.
  2.Ensure the birthday is in the correct format (DD.MM.YYYY).
- **Syntax:** `contact-add-birthday *Name* *Birthday*`
- **Example:** `contact-add-birthday Oleksandr 01.06.1999`
- **Explanation:** This command adds the birthday June 1, 1999, to the contact named Oleksandr.

4.`contact-add-email`:

- **Function:** `add_email`
- **Description:** Add an email address to a contact.
- **Steps:**
  1.Use the command `contact-add-email` followed by the contact's name and their email address.
  2.Ensure the email address is in the correct format.
- **Syntax:** `contact-add-email *Name* *Email*`
- **Example:** `contact-add-email Oleksandr example@mail.com`
- **Explanation:** This command adds the email address example@mail.com📧 to the contact named Oleksandr.

5.`contact-add-address`:

- **Function:** `add_address`
- **Description:** Add an address to a contact.
- **Steps:**
  1.Use the command `contact-add-address` followed by the contact's name and their address.
- **Syntax:** `contact-add-address *Name* *Address*`
- **Example:** `contact-add-address Oleksandr WalkStreet 7`
- **Explanation:** This command adds the address WalkStreet 7📬 to the contact named Oleksandr.

6.`contact-edit-name`:

- **Function:** `edit_contact_name`
- **Description:** Edit the name of a contact.
- **Steps:**
  1.Use the command `contact-edit-name` followed by the current contact's name and the new name.
- **Syntax:** `contact-edit-name *Name* new-*Name*`
- **Example:** `contact-edit-name Oleksandr new-Yuriy`
- **Explanation:** This command changes the name of the contact from Oleksandr to Yuriy.

7.`contact-edit-phone`:

- **Function:** `edit_phone`
- **Description:** Edit the phone number of a contact.
- **Steps:**
  1.Use the command `contact-edit-phone` followed by the contact's name, the current phone number, and the new phone
  number.
  2.Ensure both phone numbers are in the correct format (only digits).
- **Syntax:** `contact-edit-phone *Name* *Phone* *new_phone*`
- **Example:** `contact-edit-phone Oleksandr 0987654321 0971234567`
- **Explanation:** This command changes the phone number 📱0987654321 of the contact named Oleksandr to 📱0971234567.

8.`contact-edit-address`:

- **Function:** `edit_address`
- **Description:** Edit the address of a contact.
- **Steps:**
  1.Use the command `contact-edit-address` followed by the contact's name, the current address, and the new address.
- **Syntax:** `contact-edit-address *Name* *Address* new-*Address*`
- **Example:** `contact-edit-address Oleksandr WalkStreet 7 new-OxfordStreet 12`
- **Explanation:** This command changes the address of the contact named Oleksandr from WalkStreet 7📬 to OxfordStreet
  12📬.

9.`contact-edit-email`:

- **Function:** `edit_email`
- **Description:** Edit the email address of a contact.
- **Steps:**
  1.Use the command `contact-edit-email` followed by the contact's name, the current email address, and the new email
  address.
  2.Ensure both email addresses are in the correct format.
- **Syntax:** `contact-edit-email *Name* *Email* new-*Email*`
- **Example:** `contact-edit-email Oleksandr example@mail.com new-goit@mail.com`
- **Explanation:** This command changes the email address of the contact named Oleksandr from example@mail.com📧 to
  goit@mail.com📧.

10.`contact-edit-birthday`:

- **Function:** `edit_birthday`
- **Description:** Edit the birthday of a contact.
- **Steps:**
  1.Use the command `contact-edit-birthday` followed by the contact's name and the new birthday.
  2.Ensure the birthday is in the correct format (DD.MM.YYYY).
- **Syntax:** `contact-edit-birthday *Name* *Birthday*`
- **Example:** `contact-edit-birthday Oleksandr 25.09.1992`
- **Explanation:** This command changes the birthday of the contact named Oleksandr to September 25, 1992.

11.`contact-delete`:

- **Function:** `contact_delete`
- **Description:** Delete a contact.
- **Steps:**
  1.Use the command `contact-delete` followed by the contact's name.
- **Syntax:** `contact-delete *Name*`
- **Example:** `contact-delete Oleksandr`
- **Explanation:** This command deletes the contact named Oleksandr from your contact list.

12.`contact-show`:

- **Function:** `show_contact`
- **Description:** Display information about a contact by name.
- **Steps:**
  1.Use the command `contact-show` followed by the contact's name.
- **Syntax:** `contact-show *Name*`
- **Example:** `contact-show Oleksandr`
- **Explanation:** This command displays all information about the contact named Oleksandr.

13.`contact-show-phone`:

- **Function:** `show_phone`
- **Description:** Display the phone number of a contact.
- **Steps:**
  1.Use the command `contact-show-phone` followed by the contact's name.
- **Syntax:** `contact-show-phone *Name*`
- **Example:** `contact-show-phone Oleksandr`
- **Explanation:** This command displays the phone number of the contact named Oleksandr.

14.`contact-show-birthday`:

- **Function:** `show_birthday`
- **Description:** Display the birthday of a contact.
- **Steps:**
  1.Use the command `contact-show-birthday` followed by the contact's name.
- **Syntax:** `contact-show-birthday *Name*`
- **Example:** `contact-show-birthday Oleksandr`
- **Explanation:** This command displays the birthday of the contact named Oleksandr.

15.`contact-birthdays`:

- **Function:** `show_upcoming_birthdays`
- **Description:** Show upcoming birthdays within a specified number of days.
- **Steps:**
  1.Use the command `contact-birthdays` followed by the number of days.
- **Syntax:** `contact-birthdays *days_to*`
- **Example:** `contact-birthdays 7`
- **Explanation:** This command displays all upcoming birthdays within the next 7 days.

16.`contact-show-all`:

- **Function:** `show_all`
- **Description:** Display information about all contacts.
- **Steps:**
  1.Use the command contact-show-all.
- **Syntax:** `contact-show-all`
- **Example:** `contact-show-all`
- **Explanation:** This command displays information about all contacts in your

## Note Commands

1.`note-add`:

- **Function:** `note_add`
- **Description:** Add a new note with a title and content.
- **Steps:**
  1.Use the command `note-add` followed by the title of the note and the content.
  2.Ensure the title and content are enclosed in quotation marks if they contain spaces.
- **Syntax:** `note-add *Title* *Content*`
- **Example:** `note-add "Meeting Notes" "Discuss project milestones and deadlines"`
- **Explanation:** This command adds a new note with the title "Meeting Notes" and the content "Discuss project
  milestones and deadlines".

2.`note-change`:

- **Function:** `note_change`
- **Description:** Change the content of an existing note.
- **Steps:**
  1.Use the command `note-change` followed by the title of the note and the new content.
  2.Ensure the title and new content are enclosed in quotation marks if they contain spaces.
- **Syntax:** `note-change *Title* *new_Content*`
- **Example:** `note-change "Meeting Notes" "Update project milestones and deadlines"`
- **Explanation:** This command changes the content of the note titled "Meeting Notes" to "Update project milestones and
  deadlines".

3.`note-find-by-title`:

- **Function:** `note_find_by_title`
- **Description:** Find a note by its title.
- **Steps:**
  1.Use the command `note-find-by-title` followed by the title of the note.
  2.Ensure the title is enclosed in quotation marks if it contains spaces.
- **Syntax:** `note-find-by-title *Title*`
- **Example:** `note-find-by-title "Meeting Notes"`
- **Explanation:** This command finds and displays the note with the title "Meeting Notes".

4.`note-find-by-tag`:

- **Function:** `note_find_by_tag`
- **Description:** Find notes by a specific tag.
- **Steps:**
  1.Use the command `note-find-by-tag` followed by the tag.
- **Syntax:** `note-find-by-tag *Tag*`
- **Example:** `note-find-by-tag "project"`
- **Explanation:** This command finds and displays all notes tagged with "project".

5.`note-delete`:

- **Function:** `note_delete`
- **Description:** Delete a note by its title.
- **Steps:**
  1.Use the command note-delete followed by the title of the note.
  2.Ensure the title is enclosed in quotation marks if it contains spaces.
  **Syntax:** `note-delete *Title*`
  **Example:** `note-delete "Meeting Notes"`
  **Explanation:** This command deletes the note with the title "Meeting Notes".

6.`note-show-all`:

- **Function:** `note_show_all`
- **Description:** Display all notes.
- **Steps:**
  1.Use the command note-show-all without any additional parameters.
  2.Syntax: `note-show-all`
- **Example:** `note-show-all`
- **Explanation:** This command displays all notes that are currently stored

#### Your team Pystreet Boys 🧑‍💻  