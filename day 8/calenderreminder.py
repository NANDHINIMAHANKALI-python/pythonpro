import datetime

reminders = {}

def add_reminder():
    date_str = input("Enter the date (YYYY-MM-DD): ")
    time_str = input("Enter the time (HH:MM): ")
    reminder_text = input("Enter the reminder text: ")

    try:
        date = datetime.datetime.strptime(date_str, "%Y-%m-%d")
        time = datetime.datetime.strptime(time_str, "%H:%M")

        
        datetime_obj = datetime.datetime(date.year, date.month, date.day, time.hour, time.minute)

        if datetime_obj in reminders:
            reminders[datetime_obj].append(reminder_text)
        else:
            reminders[datetime_obj] = [reminder_text]

        print("Reminder added successfully!")

    except ValueError:
        print("Invalid date or time format. Use YYYY-MM-DD for date and HH:MM for time.")

def view_reminders():
    if not reminders:
        print("No reminders to display.")
        return

    for date, reminder_list in sorted(reminders.items()):
        print(f"\nReminders for {date.strftime('%Y-%m-%d %H:%M')}:")

        for i, reminder in enumerate(reminder_list, start=1):
            print(f"{i}. {reminder}")

def delete_reminder():
    view_reminders()
    if not reminders:
        return

    try:
        index_to_delete = int(input("Enter the index of the reminder to delete: ")) - 1

        dates = sorted(reminders.keys())
        date_to_delete = dates[index_to_delete]

        if len(reminders[date_to_delete]) == 1:
            del reminders[date_to_delete]
        else:
            del reminders[date_to_delete][index_to_delete]

        print("Reminder deleted successfully!")

    except (ValueError, IndexError):
        print("Invalid input. Please enter a valid index.")

def main():
    while True:
        print("\nChoose an action:")
        print("1 - Add reminder")
        print("2 - View reminders")
        print("3 - Delete reminder")
        print("4 - Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_reminder()
        elif choice == "2":
            view_reminders()
        elif choice == "3":
            delete_reminder()
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()
