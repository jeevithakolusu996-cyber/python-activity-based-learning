
import re


def validate_student_email(email):
    errors = []

    if not email:
        return ["Email is missing."]

    if email.count("@") == 0:
        errors.append("Missing '@' separator.")
        return errors

    if email.count("@") > 1:
        errors.append("Email must contain exactly one '@'.")

    parts = email.split("@", 1)
    username = parts[0]
    domain = parts[1]

    if not username:
        errors.append("Username is missing.")

    if not domain:
        errors.append("Domain is missing.")

    if username:
        if username.startswith(".") or username.endswith("."):
            errors.append(
                "Username cannot start or end with a dot."
            )

        if ".." in username:
            errors.append(
                "Username contains consecutive dots."
            )

        if not re.fullmatch(
            r"[A-Za-z0-9._-]+", username
        ):
            errors.append(
                "Username contains invalid characters."
            )

    if domain:
        if "." not in domain:
            errors.append(
                "Domain must contain at least one dot."
            )

        if domain.startswith(".") or domain.endswith("."):
            errors.append(
                "Domain cannot start or end with a dot."
            )

        if ".." in domain:
            errors.append(
                "Domain contains consecutive dots."
            )

        if not re.fullmatch(
            r"[A-Za-z0-9.-]+", domain
        ):
            errors.append(
                "Domain contains invalid characters."
            )

        labels = domain.split(".")

        for label in labels:
            if not label:
                continue

            if label.startswith("-") or label.endswith("-"):
                errors.append(
                    f"Domain label '{label}' has a "
                    "misplaced hyphen."
                )

    return errors


def validate_registration_id(identifier):
    errors = []

    if not identifier:
        return ["Registration identifier is missing."]

    parts = identifier.split("-")

    if len(parts) != 3:
        errors.append(
            "Identifier must contain exactly 3 groups "
            "separated by 2 hyphens."
        )

    if len(parts) >= 1 and parts[0] != "STU":
        errors.append("Prefix must be 'STU'.")

    if len(parts) >= 2:
        if not re.fullmatch(r"\d{4}", parts[1]):
            errors.append(
                "Year group must contain exactly 4 digits."
            )

    if len(parts) >= 3:
        if not re.fullmatch(r"\d{4}", parts[2]):
            errors.append(
                "Student number must contain exactly 4 digits."
            )

    if len(parts) == 3:
        if not re.fullmatch(
            r"STU-\d{4}-\d{4}", identifier
        ):
            errors.append(
                "Identifier has an invalid overall format."
            )

    return errors


def report(label, value, validator):
    errors = validator(value)

    print(f"\n{label}: {value!r}")

    if errors:
        print("Status: INVALID")
        for error in errors:
            print(" -", error)
    else:
        print("Status: VALID")


# Example tests
emails = [
    "student123@university.edu",
    "student..123@university.edu",
    "studentuniversity.edu",
    "@university.edu",
    "student@",
    "student@@university.edu",
]

identifiers = [
    "STU-2026-0042",
    "STU-26-0042",
    "STX-2026-0042",
    "STU-2026-AB42",
    "STU20260042",
]

for email in emails:
    report("Email", email, validate_student_email)

for identifier in identifiers:
    report(
        "Registration ID",
        identifier,
        validate_registration_id
    )
