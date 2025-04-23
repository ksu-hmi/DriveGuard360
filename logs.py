def show_logs():
    try:
        with open("log.txt", "r") as log:
            print("\n--- LOG HISTORY ---")
            print(log.read())
    except FileNotFoundError:
        print("\nNo logs found.")
