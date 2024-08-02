from meanlib import Mean

if __name__ == "__main__":
    # Create a Mean object with a maximum size of 5
    mean_calculator = Mean(max_size=5)

    # Update with single values
    print("Updating with single values:")
    print(mean_calculator.update(10))  # Output: 10.0
    print(mean_calculator.update(20))  # Output: 15.0
    print(mean_calculator.update(30))  # Output: 20.0
    print(mean_calculator.update(40))  # Output: 25.0
    print(mean_calculator.update(50))  # Output: 30.0
    print(mean_calculator.update(60))  # Output: 40.0 (removes 10)

    # Update with a list of values
    print("\nUpdating with a list of values:")
    print(mean_calculator.update_list([70, 80]))  # Output: 60.0 (removes 20 and 30)
    print(mean_calculator.update_list((90, 100)))  # Output: 80.0 (removes 40 and 50)

    # Get the current mean
    print("\nCurrent mean:")
    print(mean_calculator.get_mean())  # Output: 80.0