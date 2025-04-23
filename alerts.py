def alert_driver(message):
    print(f"ALERT: {message}")
    with open("log.txt", "a") as log:
        log.write(message + "\n")
