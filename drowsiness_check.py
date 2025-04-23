def check_drowsiness(blinks):
    count = 0
    for state in blinks:
        if state == "closed":
            count += 1
            if count >= 3:
                return True
        else:
            count = 0
    return False
