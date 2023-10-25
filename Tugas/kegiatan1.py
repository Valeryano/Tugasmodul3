def convert_to_minutes(weeks, days, hours, minutes):
    total_minutes = (weeks * 7 * 24 * 60) + (days * 24 * 60) + (hours * 60) + minutes
    return total_minutes

def curried_converter(weeks):
    def inner1(days):
        def inner2(hours):
            def inner3(minutes):
                return convert_to_minutes(weeks, days, hours, minutes)
            return inner3
        return inner2
    return inner1

data = ["3 minggu 3 hari 7 jam 21 menit",
        "5 minggu 5 hari 8 jam 11 menit",
        "7 minggu 1 hari 5 jam 33 menit"]
output_data = []

for item in data:
    parts = item.split()
    weeks = int(parts[0])
    days = int(parts[2])
    hours = int(parts[4])
    minutes = int(parts[6])
    
    # Menggunakan currying untuk mengkonversi
    result = curried_converter(weeks)(days)(hours)(minutes)
    output_data.append(result)

print(output_data)