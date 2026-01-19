import csv
from datetime import date

FILE_NAME = "job_applications.csv"

def add_job():
    company = input("Company Name: ")
    role = input("Job Role: ")
    status = input("Status (Applied/Interview/Rejected/Offer): ")
    applied_date = date.today().strftime("%d-%m-%Y")

    with open(FILE_NAME, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([company, role, applied_date, status])

    print("✅ Job application added successfully")

def view_jobs():
    try:
        with open(FILE_NAME, mode='r') as file:
            reader = csv.reader(file)
            print("\nCompany | Role | Date | Status")
            print("-" * 45)
            for row in reader:
                print(" | ".join(row))
    except FileNotFoundError:
        print("❌ No job applications found")

def search_job():
    keyword = input("Search by company name: ").lower()
    found = False

    with open(FILE_NAME, mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            if keyword in row[0].lower():
                print(row)
                found = True

    if not found:
        print("❌ No matching job found")

def main():
    while True:
        print("\n--- Job Application Tracking System ---")
        print("1. Add Job Application")
        print("2. View All Applications")
        print("3. Search Application")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_job()
        elif choice == '2':
            view_jobs()
        elif choice == '3':
            search_job()
        elif choice == '4':
            print("All the best for your career 🚀")
            break
        else:
            print("❌ Invalid choice. Try again.")

main()