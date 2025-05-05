
---

### 🧾 `fitness_tracker.py`
```python
import json
from datetime import datetime

DATA_FILE = "data.json"

def load_data():
    try:
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)

def add_entry():
    date = datetime.now().strftime("%Y-%m-%d")
    activity = input("Enter activity (e.g. Running, Gym): ")
    duration = int(input("Enter duration in minutes: "))
    calories = int(input("Enter calories burned: "))

    entry = {
        "date": date,
        "activity": activity,
        "duration_mins": duration,
        "calories_burned": calories
    }

    data = load_data()
    data.append(entry)
    save_data(data)
    print("✅ Entry added successfully!")

def view_entries():
    data = load_data()
    if not data:
        print("📭 No entries found.")
        return
    print("\n📋 Workout History:\n")
    for entry in data:
        print(f"{entry['date']} | {entry['activity']} - {entry['duration_mins']} mins - {entry['calories_burned']} cal")

def menu():
    while True:
        print("\n===== FITNESS TRACKER =====")
        print("1. Add new entry")
        print("2. View history")
        print("3. Exit")
        choice = input("Select an option (1-3): ")

        if choice == "1":
            add_entry()
        elif choice == "2":
            view_entries()
        elif choice == "3":
            print("👋 Goodbye! Stay fit.")
            break
        else:
            print("❌ Invalid option. Try again.")

if __name__ == "__main__":
    menu()
