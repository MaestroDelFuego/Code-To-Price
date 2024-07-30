import os
import platform

def clear_console():
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')

def format_time(duration):
    if duration >= 60:
        hours = int(duration // 60)
        minutes = int(duration % 60)
        return f"{hours} hours, {minutes} minutes"
    else:
        seconds = round(duration * 60)
        return f"{seconds} seconds"

def calculate_typing_time(text, typing_speed):
    words = len(text.split())
    adjusted_speed = min(max(typing_speed, 15), 50)  # Adjust speed within range [15, 50]
    typing_time = words / adjusted_speed
    return typing_time

def calculate_cost(typing_time, rate_per_hour, typing_speed):
    adjusted_rate = rate_per_hour * (1 - (50 - typing_speed) * 0.005)  # Decrease rate by 0.5% for each wpm slower than 50
    cost = typing_time / 60 * adjusted_rate
    return cost

def main():
    print("Welcome to Typing Time and Cost Calculator!")
    typing_speed = float(input("Please enter your typing speed (words per minute): "))
    rate_per_hour = 5.50  # Base cost per hour in pounds (£)

    # Inform the user about potential earnings if they typed 5 words per minute faster
    adjusted_typing_speed = typing_speed + 5
    adjusted_typing_time = 0
    adjusted_total_cost = 0

    folder_path = "code"
    while not os.path.exists(folder_path):
        folder_path = input("Enter the path to the folder containing your code files: ")

    found_files = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".js"):
                found_files.append(os.path.join(root, file))

    if not found_files:
        print("No JavaScript files found in the specified folder and its subdirectories.")
        return

    total_typing_time = 0
    total_cost = 0
    for i, file_path in enumerate(found_files):
        with open(file_path, "r") as file:
            code_text = file.read()

        typing_time = calculate_typing_time(code_text, typing_speed)
        total_typing_time += typing_time

        file_cost = calculate_cost(typing_time, rate_per_hour, typing_speed)
        total_cost += file_cost

        if i == 0:
            clear_console()
        print("File:", file_path)
        print("Typing time:", format_time(typing_time))
        print("Number of lines:", code_text.count('\n') + 1)
        print("Number of characters:", len(code_text))
        print("Cost:", "£{:.2f}".format(file_cost))
        print()

    # Inform the user about total typing time and cost
    print("\nTotal typing time for all JavaScript files:", format_time(total_typing_time))
    print("Total cost at £5.50 per hour:", "£{:.2f}".format(total_cost))

    # Calculate and display potential earnings if typing 5 words per minute faster
    adjusted_typing_time = total_typing_time * (adjusted_typing_speed / typing_speed)
    adjusted_total_cost = calculate_cost(adjusted_typing_time, rate_per_hour, adjusted_typing_speed)
    print(f"\nIf you typed 5 words per minute faster ({adjusted_typing_speed} wpm):")
    print("Adjusted typing time:", format_time(adjusted_typing_time))
    print("Adjusted total cost:", "£{:.2f}".format(adjusted_total_cost))

if __name__ == "__main__":
    main()
