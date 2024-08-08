__version__ = '1.4.0'

def mean(values: list | tuple):
    """
    Calculates the arithmetic mean of a list of values.

    This function computes the arithmetic mean, which is the sum of the values divided by the number of values.

    Args:
        values (list | tuple): A list or tuple containing the numerical values for which the mean is to be calculated.

    Returns:
        The calculated arithmetic mean (float or complex) or None if the input is empty.

    Raises:
        TypeError: If `values` is not of a compatible type.
        TypeError: If an element in `values` is not of the correct type.
    """
    try:
        return sum(values)/len(values) if values else None
    except TypeError:
        raise TypeError('There are values of incompatible types in `values`, or `values` is not of a compatible type')
    
def weighted_mean(values: list | tuple, weights: list | tuple):
    """
    Calculates the weighted mean of a list of values.

    This function computes the weighted mean.
    The weighted mean is the sum of the values, each multiplied by their corresponding weight, divided by the total sum of the weights.

    Args:
        values (list | tuple): A list containing the values for which the weighted mean is to be calculated.
        weights (list | tuple): A list structure containing the weights associated with each value.

    Returns:
        The calculated weighted mean (float or complex).

    Raises:
        TypeError: If `values` or `weights` are not of a compatible type.
        TypeError: If an element in `values` or `weights` is not of the correct type.
        ValueError: If `values` and `weights` do not have the same length.
    """
    try:
        total_weight = sum(weights)
        return sum(v * w for v, w in zip(values, weights)) / total_weight if values else None
    except ValueError:
        raise ValueError('The `values` array and the `weights` array must have the same length')
    except TypeError:
        raise TypeError('There are values ​​of incompatible types in `values` or `weights`, or `values` is not of a compatible type')
    

class SimpleMean():
    def __init__(self):
        """
        Initializes a SimpleMean object.

        This function initializes the sum and count attributes to 0.
        """
        self._sum = 0
        self.count = 0 

    def update(self, value: int | float | complex):
        """
        Updates the mean with a new value.

        This function adds the new value to the sum and increments the count.
        It then returns the updated mean.

        Args:
            value (int | float | complex): The new value to be added to the mean.

        Returns:
            The updated mean (float or complex or None).

        Raises:
            TypeError: If `value` is not of a compatible type.
        """
        try:
            self._sum += value
            self.count += 1
            return self.get_mean()
        except TypeError:
            raise TypeError('`Value` is not of a compatible type')
            

    def get_mean(self):
        """
        Returns the current mean.

        This function calculates the mean by dividing the sum by the count.
        If the count is 0, it returns None.

        Returns:
            The current mean (float or complex), or None if the count is 0.
        """
        return self._sum / self.count if self.count > 0 else None
    
class RollingMean():
    def __init__(self, max_size=None):
        """
        Initializes a RollingMean object.

        This function initializes the array attribute to an empty list.
        It also initializes the max_size attribute to the given value, or None if no value is given.

        Args:
            max_size (int | str, optional): The maximum number of values to store in the array. If None, there is no limit.

        Raises:
            ValueError: If the `max_size` is not an integer or a string of an integer.
        """
        self.array = []
        if max_size is not None:
            self.max_size = int(max_size)
        else:
            self.max_size = None
    
    def update(self, value: int | float | complex):
        """
        Updates the mean with a new value.

        This function appends the new value to the array.
        If the maximum number of values is reached, it removes the oldest values to maintain the limit.
        It then returns the updated mean.

        Args:
            value (int | float | complex): The new value to be added to the mean.

        Returns:
            The updated mean (float or complex or None).

        Raises:
            TypeError: If `value` is not of a compatible type.
        """
        old_list = self.array
        try:
            self.array.append(value)
            if self.max_size and len(self.array) > self.max_size:
                self.array.pop(0)
            return self.get_mean()
        except TypeError:
            self.array = old_list
            raise TypeError('`Value` is not of a compatible type')
    
    def update_list(self, values: list | tuple):
        """
        Updates the mean with a list of values.

        This function appends the list of values to the array.
        If the maximum number of values is reached, it removes the oldest values to maintain the limit.
        It then returns the updated mean.

        Args:
            values (list | tuple): The list of values to be added to the mean.

        Returns:
            The updated mean (float or complex or None).
        
        Raises:
            TypeError: If `values` is not a list or tuple.
            TypeError: If an element in `values` is not of the correct type.
        """
        old_list = self.array
        try:
            if values:
                self.array.extend(values)
                if self.max_size and len(self.array) > self.max_size:
                    self.array = self.array[-self.max_size:]
            return self.get_mean()
        except TypeError:
            self.array = old_list
            raise TypeError('There are values of incompatible types in `values`, or `values` is not of a compatible type')

    def get_mean(self):
        """
        Returns the current mean.

        This function calculates the mean of the values in the array.
        If the array is empty, it returns None.

        Returns:
            The current mean (float or complex), or None if the array is empty.
        """
        return sum(self.array) / len(self.array) if self.array > 0 else None

def geometric_mean(values: list | tuple):
    """
    Calculates the geometric mean of a list of values.

    This function computes the geometric mean, which is the sum of the values divided by the number of values.
    All the values should be positive and not complex.

    Args:
        values (list | tuple): A list or tuple containing the numerical values for which the mean is to be calculated.

    Returns:
        The calculated geometric mean (float) or None if the input is empty.

    Raises:
        TypeError: If `values` is not of a compatible type.
        TypeError: If an element in `values` is not of the correct type.
    """
    try:
        if values:
            product = 1
            for value in values:
                product *= value
            n = len(values)
            geo_mean = product ** (1 / n)
            return geo_mean
        else: return None
    except TypeError:
        raise TypeError('There are values of incompatible types in `values`, or `values` is not of a compatible type')
    
class RollingGeometricMean():
    def __init__(self, max_size=None):
        """
        Initializes a RollingGeometricMean object.

        This function initializes the array attribute to an empty list.
        It also initializes the max_size attribute to the given value, or None if no value is given.

        Args:
            max_size (int | str, optional): The maximum number of values to store in the array. If None, there is no limit.

        Raises:
            ValueError: If the `max_size` is not an integer or a string of an integer.
        """
        self.array = []
        if max_size is not None:
            self.max_size = int(max_size)
        else:
            self.max_size = None
    
    def update(self, value: int | float):
        """
        Updates the mean with a new value.

        This function appends the new value to the array.
        The value should be positive
        If the maximum number of values is reached, it removes the oldest values to maintain the limit.
        It then returns the updated mean.

        Args:
            value (int | float | complex): The new value to be added to the mean.

        Returns:
            The updated mean (float or None).

        Raises:
            TypeError: If `value` is not of a compatible type.
        """
        old_list = self.array
        try:
            self.array.append(value)
            if self.max_size and len(self.array) > self.max_size:
                self.array.pop(0)
            return self.get_mean()
        except TypeError:
            self.array = old_list
            raise TypeError('`Value` is not of a compatible type')
    
    def update_list(self, values: list | tuple):
        """
        Updates the mean with a list of values.

        This function appends the list of values to the array.
        All the values should be positive and not complex.
        If the maximum number of values is reached, it removes the oldest values to maintain the limit.
        It then returns the updated mean.

        Args:
            values (list | tuple): The list of values to be added to the mean.

        Returns:
            The updated mean (float or None).
        
        Raises:
            TypeError: If `values` is not a list or tuple.
            TypeError: If an element in `values` is not of the correct type.
        """
        old_list = self.array
        try:
            if values:
                self.array.extend(values)
                if self.max_size and len(self.array) > self.max_size:
                    self.array = self.array[-self.max_size:]
            return self.get_mean()
        except TypeError:
            self.array = old_list
            raise TypeError('There are values of incompatible types in `values`, or `values` is not of a compatible type')

    def get_mean(self):
        """
        Returns the current mean.

        This function calculates the mean of the values in the array.
        If the array is empty, it returns None.

        Returns:
            The current mean (float), or None if the array is empty.
        """
        if self.array:
            product = 1
            for value in self.array:
                product *= value
            n = len(self.array)
            geo_mean = product ** (1 / n)
            return geo_mean
        else: return None

def harmonic_mean(values: list | tuple):
    """
    Calculates the harmonic mean of a list of values.

    This function computes the harmonic mean, which is the reciprocal of the arithmetic mean of the reciprocals of the values.
    All the values should be positive and not complex.

    Args:
        values (list | tuple): A list or tuple containing the numerical values for which the mean is to be calculated.

    Returns:
        The calculated harmonic mean (float) or None if the input is empty.

    Raises:
        TypeError: If `values` is not of a compatible type.
        TypeError: If an element in `values` is not of the correct type.
        ZeroDivisionError: If any value in `values` is 0.
    """
    try:
        reciprocals = [1/value for value in values]
        return len(values) / sum(reciprocals) if values else None
    except TypeError:
        raise TypeError('There are values of incompatible types in `values`, or `values` is not of a compatible type')
    except ZeroDivisionError:
        raise ZeroDivisionError('One or more value in `values` are 0')

class RollingHarmonicMean():
    def __init__(self, max_size=None):
        """
        Initializes a RollingHarmonicMean object.

        This function initializes the array attribute to an empty list.
        It also initializes the max_size attribute to the given value, or None if no value is given.

        Args:
            max_size (int | str, optional): The maximum number of values to store in the array. If None, there is no limit.

        Raises:
            ValueError: If the `max_size` is not an integer or a string of an integer.
        """
        self.array = []
        if max_size is not None:
            self.max_size = int(max_size)
        else:
            self.max_size = None
    
    def update(self, value: int | float):
        """
        Updates the mean with a new value.

        This function appends the new value to the array.
        The value should be positive
        If the maximum number of values is reached, it removes the oldest values to maintain the limit.
        It then returns the updated mean.

        Args:
            value (int | float | complex): The new value to be added to the mean.

        Returns:
            The updated mean (float or None).

        Raises:
            TypeError: If `value` is not of a compatible type.
            ZeroDivisionError: If `value` is 0.
        """
        old_list = self.array
        try:
            self.array.append(value)
            if self.max_size and len(self.array) > self.max_size:
                self.array.pop(0)
            return self.get_mean()
        except TypeError:
            self.array = old_list
            raise TypeError('`Value` is not of a compatible type')
        except ZeroDivisionError:
            self.array = old_list
            raise ZeroDivisionError('`Value` is 0')
    
    def update_list(self, values: list | tuple):
        """
        Updates the mean with a list of values.

        This function appends the list of values to the array.
        All the values should be positive and not complex.
        If the maximum number of values is reached, it removes the oldest values to maintain the limit.
        It then returns the updated mean.

        Args:
            values (list | tuple): The list of values to be added to the mean.

        Returns:
            The updated mean (float or None).
        
        Raises:
            TypeError: If `values` is not a list or tuple.
            TypeError: If an element in `values` is not of the correct type.
            ZeroDivisionError: If any value in `values` is 0.
        """
        old_list = self.array
        try:
            if values:
                self.array.extend(values)
                if self.max_size and len(self.array) > self.max_size:
                    self.array = self.array[-self.max_size:]
            return self.get_mean()
        except TypeError:
            self.array = old_list
            raise TypeError('There are values of incompatible types in `values`, or `values` is not of a compatible type')
        except ZeroDivisionError:
            self.array = old_list
            raise ZeroDivisionError('One or more value in `values` are 0')

    def get_mean(self):
        """
        Returns the current mean.

        This function calculates the mean of the values in the array.
        If the array is empty, it returns None.

        Returns:
            The current mean (float), or None if the array is empty.
        """
        reciprocals = [1/value for value in self.array]
        return len(self.array) / sum(reciprocals) if self.array else None
