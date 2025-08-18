import faker
import requests

# Replace with the url of your codespaces instance
base_url = "https://verbose-system-r5xgxqw56wcp5xv-8000.app.github.dev"

fake = faker.Faker()


def create_gig(date, time):
    gig_data = {
        "venue_id": 1,
        "client_id": 1,
        "name": fake.text(max_nb_chars=10),
        "date": date,
        "time": time,
    }
    response = requests.post(f"{base_url}/api/gigs", json=gig_data)
    print(response.json())


# second gig close to the notification window
time1 = "12:00"
date = "2026-01-01"
create_gig(date, time1)

time2 = "18:00"
create_gig(date, time2)

# Second gig in the notification window (but before)
time3 = "11:00"
create_gig(date, time3)

# Second gig in the notification window (but after)
time4 = "19:00"
create_gig(date, time4)

# Second gig at the same time as another
create_gig(date, time4)

# Gig bewtween to gigs that should both notify
time5 = "14:00"
create_gig(date, time5)
