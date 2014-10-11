#!/usr/bin/env python3
import random


class Operation:

    """Represents an operation in the game"""

    def __init__(self):
        """Constructor. Sets all the properties to None."""
        self.nb1 = None
        self.nb2 = None
        self.result = None
        self.operator = None

    def __str__(self):
        """String conversion of the Operation.
        It will be like '2 + 2 = 4', or '2 - ? = ?', or '? ? ? = ?'.
        If a number or operator is not set, it's replaced by the character '?'.
        """
        str_nb1 = str(self.nb1) if self.nb1 is not None else '?'
        str_nb2 = str(self.nb2) if self.nb2 is not None else '?'
        str_op = self.operator if self.operator is not None else '?'
        str_result = str(self.result) if self.result is not None else '?'
        return "{} {} {} = {}".format(str_nb1, str_op, str_nb2, str_result)

    def _calculate_result(self):
        """Tries to calculate the result. Will do nothing i"""
        if self.nb1 is not None and \
           self.nb2 is not None and \
           self.operator is not None:
            if self.operator == "+":
                self.result = self.nb1 + self.nb2
            elif self.operator == "-" and self.nb1 > self.nb2:
                self.result = self.nb1 - self.nb2
            elif self.operator == "*":
                self.result = self.nb1 * self.nb2
            elif self.operator == "/" and \
                    self.nb2 != 0 and \
                    self.nb1 % self.nb2 == 0:
                self.result = self.nb1 // self.nb2
        return False

    def use_number(self, nb):
        """Tries to use the given number in the operation"""
        # If the first number is not set
        if self.nb1 is None:
            self.nb1 = nb
            return True
        # If the second number is not set
        elif self.nb2 is None:
            self.nb2 = nb
            self._calculate_result()
            return True
        # If the numbers are already set
        else:
            return False

    def use_operator(self, operator):
        """Tries to use the given operator in the operation"""
        if operator in ['+', '-', '*', '/']:
            self.operator = operator
            self._calculate_result()
            return True
        else:
            return False

    def is_complete(self):
        """Returns True if the operation has a result, False otherwize"""
        if self.result is not None:
            return True
        else:
            return False


class CompteEstBon:

    """Game class"""

    def __init__(self):
        # Target is choosen randomly (1 <= target < 1000)
        self.target = random.randrange(101, 1000)
        # Base numbers are chosen randomly between 1..10, 25, 50, 75, 100
        possible = list(range(1, 11)) + [25, 50, 75, 100]
        self.base_nums = [random.choice(possible) for i in range(6)]
        self.used_base_nums = [False for i in range(6)]
        # Results are empty on initialization
        self.results = []
        self.used_results = []
        # Will be true when the target is found
        self.finished = False
        # Contains all the operations (calculi)
        self.ops = [Operation()]

    def use_base_number(self, index):
        """Try to use the base number at index in the current operation.

        :param index: the index of the base number to use (0 to 6)
        :returns: True if the number has been used, otherwize False
        """
        try:
            # If the number is already used
            if self.used_base_nums[index]:
                return False
            # If the number is not used
            else:
                # If the number can be used in the current operation
                if self.ops[-1].use_number(self.base_nums[index]):
                    # Set it as used
                    self.used_base_nums[index] = True
                    # if the result has been calculated
                    if self.ops[-1].is_complete():
                        # set the game as finished if the target has been found
                        if self.ops[-1].result == self.target:
                            self.finished = True
                        # add the result to the results list
                        self.results.append(self.ops[-1].result)
                        self.used_results.append(False)
                        # add a new operation
                        self.ops.append(Operation())
                    return True
                # If the number cannot be used in the operation
                else:
                    return False
        # If the given index is out of array
        except IndexError:
            return False

    def use_result(self, index):
        """Try to use the result at index in the curent operation.

        :param index: the index of the result to use
        :returns: True if the result has been used, otherwize False
        """
        try:
            # If the result is already used
            if self.used_results[index]:
                return False
            # If the result is not used
            else:
                # If the result can be used in the current operation
                if self.ops[-1].use_number(self.results[index]):
                    # Set it as used
                    self.used_results[index] = True
                    # Try to switching to next operation
                    self.try_next_operation()
                    return True
                # If the number cannot be used in the operation
                else:
                    return False
        # If the given index is out of array
        except IndexError:
            return False

    def use_operator(self, operator):
        """Try to use the given operator for the current operation."""
        if self.ops[-1].use_operator(operator):
            self.try_next_operation()
            return True
        else:
            return False

    def try_next_operation(self):
        """Try going to next operation, if current operation has a result"""
        # if the result has been calculated
        if self.ops[-1].is_complete():
            # set the game as finished if the target has been found
            if self.ops[-1].result == self.target:
                self.finished = True
            # add the result to the results list
            self.results.append(self.ops[-1].result)
            self.used_results.append(False)
            # add a new operation
            self.ops.append(Operation())
            return True
        else:
            return False

    def get_operations_strings(self):
        """Returns an array of strings of all operations"""
        return [str(op) for op in self.ops]
        # return reduce(lambda x: str(x) + "\n", self.ops)

    def get_numbers(self):
        return zip(self.base_nums, self.used_base_nums)

    def get_results(self):
        return zip(self.results, self.used_results)
