# A simple class Apple
class Apple:
    # Variable variety
    variety = 'Ordinary apples'
    # Static method show
    @staticmethod
    def show():
        print(Apple.variety)

    # Constructor
    def __init__(self, w):
        # The instance variable weight is defined by self, which represents the instance
        self.weight = w

# Assign a value to the attribute variety
Apple.variety = 'Stone apples'
# Call the show method
Apple.show()

# Add a class variable to the Apple class and then display all the attributes of the Apple class
Apple.price = 10
print(Apple.__dict__)
# Add an instance variable to the instance and then display all the attributes of the instance
apple = Apple(100)
apple.price = 30
print(apple.__dict__)

# Create an instance of the Apple class
apple = Apple(30)
# Access the class variable variety through the instance
print(apple.variety)

# The following assignment statement will define a new instance variable variety for the instance
apple.variety = 'Extra large apple'
# Therefore, the class variable variety does not change
print(Apple.variety)