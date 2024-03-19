# Sports-Locker - A Player Locker CLI

As a former rugby player one of the biggest challenges was keeping track of locker  assignments for my fellow students in high school. Some of the biggest issues included:

* Students constantly forgetting or misplacing their locker combinations
* Needing to get into a students' locker if they are absent to access balls.
* Teachers having to print a hard copy of the locker inventory and start fresh every year

Sports-Locker is a Command Line Interface allowing users to query from a SQLAlchemy database of sports, lockers, and students. The database is set up with many-to-many relationships backrefered through the student table. Students can play many games and students can have many lockers.

Sports-locker allows the user to complete full CRUD actions through the CLI. The main menu options include:

* Search the database
* Print records from the database
* Create new records
* Update existing records
* Delete records from the database

This CLI is set up specifically for HIGH SCHOOL Sports student data, but could be adapted for other grade levels or educational disciplines.

## Installation

Fork and clone a copy of the repository. This project requires python3 and pip to be installed on your computer. Install dependencies by running pipenv install, then start up a virtual environment by running pipenv shell.

## Resources

To learn more about querying using SQLAlchemy: [SQLAlchemy Documentation](https://www.sqlalchemy.org/)

Check out Faker for all of your database seeding needs: [Faker Documentation](https://faker.readthedocs.io/en/master/)

Do your tables look awful? Check out Pandas to learn how to pretty-print your data! [Pandas Documentation](https://pandas.pydata.org/)

Test out user input verification: [Regex101](https://regex101.com/)

Display selectable options in the terminal and return the selection ID (or whatever you want!) using Inquirer: [Inquirer Documentation](https://pypi.org/project/inquirer/)

## Authors :black_nib:
- **Levis Ngigi** <[LevisNgigi](https://github.com/LevisNgigi)>

# License

This project is licensed under the [MIT License](LICENSE)