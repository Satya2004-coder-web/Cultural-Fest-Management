from default import Event

class EM:
    def __init__(self):
        self.events = []

    def display_events(self):
        if not self.events:
            print("No events available.")
            return

        print("\n--- Event List ---")
        for idx, event in enumerate(self.events, start=1):
            print(f"{idx}. {event}")

    def add_event(self):
        name = input("Enter event name: ")
        date = input("Enter event date (YYYY-MM-DD): ")
        status = input("Enter event status (upcoming/ongoing/over): ").lower()

        if status not in ['upcoming', 'ongoing', 'over']:
            print("Invalid status. Event not added.")
            return

        new_event = Event(name, date, status)
        self.events.append(new_event)
        print("Event added successfully.")

    def update_event(self):
        self.view_events()
        if not self.events:
            return

        try:
            index = int(input("Enter the event number to update: ")) - 1
            if index < 0 or index >= len(self.events):
                print("Invalid event number.")
                return

            print("Leave fields empty to keep existing values.")
            name = input("Enter new event name: ")
            date = input("Enter new event date (YYYY-MM-DD): ")
            status = input("Enter new event status (upcoming/ongoing/over): ").lower()

            if name:
                self.events[index].name = name
            if date:
                self.events[index].date = date
            if status in ['upcoming', 'ongoing', 'over']:
                self.events[index].status = status

            print("Event updated successfully.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    def delete_event(self):
        self.view_events()
        if not self.events:
            return

        try:
            index = int(input("Enter the event number to delete: ")) - 1
            if index < 0 or index >= len(self.events):
                print("Invalid event number.")
                return

            deleted_event = self.events.pop(index)
            print(f"Event '{deleted_event.name}' deleted successfully.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")
