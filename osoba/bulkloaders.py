from osoba.models import *

class OsobaBulkLoader:
    def consume_request(self, request):
        pass

class JSONLoader(OsobaBulkLoader):
    def consume_request(self, request):
        data = self.get_json()
        self.consume(data)

    def consume(self, data):
        # First, consume nodes:
        pass
        # Second, consume edges:
        pass

class CSVLoader(OsobaBulkLoader):
    pass

class OsobaGraphLoader(OsobaBulkLoader):
    pass
    
