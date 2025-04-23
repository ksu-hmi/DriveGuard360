from drowsiness_check import check_drowsiness
from stroke_check import check_stroke
from alerts import alert_driver
from logs import show_logs

def menu():
    while True:
        print("\nWelcome to DriveGuard360")
        print("1. Run drowsiness check")
        print("2. Run stroke check")
        print("3. Show logs")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            blinks = ["open", "open", "closed", "closed", "closed"]
            if check_drowsiness(blinks):
                alert_driver("Drowsiness detected")
        elif choice == "2":
            face_data = ["normal", "normal", "drooping", "drooping"]
            if check_stroke(face_data):
                alert_driver("Stroke warning!")
        elif choice == "3":
            show_logs()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    menu()


