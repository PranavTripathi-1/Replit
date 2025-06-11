import json
from datetime import datetime

# Helper function to convert ISO timestamp to milliseconds
def iso_to_millis(iso_str):
    dt = datetime.strptime(iso_str, "%Y-%m-%dT%H:%M:%SZ")
    return int(dt.timestamp() * 1000)

# IMPLEMENT: load_data
def load_data():
    # Load data from both input files
    with open("data-1.json", "r") as f1:
        data1 = json.load(f1)

    with open("data-2.json", "r") as f2:
        data2 = json.load(f2)

    unified = []

    # Convert ISO timestamps in data1 to milliseconds
    for entry in data1:
        unified.append({
            "timestamp": iso_to_millis(entry["timestamp"]),
            "value": entry["value"]
        })

    # data2 is already in correct format
    for entry in data2:
        unified.append({
            "timestamp": entry["timestamp"],
            "value": entry["value"]
        })

    return unified

# IMPLEMENT: convert_and_save
def convert_and_save(data):
    # Sort by timestamp if needed
    data.sort(key=lambda x: x["timestamp"])

    # Save to the output file
    with open("output.json", "w") as out:
        json.dump(data, out, indent=2)

# Load and process data, then save it
if __name__ == "__main__":
    unified_data = load_data()
    convert_and_save(unified_data)
result = []
for entry in combined_data:
    result.append({
        "timestamp": timestamp_in_millis,
        "value": some_value
    })
combined_data = load_data()
    convert_and_save(combined_data)