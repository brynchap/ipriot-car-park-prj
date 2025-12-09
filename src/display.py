class Display:
    def __init__(self, id, message = "", is_on = False):
        self.id = id
        self.message = message
        self.is_on = is_on

    def __str__(self):
        """
        Returns specific string when called.

        Parameter:
            self (Display): The current class instance

        Returns:
            string: A string containing the instance's `id` and `message` values.
        """
        return f"Display {self.id}: {self.message}"
    
    def update(self, data):
        for key, value in data.items():
            print(f"{key}: {value}")
            self.message = value
