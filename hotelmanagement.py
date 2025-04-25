class Hostel:
    def __init__(self, total_rooms):
        self.total_rooms = total_rooms
        self.rooms = {i: None for i in range(1, total_rooms + 1)}  # room_number: student_name

    def assign_room(self, student_name):
        for room, occupant in self.rooms.items():
            if occupant is None:
                self.rooms[room] = student_name
                print(f"Room {room} assigned to {student_name}.")
                return
        print("Sorry, no rooms available.")

    def vacate_room(self, room_number):
        if room_number in self.rooms and self.rooms[room_number] is not None:
            print(f"Room {room_number} vacated by {self.rooms[room_number]}.")
            self.rooms[room_number] = None
        else:
            print("Room is already vacant or invalid.")

    def view_occupancy(self):
        print("\nCurrent Room Occupancy:")
        for room, occupant in self.rooms.items():
            status = occupant if occupant else "Vacant"
            print(f"Room {room}: {status}")

# Sample usage
def main():
    hostel = Hostel(total_rooms=5)  # You can change the total number of rooms

    while True:
        print("\n--- Hostel Management ---")
        print("1. Assign Room")
        print("2. Vacate Room")
        print("3. View Occupancy")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            name = input("Enter student name: ")
            hostel.assign_room(name)
        elif choice == '2':
            try:
                room_no = int(input("Enter room number to vacate: "))
                hostel.vacate_room(room_no)
            except ValueError:
                print("Please enter a valid room number.")
        elif choice == '3':
            hostel.view_occupancy()
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
