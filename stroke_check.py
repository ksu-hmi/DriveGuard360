def check_stroke(face_data):
    count = 0
    for state in face_data:
        if state == "drooping":
            count += 1
            if count >= 2:
                return True
        else:
            count = 0
    return False
