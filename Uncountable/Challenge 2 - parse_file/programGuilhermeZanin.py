class Entry:
    def __init__(self, name, unit, data):
        self.name = name
        self.unit = unit
        self.data = data

    def __str__(self):
        return f"name: {self.name}, unit: {self.unit}, data: {self.data}"

class Section:
    def __init__(self):
        self.data = []

    def add_entry(self, entry):
        self.data.append(entry)
    
    def __str__(self):
        entries_str = "\n  ".join(str(entry) for entry in self.data)
        return f"Section:\n  {entries_str}"

def load_csv() -> list[list[str]]:
   import csv
   from io import StringIO
   import requests
   response = requests.get(
       "https://drive.google.com/uc?id=1o8dFEjUuVJHX1EjfKMrezmPiXxX5206A"
   )
   response.raise_for_status()
   csv_data = StringIO(response.text)
   csv_reader = csv.reader(csv_data)
   data_list = [row for row in csv_reader]
   return data_list

def parse_file(data_list):
    """
    Parses the provided list of lists (CSV data) into Section and Entry objects.
    Returns a list of Section objects.
    """
    sections = []  # store all sections
    current_section = Section()  # Current section being parsed

    for row in data_list:
        if not any(row):
            # If the row is empty, it indicates the end of a section
            if current_section.data:
                sections.append(current_section)  # Add the current section to the list
                current_section = Section()  # Start a new section
        else:
            # Clean and strip all the strings in the row
            row = [item.strip() for item in row]
            
            if row[7].lower() == 'yes':
                continue  # Skip this entry if "Ignore?" is yes

            name, unit = row[0], row[2]
            values = [value for value in row[0:7] if value]  # Only keep non-empty values

            if len(values) <= 3: # Gets the first values with only 3 columns
                # Line entry
                entry = Entry(name, unit, values[1])
                current_section.add_entry(entry)
            else:
                # Tabular entry
                for col in range(len(values)): # len(values) is 7
                    entry_data = [data_list[i][col] for i in range(20, 150) if data_list[i][col]]
                    entry = Entry(entry_data[0],entry_data[1],entry_data[2:])
                    current_section.add_entry(entry)

    if current_section.data:
        # Add the last section if it contains any data
        sections.append(current_section)

    return sections

# Example and tests
data_list = load_csv()
sections = parse_file(data_list)

# Print to verify the output
print("\n-------Parsed Sections-------:")
for section in sections:
    print(section) # Add breakpoint and Run in Debug mode to see results
    print("\n-------End of section-------\n")
