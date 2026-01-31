import sqlite3

conn = sqlite3.connect('events.db')
cur = conn.cursor()

def create_table():
    cur.execute("DROP TABLE IF EXISTS events")

    cur.execute(
        """
            CREATE TABLE IF NOT EXISTS events (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                start_date TEXT,
                end_date TEXT,
                start_time TEXT NOT NULL,
                end_time TEXT NOT NULL,
                location TEXT,
                description TEXT
            )
        """
    )
    conn.commit()
    # print("Table created successfully")
create_table()

def event_exists(start_date, start_time):
    conn = sqlite3.connect('events.db')
    cur = conn.cursor()

    cur.execute(
        """
            SELECT * FROM events WHERE start_date = ? AND start_time = ?
        """, (start_date, start_time))
    
    result = cur.fetchone()
    conn.close()
    return result is not None

def insert(title, start_date, end_date, start_time, end_time, location, description):
    cur.execute("INSERT INTO events (title, start_date, end_date, start_time, end_time, location, description) VALUES (?, ?, ?, ?, ?, ?, ?)", (title, start_date, end_date, start_time, end_time, location, description))
    conn.commit()
    print(f"Inserted {title} successfully")

def update(id, new_title, new_startdate, new_enddate, new_starttime, new_endtime, new_location, new_description):
    cur.execute(
        "UPDATE events SET title = ?, start_date = ?, end_date = ?, start_time = ?, end_time = ?, location  = ?, description = ? WHERE id = ?",
        (new_title, new_startdate, new_enddate, new_starttime, new_endtime, new_location, new_description, id)
    )
    conn.commit()
    print(f"Updated events with ID: {id} successfully")

def delete(id):
    cur.execute("DELETE FROM events WHERE id= ?", (id, ))
    conn.commit()
    print(f"Deleted events with ID: {id} successfully")

def delete_all():
    cur.execute("DELETE FROM events")
    conn.commit()
    print("All events deleted successfully")

def retrieve_all():
    cur.execute("SELECT * FROM events")
    rows = cur.fetchall()
    if rows:
        for row in rows:
            print(
                f"""
                    ID: {row[0]}
                    Title: {row[1]}
                    Start: {row[2]} {row[4]}
                    End: {row[3]} {row[5]}
                    Location: {row[6]}
                    Description: {row[7]}
                """
                )
    else:
        print("No events found.")

def close_connection():
    conn.close()