# Full Stack Developer Test

Welcome to the AgVend Digital Solutions full stack developer test. Follow the instructions below to set up your development environment using GitHub Codespaces.

## Setup Instructions

1. **Access the Repository:**
   - Ensure you have access to this repository. If you do not have access, please request access from the repository owner.

2. **Create a Codespace:**
   - Click the `Code` button at the top right of the repository page.
   - Select `Open with Codespaces` from the dropdown menu.
   - If you do not see `Codespaces` as an option, click `New codespace` and select the appropriate branch (usually `main`).

3. **Initialize the Environment:**
   - The Codespace will automatically set up the environment based on the configuration files provided in the repository.
   - Once the environment is ready, you can start working on the tasks as described below.

## Tasks

### Backend Development
- Implement the following API endpoints:
  - `POST /add-book` - Add a new book.
  - `GET /books/<isbn>` - Retrieve book details.
  - `PUT /books/<isbn>` - Update stock quantity.
  - `DELETE /books/<isbn>` - Delete a book.

### Frontend Development
- Create a user interface to interact with the above API endpoints.
  - Use Django templates or React.
  - Ensure the interface is user-friendly and responsive.

### Database Management
- Write SQL queries to:
  - Retrieve books by a specific author.
  - Find the top 5 most expensive books.
  - Update the price of a book by its ISBN.
  - Delete all books with zero stock.
- Explain how you would optimize the database for performance.

### Code Review and Debugging
- Review and fix the provided code snippet in `core/views.py`.
- Explain the issues and your fixes in a separate document.

## Environment Details

- **Python Version:** 3.9
- **Django Version:** 5.0.4
- **Database:** SQLite (for simplicity, replace with PostgreSQL if needed)

Feel free to reach out if you have any questions or encounter any issues.
