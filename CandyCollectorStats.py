

def main():
    total_candies = 0
    students_more_than_4 = 0

    while True:
        candies_collected = int(input("Enter the number of candies collected (enter 1000 to terminate): "))
        
        if candies_collected == 1000:
            break
        
        total_candies += candies_collected
        
        if candies_collected > 4:
            students_more_than_4 += 1

    print(f"Number of students who got more than 4 candies: {students_more_than_4}")
    print(f"Total number of candies collected by all students: {total_candies}")

if __name__ == "__main__":
    main()
