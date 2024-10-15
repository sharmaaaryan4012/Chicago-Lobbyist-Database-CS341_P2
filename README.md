# Chicago Lobbyist Database

Welcome to the **Chicago Lobbyist Database** project. This project is designed to manage and query information about lobbyists, their employers, and their clients in Chicago. The application provides various functionalities to interact with the database, such as retrieving statistics, searching for lobbyists, and managing their records.

## Table of Contents
- [Project Overview](#project-overview)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Contributors](#contributors)
- [License](#license)

## Project Overview

The Chicago Lobbyist Database application is a command-line interface (CLI) tool built with Python. It allows users to:
- Display general statistics about the lobbyists.
- Search for lobbyists by name.
- Retrieve detailed information about a specific lobbyist.
- Display the top N lobbyists based on their total compensation in a given year.
- Add a registration year for a lobbyist.
- Set the salutation for a lobbyist.

## Project Structure

The project consists of the following files:

- **main.py**: The main script that drives the CLI application.
- **objecttier.py**: Contains the functions to interact with the SQLite database.
- **requirements.txt**: Lists the dependencies required for the project.
- **Chicago_Lobbyists.db**: The SQLite database file (not included in the repository).

## Installation

To install and run this project, follow these steps:

1. **Clone the Repository**:
   ```sh
   git clone https://github.com/sharmaaaryan4012/Chicago-Lobbyist-Database-CS341_P2.git
   cd Chicago-Lobbyist-Database-CS341_P2
   ```

2. **Set Up the Environment**:
   Ensure you have Python installed (preferably Python 3.6+). Create and activate a virtual environment:
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**:
   ```sh
   pip install -r requirements.txt
   ```

4. **Database Setup**:
   Ensure the database file `Chicago_Lobbyists.db` is in the project directory. If not, create or obtain it.

## Usage

To run the application, execute the `main.py` script:
```sh
python main.py
```

You will be presented with a menu to choose from various commands:
1. Search for lobbyists by name.
2. Retrieve detailed information about a specific lobbyist.
3. Display the top N lobbyists based on their total compensation in a given year.
4. Add a registration year for a lobbyist.
5. Set the salutation for a lobbyist.
6. Exit the application by typing `x`.
