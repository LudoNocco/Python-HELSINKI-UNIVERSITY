from datetime import datetime, timedelta

filename = input("Filename: ")
start_date = input("Starting date (dd.mm.yyyy): ")
days = int(input("How many days: "))

start_date_obj = datetime.strptime(start_date, "%d.%m.%Y")
screen_times = []
total_minutes = 0

for i in range(days):
    current_date = start_date_obj.strftime("%d.%m.%Y")
    screen_time = input(f"Screen time {current_date}: ")
    tv, computer, mobile = map(int, screen_time.split())
    screen_times.append((current_date, tv, computer, mobile))
    total_minutes += tv + computer + mobile
    start_date_obj += timedelta(days=1)

average_minutes = total_minutes / days

with open(filename, "w") as file:
    file.write(f"Time period: {screen_times[0][0]}-{screen_times[-1][0]}\n")
    file.write(f"Total minutes: {total_minutes}\n")
    file.write(f"Average minutes: {average_minutes:.1f}\n")
    for date, tv, computer, mobile in screen_times:
        file.write(f"{date}: {tv}/{computer}/{mobile}\n")

print(f"Data stored in file {filename}")
