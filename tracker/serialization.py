class BaseSerialization:

    _model = None

    def serializer(self, instance):
        raise NotImplemented('Abstract class serialize not implemented')

    def deserializer(self, data):
        raise NotImplemented('Abstract class serialize not implemented')