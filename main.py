
from db import create_table, update, delete, delete_all, retrieve_all, close_connection
from func import create_event

def main():
    create_table()

    active = True

    while active:
        print("\nChoose an operation: INSERT / UPDATE / DELETE / DELETE ALL / RETRIEVE ALL / QUIT")
        choice = input("Enter your choice: ").strip().upper()

        if choice == "INSERT":
            try:
                title = input("Enter event title: ").strip().title()
                start_date = input("Enter start date (YYYY-MM-DD or 'Oct 31, 2025'): ").strip()
                end_date = input("Enter end date (YYYY-MM-DD or 'Oct 31, 2025'): ").strip()
                start_time = input("Enter starting time (HH:MM, 24-hour): ").strip()
                end_time = input("Enter ending time (HH:MM, 24-hour): ").strip()
                location = input("Enter event location: ").strip().title()
                description = input("Enter event description: ").strip().title()

                create_event(title, start_date, end_date, start_time, end_time, location, description)
            except ValueError as e:
                print(f"Error: {e}")
            except Exception as e:
                print(f"Unexpected error: {e}")

        elif choice == "UPDATE":
            retrieve_all()
            try:
                id = int(input("Enter event ID to update: "))
                new_title = input("Enter new event title: ").strip().title()
                new_startdate = input("Enter new event date (YYYY-MM-DD or 'Oct 31, 2025'): ").strip()
                new_enddate = input("Enter new event date (YYYY-MM-DD or 'Oct 31, 2025'): ").strip()
                new_starttime = input("Enter new start time (HH:MM): ").strip()
                new_endtime = input("Enter new end time (HH:MM): ").strip()
                new_location = input("Enter new event location: ").strip().title()
                new_description = input("Enter new description: ").strip().title()
                
                update(id, new_title, new_startdate, new_enddate, new_starttime, new_endtime, new_location, new_description)
            except ValueError:
                print("Please enter a valid numeric ID.")

        elif choice == "DELETE":
            retrieve_all()
            try:
                id = int(input("\nEnter event ID to delete: "))
                delete(id)
            except ValueError:
                print("Please enter a valid numeric ID.")

        elif choice == "DELETE ALL":
            confirm = input("Are you sure you want to DELETE ALL events? (yes/no): ").strip().lower()
            if confirm == "yes":
                delete_all()
            else:
                print("Delete all cancelled.")

        elif choice == "RETRIEVE ALL":
            retrieve_all()

        elif choice in ("QUIT", "EXIT"):
            active = False
            print("Goodbye!")

        else:
            print("Invalid choice! Please try again.")

    close_connection()

# if __name__ == "_main_":
main()
