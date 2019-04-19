import json


class ObjectSerializer: 
    def serialize(self, serializable, format):
        serializer = factory.get_serializer(format) #pick the concrete instructions
        serializable.serialize(serializer) #run the concrete instructions on the data object
        return serializer.to_str()



#Creator/Factory
class SerializeFactory:
    def get_serializer(self, format):
        if format == 'JSON':
            return JsonSerializer()
        elif format == 'XML':
            return XmlSerializer()
        else:
            raise ValueError(format)


#Product
class JsonSerializer:
    def __init__(self):
        self._current_object = None

    def start_object(self, object_name, object_id):
        self._current_object = {
            'id': object_id
        }

    def add_property(self, name, value):
        self._current_object[name] = value

    def to_str(self):
        return json.dumps(self._current_object)