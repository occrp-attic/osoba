from osoba.models import *
import csv

class OsobaBulkLoader:
    def consume_request(self, request):
        pass

class JSONLoader(OsobaBulkLoader):
    def consume_request(self, request):
        data = self.get_json()
        return self.consume(data), 400

    def consume(self, data):
        # First, consume nodes:
        pass
        # Second, consume edges:
        pass

class CSVLoader(OsobaBulkLoader):
    def __init__(self):
        self.nodes = []

    def consume_request(self, request):
        print "Loading CSV!"
        if len(request.files) != 2:
            return {"error": "Need exactly 2 files."}, 400
        if request.files.keys() != ["nodes", "edges"]:
            return {"error": "Provide 'nodes' and 'edges'."}, 400

        edges = request.files["edges"]
        nodes = request.files["nodes"]
        res1, status = self.consume_nodes(nodes)
        if status != 200:
            return res1, status
        res2, status = self.consume_edges(edges)
        if status != 200:
            return res2, status
        return {"nodes": res1, "edges": res2}, 200

    def consume_nodes(self, data):
        added = 0
        nodereader = csv.DictReader(data)
        for node in nodereader:
            if not node.get("type"):
                return {"error": "Line %d of nodes doesn't have type" %
                        nodereader.line_num}, 400
            t = node.get("type")
            if not t in OSOBA_ENTITY_TYPES:
                return {"error": "%s isn't a valid type.",
                        "valid": OSOBA_ENTITY_TYPES}, 400

            del node["type"]
            n = create_entity(t, properties=node)
            self.nodes.append((node, n.id))
            added += 1

        return {"added": added}, 200

    def consume_edges(self, data):
        added = 0
        nodereader = csv.DictReader(data)
        for node in nodereader:
            if not node.get("type"):
                return {"error": "Line %d of edges doesn't have type" %
                        nodereader.line_num}, 400
            if not node.get("from"):
                return {"error": "Line %d of edges doesn't have from" %
                        nodereader.line_num}, 400
            if not node.get("to"):
                return {"error": "Line %d of edges doesn't have to" %
                        nodereader.line_num}, 400
            t = node.get("type")
            _from = node.get("from")
            _to = node.get("to")

            if _from.startswith("ref:"):
                oldfrom = _from
                tok = _from.split(":")
                field = tok[1]
                value = tok[2]
                for items in self.nodes:
                    if items[0][field] == value:
                        _from = items[1]
                        break
                if _from == oldfrom:
                    return {"error": "Couldn't find reference '%s'" % value}, 400

            if _to.startswith("ref:"):
                oldto = _to
                tok = _to.split(":")
                field = tok[1]
                value = tok[2]
                for items in self.nodes:
                    if items[0][field] == value:
                        _to = items[1]
                        break
                if _to == oldto:
                    return {"error": "Couldn't find reference '%s'" % value}, 400


            if not t in OSOBA_RELATIONSHIP_TYPES:
                return {"error": "%s isn't a valid type." % t,
                        "valid": OSOBA_ENTITY_TYPES}, 400

            del node["type"]
            del node["from"]
            del node["to"]
            n = create_relationship(t, _from, _to, properties=node)
            added += 1

        return {"added": added}, 200


class OsobaGraphLoader(OsobaBulkLoader):
    pass
