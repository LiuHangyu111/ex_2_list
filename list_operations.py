participants = [
    "Alice Wong", "Chen Wei", "David Kim", "Fatima Ali",
    "George Smith", "Hana Lee", "Audrey Hepburn",
    "James Stewart", "George Scott"
]

scores = [78, 92, 64, 87, 55, 73, 69, 96, 90]

qualification_score = 70
distinction_score = 90

def display_all():
    print("\nCURRENT PARTICIPANTS AND SCORES:")
    for name, score in zip(participants, scores):
        print(f"  {name} | Score: {score}")

def add_participant():
    name = input("Enter name: ").strip()
    if not name:
        print("Error: Name cannot be empty!")
        return
    for p in participants:
        if p.lower() == name.lower():
            print(f"Error: '{name}' already registered!")
            return
    try:
        score = float(input("Enter score (0-100): ").strip())
    except ValueError:
        print("Error: Score must be a number!")
        return
    if score < 0 or score > 100:
        print("Error: Score must be between 0 and 100!")
        return
    participants.append(name)
    scores.append(score)
    print(f"Successfully registered '{name}' with score {score}!")

def search_participant():
    name = input("Enter name to search: ").strip()
    if not name:
        print("Error: Name cannot be empty!")
        return
    for i in range(len(participants)):
        if participants[i].lower() == name.lower():
            score = scores[i]
            print(f"\n  Name: {participants[i]}")
            print(f"  Score: {score}")
            if score >= distinction_score:
                print("  Status: DISTINCTION")
            elif score >= qualification_score:
                print("  Status: QUALIFIED")
            else:
                print("  Status: NOT QUALIFIED")
            return
    print(f"Participant '{name}' not found!")

def display_all_status():
    print("\nALL PARTICIPANTS - STATUS REPORT")
    for i in range(len(participants)):
        score = scores[i]
        if score >= distinction_score:
            status = "DISTINCTION"
        elif score >= qualification_score:
            status = "QUALIFIED"
        else:
            status = "NOT QUALIFIED"
        print(f"{participants[i]} - Score: {score} - {status}")

def check_distinctions_and_pass():
    has_distinction = False
    all_passed = True
    for score in scores:
        if score >= distinction_score:
            has_distinction = True
        if score < 50:
            all_passed = False
    print(f"Has at least one DISTINCTION? {'Yes' if has_distinction else 'No'}")
    print(f"All participants passed (>=50)? {'Yes' if all_passed else 'No'}")

def update_score():
    name = input("Enter name to update: ").strip()
    if not name:
        print("Error: Name cannot be empty!")
        return
    for i in range(len(participants)):
        if participants[i].lower() == name.lower():
            print(f"Current score: {scores[i]}")
            try:
                new_score = float(input("Enter new score (0-100): ").strip())
            except ValueError:
                print("Error: Score must be a number!")
                return
            if new_score < 0 or new_score > 100:
                print("Error: Score must be between 0 and 100!")
                return
            scores[i] = new_score
            print(f"Score updated successfully to {new_score}!")
            return
    print(f"Participant '{name}' not found!")

def remove_participant():
    name = input("Enter name to remove: ").strip()
    if not name:
        print("Error: Name cannot be empty!")
        return
    for i in range(len(participants)):
        if participants[i].lower() == name.lower():
            removed_name = participants.pop(i)
            removed_score = scores.pop(i)
            print(f"Removed '{removed_name}' (score: {removed_score})")
            return
    print(f"Participant '{name}' not found!")

def display_scoreboard():
    combined = [(scores[i], participants[i]) for i in range(len(participants))]
    for i in range(len(combined)):
        for j in range(i + 1, len(combined)):
            if combined[i][0] < combined[j][0]:
                combined[i], combined[j] = combined[j], combined[i]
    print("\nSCOREBOARD (Ranked by Score)")
    for rank in range(len(combined)):
        print(f"#{rank + 1} {combined[rank][1]} - Score: {combined[rank][0]}")

def calculate_statistics():
    if not scores:
        print("No participants.")
        return
    highest = max(scores)
    lowest = min(scores)
    average = sum(scores) / len(scores)
    num_distinction = sum(1 for s in scores if s >= distinction_score)
    num_qualified = sum(1 for s in scores if qualification_score <= s < distinction_score)
    num_not_qualified = sum(1 for s in scores if s < qualification_score)
    print(f"Highest Score: {highest}")
    print(f"Lowest Score: {lowest}")
    print(f"Average Score: {average:.2f}")
    print(f"DISTINCTION: {num_distinction}, QUALIFIED: {num_qualified}, NOT QUALIFIED: {num_not_qualified}")

def generate_final_report():
    combined = [(scores[i], participants[i]) for i in range(len(participants))]
    for i in range(len(combined)):
        for j in range(i + 1, len(combined)):
            if combined[i][0] < combined[j][0]:
                combined[i], combined[j] = combined[j], combined[i]
    print("\nFINAL COMPREHENSIVE REPORT")
    for rank in range(len(combined)):
        score = combined[rank][0]
        if score >= distinction_score:
            status = "DISTINCTION"
        elif score >= qualification_score:
            status = "QUALIFIED"
        else:
            status = "NOT QUALIFIED"
        print(f"#{rank + 1} {combined[rank][1]} - Score: {score} - {status}")
    calculate_statistics()

def main():
    while True:
        print("\n" + "="*50)
        print("STUDENT SCORE MANAGEMENT SYSTEM")
        print("="*50)
        print("1. Display all")
        print("2. Add new")
        print("3. Search")
        print("4. Display statuses")
        print("5. Check distinctions & passing")
        print("6. Update score")
        print("7. Remove")
        print("8. Scoreboard")
        print("9. Statistics")
        print("10. Final report")
        print("0. Exit")
        print("="*50)
        choice = input("Enter your choice: ").strip()
        if choice == "0":
            print("Goodbye!")
            break
        elif choice == "1":
            display_all()
        elif choice == "2":
            add_participant()
        elif choice == "3":
            search_participant()
        elif choice == "4":
            display_all_status()
        elif choice == "5":
            check_distinctions_and_pass()
        elif choice == "6":
            update_score()
        elif choice == "7":
            remove_participant()
        elif choice == "8":
            display_scoreboard()
        elif choice == "9":
            calculate_statistics()
        elif choice == "10":
            generate_final_report()
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()