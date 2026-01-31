


from datetime import datetime, timedelta
from db import insert, event_exists
from Rough_code.location import validate_location, available_locations

def parse_date(date_str):
    for fmt in ("%Y-%m-%d", "%b %d, %Y"):
        try:
            return datetime.strptime(date_str, fmt)
        except ValueError:
            continue
    raise ValueError("Invalid date format. Please use YYYY-MM-DD or 'Oct 31, 2025'.")
        
def create_event(title, start_date, end_date, start_time, end_time, location, description):
    now = datetime.now()
    max_duration = timedelta(days=360)
    min_duration = timedelta(minutes=1)

    start_date_obj = parse_date(start_date)
    end_date_obj = parse_date(end_date)

    if not validate_location(location):
        raise ValueError(f"Invalid location. Choose from: {', '.join(available_locations).title()}")
    
    try:
        start_time_obj = datetime.strptime(start_time, "%H:%M")
        end_time_obj = datetime.strptime(end_time, "%H:%M")
    except ValueError:
        raise ValueError("Invalid time format. Please use HH:MM(24-hour format).")
    
    start_dt = datetime.combine(start_date_obj, start_time_obj.time())
    end_dt = datetime.combine(end_date_obj, end_time_obj.time())

    if start_dt < now:
        raise ValueError("Start time cannot be in the past.")
    
    if end_dt <= start_dt:
        raise ValueError("End time must be after start time.")
        
    if start_dt - now > max_duration:
        raise ValueError("Event cannot be scheduled more than 360 days in the future.")
    
    if end_dt - start_dt > max_duration:
        raise ValueError("Event duration cannot exceed 360 days.")
    
    if end_dt - start_dt < min_duration:
        raise ValueError("Event duration must be more than a minute.")
    
    start_time_str = start_time_obj.strftime("%H:%M")
    end_time_str = end_time_obj.strftime("%H:%M")
    
    if event_exists(start_date_obj.date(), start_time_str):
        raise ValueError("Another event already starts at this exact time.")
  
    insert(
        title, 
        start_date_obj.date(), 
        end_date_obj.date(), 
        start_time_str, 
        end_time_str, 
        location, 
        description
    )
    
    print(f"Event '{title}' created successfully!")