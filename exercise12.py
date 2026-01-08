starting_hour = 9
starting_minute = 30
stopping_hour = 11
stopping_minute = f"{0:02d}"
hourly_rate = 15
total_hours = stopping_hour - (starting_hour + starting_minute / 60)
payment = f"{(total_hours * hourly_rate):.2f}"


print(f"Worked {starting_hour}:{starting_minute} to {stopping_hour}:{stopping_minute}")
print(f"Total hours: {total_hours}")
print(f"Payment: ${payment}")