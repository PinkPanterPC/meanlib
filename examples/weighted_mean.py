from meanlib import weighted_mean

if __name__ == "__main__":
    # Define values and weights
    values = [3, 5, 8, 10]
    weights = [1, 2, 3, 4]

    # Calculate the weighted mean
    result = weighted_mean(values, weights)

    # Print the result
    print(f"The weighted mean is: {result}") # Output: The weighted mean is: 7.7