# This class is use for converting json response to a general object.
# In order to query data from json response easily

class Generic:
    @classmethod
    def from_dict(cls, dict):
        obj = cls()
        obj.__dict__.update(dict)
        return obj
