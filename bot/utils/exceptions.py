class DatabaseCreationError(Exception):
    def __init__(self, message="An error occurred while creating database tables."):
        self.message = message
        super().__init__(self.message)