from abc import ABC, abstractmethod, get_cache_token

# Define the abstract base class Man
class Man(ABC):
    @abstractmethod
    def run(self):
        pass

# Register the classes Jerry and Tom as virtual derived classes and see how the token changes
print(f'The token is {get_cache_token()}')

@Man.register
class Jerry():
    pass

print(f'The token is {get_cache_token()}')

class Tom():
    def run(self):
        # ERROR Man is not in the MRO
        super().run()
Man.register(Tom)

print(f'The token is {get_cache_token()}')

# Jerry and Tom are considered derived classes
print(issubclass(Jerry, Man))
print(issubclass(Tom, Man))
# You can create an instance as normal
print(isinstance(Jerry(), Man))
print(isinstance(Tom(), Man))

Tom().run()