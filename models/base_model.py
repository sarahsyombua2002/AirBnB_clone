#!/usr/bin/python3
"""
BaseModel module: This module defines the BaseModel class.
"""

import uuid
from datetime import datetime
from models import storage

class BaseModel:
    """
    BaseModel class: Reps a base model with common attributes and methods.
    """

    def __init__(self, *args, **kwargs):
        """
        Constructor: Initializes a BaseModel instance.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.
        """
        if kwargs:  # If we have a magical recipe
            for key, value in kwargs.items():
                if key != '__class__':
                    setattr(self, key, value)

                    # Convert created_at and updated_at strings to datetime
                    if key in ['created_at', 'updated_at']:
                        setattr(self, key, datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f'))
        else:  # If no recipe, create a new with an ID, creation time, and update time
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)  

    def __str__(self):
        """
        String representation: Returns a string representation of the BaseModel.

        Returns:
            str: String representation.
        """
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """
        Save method: Updates the public instance attribute updated_at with the current datetime.
        """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """
        to_dict method: Converts the BaseModel instance to a dictionary.

        Returns:
            dict: Dictionary representation of the instance.
        """
        obj_dict = self.__dict__.copy()  # Get a copy of the instance's __dict__
        obj_dict['__class__'] = self.__class__.__name__  # Add class name to the dictionary

        # Convert created_at and updated_at to string object in ISO format
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()

        return obj_dict

# Example usage:
if __name__ == "__main__":
    # Create an instance of BaseModel
    my_model = BaseModel()

    # Print the string representation
    print(str(my_model))

    # Update and save
    my_model.save()

    # Print the updated string representation
    print(str(my_model))

    # Convert to dictionary
    my_model_dict = my_model.to_dict()

    # Print the dictionary
    print(my_model_dict)

    # Recreate an instance from the dictionary
    recreated_model = BaseModel(**my_model_dict)

    # Print the string representation of the recreated instance
    print(str(recreated_model))

