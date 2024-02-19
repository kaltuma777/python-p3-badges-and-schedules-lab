def badge_maker(name):
    return f"Hello, my name is {name}."

print(badge_maker("Kaltuma"))

def batch_badge_creator(names):
    badges = ['Hello, my name is ' + item + '.' for item in names]
    return badges        

print(batch_badge_creator(["Gadafi","Nasir"]))

def assign_rooms(names):
    rooms = range(1, len(names) + 1)
    return [f"Hello, {name}! You'll be assigned to room {room}!" for room, name in enumerate(names, start = 1)]

print(assign_rooms(["Gadafi", "Samir", "Ayub", "Abdi", "Esther", "Rachel", "Mohamed"]))

def printer(names):
    badges = batch_badge_creator(names)
    room_assignment = assign_rooms(names)

    for item in badges:
        print(item)

    for room in room_assignment:
        print(room)

printer(["Gadafi", "Nasir"])