participants = [
    "Alice Wong",
    "Chen Wei",
    "David Kim",
    "Fatima Ali",
    "George Smith",
    "Hana Lee",
    "Audrey Hepburn",
    "James Stewart",
    "George Scott"
]

scores = [78, 92, 64, 87, 55, 73, 69, 96, 90]

qualification_score = 70
distinction_score = 90

if len(participants) != len(scores):
    print("Warning: Participants and scores lists have different lengths!")
else:
    print(f"Lists are synchronized with {len(participants)} participants.")

print("\n" + "="*60)
print("CURRENT PARTICIPANTS AND SCORES:")
print("="*60)
for name, score in zip(participants, scores):
    print(f"  {name} | Score: {score}")
print("="*60)

def add_participant():
    print("\n" + "-"*60)
    print("ADD NEW PARTICIPANT")
    print("-"*60)
    
    name = input("Enter participant's name: ").strip()
    
    if name == "":
        print("Error: Name cannot be empty!")
        return
    
    already_exists = False
    for participant in participants:
        if participant.lower() == name.lower():
            already_exists = True
            break
    
    if already_exists:
        print(f"Error: '{name}' is already registered!")
        return
    
    score_input = input("Enter score (0-100): ").strip()
    
    is_number = True
    try:
        score = float(score_input)
    except ValueError:
        is_number = False
    
    if not is_number:
        print("Error: Score must be a number!")
        return
    
    if score < 0 or score > 100:
        print("Error: Score must be between 0 and 100!")
        return
    
    participants.append(name)
    scores.append(score)
    print(f"Successfully registered '{name}' with score {score}!")

def search_participant():
    print("\n" + "-"*60)
    print("SEARCH PARTICIPANT")
    print("-"*60)
    
    name = input("Enter participant's name to search: ").strip()
    
    if name == "":
        print("Error: Name cannot be empty!")
        return
    
    found = False
    for i in range(len(participants)):
        if participants[i].lower() == name.lower():
            score = scores[i]
            found = True
            print(f"\n  Name: {participants[i]}")
            print(f"  Score: {score}")
            
            if score >= distinction_score:
                print("  Status: DISTINCTION")
            elif score >= qualification_score:
                print("  Status: QUALIFIED")
            else:
                print("  Status: NOT QUALIFIED")
            break
    
    if not found:
        print(f"Participant '{name}' not found!")

def display_all_status():
    print("\n" + "="*60)
    print("ALL PARTICIPANTS - STATUS REPORT")
    print("="*60)
    print("Name                 Score    Status")
    print("-"*60)
    
    for i in range(len(participants)):
        name = participants[i]
        score = scores[i]
        
        if score >= distinction_score:
            status = "DISTINCTION"
        elif score >= qualification_score:
            status = "QUALIFIED"
        else:
            status = "NOT QUALIFIED"
        
        print(f"{name:<20} {score:<8} {status}")
    print("="*60)

def check_distinctions_and_pass():
    print("\n" + "-"*60)
    print("DISTINCTION AND PASSING CHECK")
    print("-"*60)
    
    has_distinction = False
    all_passed = True
    
    for score in scores:
        if score >= distinction_score:
            has_distinction = True
        if score < 50:
            all_passed = False
    
    if has_distinction:
        print("  Has at least one DISTINCTION? Yes")
    else:
        print("  Has at least one DISTINCTION? No")
    
    if all_passed:
        print("  All participants passed (>=50)? Yes")
    else:
        print("  All participants passed (>=50)? No")
    
    if has_distinction:
        distinction_names = []
        for i in range(len(participants)):
            if scores[i] >= distinction_score:
                distinction_names.append(participants[i])
        print(f"  Distinction holders: {', '.join(distinction_names)}")

def update_score():
    print("\n" + "-"*60)
    print("UPDATE PARTICIPANT SCORE")
    print("-"*60)
    
    name = input("Enter participant's name to update: ").strip()
    
    if name == "":
        print("Error: Name cannot be empty!")
        return
    
    found_index = -1
    for i in range(len(participants)):
        if participants[i].lower() == name.lower():
            found_index = i
            break
    
    if found_index == -1:
        print(f"Participant '{name}' not found!")
        return
    
    print(f"Current score for '{participants[found_index]}': {scores[found_index]}")
    
    score_input = input("Enter new score (0-100): ").strip()
    
    is_number = True
    try:
        new_score = float(score_input)
    except ValueError:
        is_number = False
    
    if not is_number:
        print("Error: Score must be a number!")
        return
    
    if new_score < 0 or new_score > 100:
        print("Error: Score must be between 0 and 100!")
        return
    
    scores[found_index] = new_score
    print(f"Score updated successfully for '{participants[found_index]}' to {new_score}!")

def remove_participant():
    print("\n" + "-"*60)
    print("REMOVE PARTICIPANT")
    print("-"*60)
    
    name = input("Enter participant's name to remove: ").strip()
    
    if name == "":
        print("Error: Name cannot be empty!")
        return
    
    found_index = -1
    for i in range(len(participants)):
        if participants[i].lower() == name.lower():
            found_index = i
            break
    
    if found_index == -1:
        print(f"Participant '{name}' not found!")
        return
    
    removed_name = participants.pop(found_index)
    removed_score = scores.pop(found_index)
    print(f"Removed '{removed_name}' (score: {removed_score})")

def display_scoreboard():
    print("\n" + "="*60)
    print("SCOREBOARD (Ranked by Score)")
    print("="*60)
    print("Rank   Name                 Score")
    print("-"*60)
    
    combined = []
    for i in range(len(participants)):
        combined.append((scores[i], participants[i]))
    
    for i in range(len(combined)):
        for j in range(i + 1, len(combined)):
            if combined[i][0] < combined[j][0]:
                temp = combined[i]
                combined[i] = combined[j]
                combined[j] = temp
    
    for rank in range(len(combined)):
        score = combined[rank][0]
        name = combined[rank][1]
        print(f"{rank + 1:<6} {name:<20} {score:<8}")
    print("="*60)

def calculate_statistics():
    print("\n" + "-"*60)
    print("STATISTICS")
    print("-"*60)
    
    if len(scores) == 0:
        print("No participants to calculate statistics.")
        return
    
    highest = scores[0]
    lowest = scores[0]
    
    for score in scores:
        if score > highest:
            highest = score
        if score < lowest:
            lowest = score
    
    total = 0
    for score in scores:
        total = total + score
    average = total / len(scores)
    
    num_highest = 0
    num_lowest = 0
    for score in scores:
        if score == highest:
            num_highest = num_highest + 1
        if score == lowest:
            num_lowest = num_lowest + 1
    
    num_distinction = 0
    num_qualified = 0
    num_not_qualified = 0
    
    for score in scores:
        if score >= distinction_score:
            num_distinction = num_distinction + 1
        elif score >= qualification_score:
            num_qualified = num_qualified + 1
        else:
            num_not_qualified = num_not_qualified + 1
    
    print(f"  Highest Score: {highest} (achieved by {num_highest} participant(s))")
    
    highest_names = []
    for i in range(len(participants)):
        if scores[i] == highest:
            highest_names.append(participants[i])
    print(f"    - {', '.join(highest_names)}")
    
    print(f"  Lowest Score: {lowest} (achieved by {num_lowest} participant(s))")
    
    lowest_names = []
    for i in range(len(participants)):
        if scores[i] == lowest:
            lowest_names.append(participants[i])
    print(f"    - {', '.join(lowest_names)}")
    
    print(f"  Average Score: {average:.2f}")
    print(f"  Participants with DISTINCTION (>= {distinction_score}): {num_distinction}")
    print(f"  Participants QUALIFIED ({qualification_score}-{distinction_score - 1}): {num_qualified}")
    print(f"  Participants NOT QUALIFIED (< {qualification_score}): {num_not_qualified}")

def generate_final_report():
    print("\n" + "="*60)
    print("FINAL COMPREHENSIVE REPORT")
    print("="*60)
    
    combined = []
    for i in range(len(participants)):
        combined.append((scores[i], participants[i]))
    
    for i in range(len(combined)):
        for j in range(i + 1, len(combined)):
            if combined[i][0] < combined[j][0]:
                temp = combined[i]
                combined[i] = combined[j]
                combined[j] = temp
    
    print("\nRank   Name                 Score    Status")
    print("-"*60)
    
    for rank in range(len(combined)):
        score = combined[rank][0]
        name = combined[rank][1]
        
        if score >= distinction_score:
            status = "DISTINCTION"
        elif score >= qualification_score:
            status = "QUALIFIED"
        else:
            status = "NOT QUALIFIED"
        
        print(f"{rank + 1:<6} {name:<20} {score:<8} {status}")
    
    print("-"*60)
    calculate_statistics()
    print("="*60)

def main():
    while True:
        print("\n" + "="*60)
        print("STUDENT SCORE MANAGEMENT SYSTEM")
        print("="*60)
        print("1. Display all participants")
        print("2. Add new participant")
        print("3. Search participant")
        print("4. Display all statuses")
        print("5. Check distinctions and passing")
        print("6. Update score")
        print("7. Remove participant")
        print("8. Display scoreboard")
        print("9. Show statistics")
        print("10. Generate final report")
        print("0. Exit")
        print("="*60)
        
        choice = input("Enter your choice: ").strip()
        
        if choice == "0":
            print("Goodbye!")
            break
        elif choice == "1":
            print("\n" + "="*60)
            print("CURRENT PARTICIPANTS AND SCORES:")
            print("="*60)
            for name, score in zip(participants, scores):
                print(f"  {name} | Score: {score}")
            print("="*60)
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
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()