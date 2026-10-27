INPUT:
    Applicants
    Scholarship quota K

FOR each applicant:
    IF aggregate marks < 75
       OR any required subject mark < 60
       OR attendance < 80
       OR annual family income > 250000:
           Mark applicant as INELIGIBLE
    ELSE:
           Mark applicant as ELIGIBLE

Sort eligible applicants by:
    1. Aggregate marks descending
    2. Required-subject average descending
    3. Attendance descending
    4. Annual family income ascending
    5. Application submission time ascending

Allocate scholarships to the first K eligible applicants.

Mark remaining eligible applicants as WAITLISTED.
Mark all other applicants as INELIGIBLE.

OUTPUT:
    Scholarship recipients
    Ranked waiting list
    Ineligible applicants with rejection reasons
