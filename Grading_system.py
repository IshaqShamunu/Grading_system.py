def get_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"


def add_students():
    students = []
    n = int(input("How many students do you want to enter? "))
    for i in range(n):
        name = input("Enter name: ")
        age = int(input("Enter age: "))
        score = float(input("Enter score: "))
        students.append({"name": name, "age": age, "score": score})
    return students


def display_records(students):
    print("\n--- Student Records ---")
    for s in students:
        s["grade"] = get_grade(s["score"])
        print(f"Name: {s['name']} | Age: {s['age']} | Score: {s['score']} | Grade: {s['grade']}")


def show_summary(students):
    highest = max(students, key=lambda x: x["score"])
    total = sum(s["score"] for s in students)
    average = total / len(students)
    print("\nTop Student:", highest["name"], "with score", highest["score"])
    print("Class Average:", round(average, 2))


def search_student(students):
    name = input("\nEnter a student name to search: ")
    found = False
    for s in students:
        if s["name"].lower() == name.lower():
            print(f"Found → Name: {s['name']}, Age: {s['age']}, Score: {s['score']}, Grade: {get_grade(s['score'])}")
            found = True
            break
    if not found:
        print("Student not found.")


# Main Program
students = add_students()
display_records(students)
show_summary(students)
search_student(students)
