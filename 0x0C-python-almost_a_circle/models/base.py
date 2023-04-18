#!/usr/bin/python3

"""Defines a base model class."""
import json
import csv
import turtle


class Base:
    """This is the documentation for the base model in project 0x0C*.
      It serves as the foundation for all other classes. The class has
        a private attribute called __nb_object which keeps track of
        the number of Base instances that have been created.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a new Base.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON representation of a list of dictionaries.
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Create a file that contains the JSON representation of a list of objects.
        """
        filename = cls.__name__ + ".json"
        with open(filename, "w") as jsonfile:
            if list_objs is None:
                jsonfile.write("[]")
            else:
                list_dicts = [o.to_dictionary() for o in list_objs]
                jsonfile.write(Base.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """Returns the result of deserializing a JSON string.
        """
        if json_string is None or json_string == "[]":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Create and return an instance of a class using a dictionary of attributes.
        """
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                new = cls(1, 1)
            else:
                new = cls(1)
            new.update(**dictionary)
            return new

    @classmethod
    def load_from_file(cls):
        """Returns a list of classes that have been created by parsing a file
          containing JSON strings.
        """
        filename = str(cls.__name__) + ".json"
        try:
            with open(filename, "r") as jsonfile:
                list_dicts = Base.from_json_string(jsonfile.read())
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Creates a CSV file representation of a collection of objects and save it to a file
        """
        filename = cls.__name__ + ".csv"
        with open(filename, "w", newline="") as csvfile:
            if list_objs is None or list_objs == []:
                csvfile.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """Returns a list of classes that were created by instantiating objects
          from a CSV file
        """
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, "r", newline="") as csvfile:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                list_dicts = csv.DictReader(csvfile, fieldnames=fieldnames)
                list_dicts = [dict([k, int(v)] for k, v in d.items())
                              for d in list_dicts]
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """
        Use Turtle module to create both rectangles and squares on a canvas.
        """
        skk = turtle.Turtle()
        skk.screen.bgcolor("#b7312c")
        skk.pensize(3)
        skk.shape("turtle")

        skk.color("#ffffff")
        for rect in list_rectangles:
            skk.showturtle()
            skk.up()
            skk.goto(rect.x, rect.y)
            skk.down()
            for i in range(2):
                skk.forward(rect.width)
                skk.left(90)
                skk.forward(rect.height)
                skk.left(90)
            skk.hideturtle()

        skk.color("#b5e3d8")
        for sq in list_squares:
            skk.showturtle()
            skk.up()
            skk.goto(sq.x, sq.y)
            skk.down()
            for i in range(2):
                skk.forward(sq.width)
                skk.left(90)
                skk.forward(sq.height)
                skk.left(90)
            skk.hideturtle()

        turtle.exitonclick()
