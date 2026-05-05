total_seats = 50
bookings = {}
booking_id = 1

while True:
    print("\n--- Railway Reservation System ---")
    print("1. Check Availability")
    print("2. Book Ticket")
    print("3. View Reservation")
    print("4. Cancel Ticket")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        available = total_seats - len(bookings)
        print("Available Seats:", available)

    elif choice == 2:
        if len(bookings) < total_seats:
            name = input("Enter Name: ")
            age = int(input("Enter Age: "))
            seat_no = len(bookings) + 1

            bookings[booking_id] = {
                "name": name,
                "age": age,
                "seat": seat_no
            }

            print("Ticket Booked Successfully")
            print("Booking ID:", booking_id)
            print("Seat Number:", seat_no)

            booking_id += 1
        else:
            print("No Seats Available")

    elif choice == 3:
        bid = int(input("Enter Booking ID: "))

        if bid in bookings:
            print("\nReservation Details")
            print("Name:", bookings[bid]["name"])
            print("Age:", bookings[bid]["age"])
            print("Seat Number:", bookings[bid]["seat"])
        else:
            print("Booking ID Not Found")

    elif choice == 4:
        bid = int(input("Enter Booking ID to Cancel: "))

        if bid in bookings:
            del bookings[bid]
            print("Ticket Cancelled Successfully")
        else:
            print("Invalid Booking ID")

    elif choice == 5:
        print("Thank You")
        break

    else:
        print("Invalid Choice")
