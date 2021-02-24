def add_time(start, duration, day_of_week = False):

  # Set up indices and lists
  days_of_the_week_index = {"monday":0, "tuesday":1,"wednesday":2,"thursday":3,"friday":4,"saturday":5,"sunday":6}

  days_of_the_week_list = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]

  # Set up variables
  duration_tuple = duration.partition(":")
  duration_hours = int(duration_tuple[0])
  duration_minutes = int(duration_tuple[2])

  start_tuple = start.partition(":")
  start_minutes_tuple = start_tuple[2].partition(" ")
  start_hours = int(start_tuple[0])
  start_minutes = int(start_minutes_tuple[0])
  am_or_pm = start_minutes_tuple[2]
  am_or_pm_flip = {"AM":"PM", "PM":"AM"}

  end_minutes = start_minutes + duration_minutes

  # Check if end_minutes is at least 60
  if (end_minutes >=60):
    start_hours += 1
    end_minutes = end_minutes % 60

  amount_of_am_pm_flips = (start_hours + duration_hours)//12

  amount_of_days = (duration_hours//24)
  end_hours = (start_hours + duration_hours) % 12

  # Format end_minutes
  end_minutes = end_minutes if end_minutes > 9 else "0" + str(end_minutes)

  end_hours = end_hours = 12 if end_hours == 0 else end_hours

  if (am_or_pm == "PM" and start_hours + (duration_hours % 12) >= 12):
    amount_of_days += 1

  am_or_pm = am_or_pm_flip[am_or_pm] if amount_of_am_pm_flips % 2 == 1 else am_or_pm

  my_return_time = str(end_hours) + ":" + str(end_minutes) + " " + am_or_pm

  # Check status for day_of_week
  if (day_of_week):
    day_of_week = day_of_week.lower()
    idx = int((days_of_the_week_index[day_of_week]) + amount_of_days) % 7
    new_day = days_of_the_week_list[idx]
    my_return_time += ", " + new_day

  # Check the amount of days
  if (amount_of_days == 1):
    return my_return_time + " " + "(next day)"
  elif (amount_of_days > 1):
    return my_return_time + " (" + str(amount_of_days) + " days later)"

  return my_return_time
