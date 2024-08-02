from meanlib import SimpleMean

if __name__ == "__main__":
    # Create a SimpleMean object
    mean = SimpleMean()

    # Update the mean with some values
    print(mean.update(5))  # Output: 5.0
    print(mean.get_mean())  # Output: 5.0

    mean.update(10)
    mean.update(15)
    mean.update(20)

    print(mean.get_mean())  # Output: 12.5
    print(mean.count)  # Output: 4

    # Update the mean with a complex number
    mean.update(2 + 3j)

    print(mean.get_mean())  # Output: (10.4+0.6j)
    print(mean.count)  # Output: 5