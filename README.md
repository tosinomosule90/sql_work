# Event Scheduler 📅

**Brief description**

A small command-line Event Scheduler written in Python that stores events in a local SQLite database (`events.db`). It provides simple CRUD operations via a text-based menu: INSERT, UPDATE, DELETE, DELETE ALL, RETRIEVE ALL, and QUIT.

---

## How it works 🔧

- `main.py` runs a loop that prompts the user for commands and input values.
- `func.py` contains event validation and `create_event()` which:
  - parses dates and times (supports `YYYY-MM-DD` and `Mon DD, YYYY` formats),
  - validates time format (`HH:MM`, 24-hour),
  - ensures events aren’t scheduled in the past, have valid durations, and don’t conflict with existing events,
  - checks location validity using `Rough_code.location`'s `validate_location()` / `available_locations`.
- `db.py` manages a SQLite DB (`events.db`) and implements: table creation, insert, update, delete, delete_all, retrieve_all, and a check that prevents duplicate start-time events.

---

## Quick start 🚀

1. Ensure you have Python 3.8+ installed.
2. (Optional) Create and activate a virtual environment:
   ```bash
   python -m venv .venv
   .\.venv\Scripts\activate
   ```
3. Run the app:
   ```bash
   python main.py
   ```
4. Use commands shown in the prompt (e.g., `INSERT`, `RETRIEVE ALL`), then follow input prompts for event fields.

---

## Important notes & formats ⚠️

- Date formats accepted: `YYYY-MM-DD` or `Oct 31, 2025`.
- Time format: `HH:MM` (24-hour).
- Events cannot start in the past and cannot exceed a 360-day duration.
- Location validation depends on `Rough_code.location` — ensure that module is available or replace the validation logic.

---

## File overview 📁

- `main.py` — CLI menu and user interaction.
- `func.py` — input parsing and event validation logic.
- `db.py` — SQLite connection and CRUD functions.

---

## Requirements 📦

- No third-party packages required — uses Python standard library (`sqlite3`, `datetime`).
- Recommended Python: 3.8+

To verify your environment:

```bash
# No pip installs required; just ensure Python 3.8+
python --version
```

## Sample Run Output 🖥️

Below is a sample interaction showing an `INSERT` followed by `RETRIEVE ALL`:

```text
Choose an operation: INSERT / UPDATE / DELETE / DELETE ALL / RETRIEVE ALL / QUIT
Enter your choice: INSERT
Enter event title: Team Meeting
Enter start date (YYYY-MM-DD or 'Oct 31, 2025'): 2026-02-15
Enter end date (YYYY-MM-DD or 'Oct 31, 2025'): 2026-02-15
Enter starting time (HH:MM, 24-hour): 14:00
Enter ending time (HH:MM, 24-hour): 15:00
Enter event location: Boardroom
Enter event description: Monthly planning
Event 'Team Meeting' created successfully!

Choose an operation: INSERT / UPDATE / DELETE / DELETE ALL / RETRIEVE ALL / QUIT
Enter your choice: RETRIEVE ALL
                    ID: 1
                    Title: Team Meeting
                    Start: 2026-02-15 14:00
                    End: 2026-02-15 15:00
                    Location: Boardroom
                    Description: Monthly Planning
```

---

