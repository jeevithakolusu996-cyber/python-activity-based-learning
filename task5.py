
from datetime import datetime

DAYS = {
    "monday", "tuesday", "wednesday", "thursday",
    "friday", "saturday", "sunday"
}


def parse_time(value):
    return datetime.strptime(value.strip(), "%H:%M").time()


def normalize_schedule(schedule):
    """Accept a comma-separated string or a 5-element tuple/list."""
    if isinstance(schedule, str):
        fields = [x.strip() for x in schedule.split(",")]
    else:
        fields = list(schedule)

    if len(fields) != 5:
        raise ValueError(
            "Schedule must contain course, day, start, end, room"
        )

    course, day, start, end, room = map(str, fields)

    if day.lower() not in DAYS:
        raise ValueError(f"Invalid day: {day}")

    start_time = parse_time(start)
    end_time = parse_time(end)

    if start_time >= end_time:
        raise ValueError(
            f"Invalid time interval for {course}"
        )

    if not course.strip() or not room.strip():
        raise ValueError("Course and room must not be empty")

    return (
        course.strip(),
        day.title(),
        start_time,
        end_time,
        room.strip()
    )


def overlaps(a, b):
    """Schedules must already be normalized."""
    return (
        a[1] == b[1]
        and a[2] < b[3]
        and b[2] < a[3]
    )


def detect_conflicts(schedules):
    conflicts = []

    for i in range(len(schedules)):
        for j in range(i + 1, len(schedules)):
            a, b = schedules[i], schedules[j]

            if not overlaps(a, b):
                continue

            if a[4] == b[4]:
                conflicts.append(
                    ("ROOM CONFLICT", a[0], b[0], a[4])
                )
            else:
                conflicts.append(
                    ("STUDENT CONFLICT", a[0], b[0], None)
                )

    return conflicts


def check_room_availability(schedules, unavailable):
    """
    unavailable entries:
    (day, start, end, room)
    """
    conflicts = []

    for s in schedules:
        for day, start, end, room in unavailable:
            blocked = normalize_schedule(
                (s[0], day, start, end, room)
            )

            if s[4] == room and overlaps(s, blocked):
                conflicts.append(
                    (s[0], s[4], day, start, end)
                )

    return conflicts


def validate_timetable(raw_schedules, unavailable=()):
    schedules = []
    errors = []

    for index, raw in enumerate(raw_schedules, start=1):
        try:
            schedules.append(normalize_schedule(raw))
        except (ValueError, TypeError) as exc:
            errors.append(f"Schedule {index}: {exc}")

    conflicts = detect_conflicts(schedules)
    room_conflicts = check_room_availability(
        schedules, unavailable
    )

    return {
        "valid": not errors and not conflicts and not room_conflicts,
        "errors": errors,
        "conflicts": conflicts,
        "unavailable_rooms": room_conflicts,
    }


# Example timetable: strings and tuples are both supported.
proposed = [
    "CS101,Monday,09:00,10:00,R101",
    ("MA102", "Monday", "09:30", "10:30", "R102"),
    ("PH103", "Monday", "10:00", "11:00", "R101"),
]

unavailable = [
    ("Monday", "10:00", "11:00", "R101")
]

result = validate_timetable(proposed, unavailable)

print("Valid timetable:", result["valid"])
print("Invalid entries:", result["errors"])
print("Time conflicts:", result["conflicts"])
print("Unavailable rooms:", result["unavailable_rooms"])

