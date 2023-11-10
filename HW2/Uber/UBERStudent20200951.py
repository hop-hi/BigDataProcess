import sys
from datetime import datetime
def uber(input_file, output_file):
    try:
        with open(input_file, 'r', encoding='utf-8') as infile, open(output_file, 'w', encoding='utf-8') as outfile:
            for line in infile:
                data = line.strip().split(',')
                base_number = data[0]
                date = data[1]
                vehicles = int(data[2])
                trips = int(data[3])

                month, day, year = map(int, date.split('/'))
                dateDict = {0: 'MON', 1: 'TUE', 2: 'WED', 3: 'THU', 4: 'FRI', 5: 'SAT', 6: 'SUN'}
                week_of_day = dateDict[datetime(year, month, day).weekday()]

                result = "{},{} {},{}\n".format(base_number, week_of_day, vehicles, trips)
                outfile.write(result)
    except FileNotFoundError:
        print("FileNotFoundError")
        return None

if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    uber(input_file, output_file)