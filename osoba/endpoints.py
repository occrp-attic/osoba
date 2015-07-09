from osoba.models import *
from osoba.bulkloaders import *
from osoba.core import db
from osoba import settings
from flask import request
from flask_restful import Resource

class ValidatedResource(Resource):
    def validate(self, data, template):
        out = {}
        for item, _type in template.iteritems():
            val = data.get(item)
            _type = _type.split(":")
            if _type[0] == "int":
                try: val = int(val)
                except: return False, "Value is not an integer (%s)" % val
                out[item] = val
            elif _type[0] == "list":
                options = _type[1:]
                if not val in options:
                    return False, "Invalid value for %s. Valid values: %s" % (
                                item, options)
                out[item] = val
            elif _type[0] == "string":
                if not type(val) in [str, unicode]:
                    return False, "Input data for '%s' is not a string (it's %s)" % (item, type(val))
                if len(_type) == 2:
                    maxlen = int(_type[1])
                    if not len(val) < maxlen:
                        return False, "Input data for %s too long (%d max)" % (
                            item, maxlen)
                out[item] = val
            else:
                print "Unknown data type in template"
                return False, "Unknown data type in template"
        return True, out

class Welcome(Resource):
    def get(self):
        val = {"message": "Welcome to Osoba v%s" % settings.VERSION}
        val["version"] = settings.VERSION
        val["entities"] = Entity.query.count()
        val["entity_properties"] = EntityProperty.query.count()
        val["relationships"] = Relationship.query.count()
        val["relationship_properties"] = RelationshipProperty.query.count()
        return val

class EntityCollection(ValidatedResource):
    def get(self):
        query = request.args.get("q")
        if not query:
            return {"q": None, "error": "Must provide query"}, 400
        return {"q": query}

    def post(self):
        template = {"type": "list:" + ":".join(OSOBA_ENTITY_TYPES)}
        res, out = self.validate(request.get_json(), template)
        if not res: return {"error": out}, 400

        e = create_entity(out.get("type"))
        return e.to_json()

class EntityMember(ValidatedResource):
    def get(self, eid):
        e = Entity.query.get(eid)
        return e.to_json()

    def put(self, eid):
        e = Entity.query.get(eid)

        template = {"key": "string", "value": "string"}
        res, out = self.validate(request.form, template)
        if not res: return {"error": out}, 400

        prop = e.set_prop(out["key"], out["value"])

        return prop.to_json()

    def patch(self, eid):
        try:    data = request.get_json()
        except: return {"error": "Not valid JSON"}, 400

        e = Entity.query.get(eid)
        for key, value in data.iteritems():
            if type(value) in [list, dict]:
                return {"error": "Property values may not be lists or dicts"}, 400

        for key, value in data.iteritems():
            e.set_prop(key, value)

        return e.to_json()

    def delete(self, eid):
        e = Entity.query.get(eid)
        db.session.delete(e)
        db.session.commit()
        return {"deleted": True, "eid": eid}


class RelationshipCollection(ValidatedResource):
    def post(self):
        template = {
            "to": "int",
            "from": "int",
            "type": "list:" + ":".join(OSOBA_RELATIONSHIP_TYPES)
        }
        res, out = self.validate(request.get_json(), template)
        if not res: return {"error": out}, 400

        r = create_relationship(out.get("type"), out.get("from"), out.get("to"))
        return r.to_json()

class RelationshipMember(ValidatedResource):
    def get(self, rid):
        e = Relationship.query.get(rid)
        return e.to_json()

    def put(self, rid):
        e = Relationship.query.get(rid)

        template = {"key": "string", "value": "string"}
        res, out = self.validate(request.form, template)
        if not res: return {"error": out}, 400

        prop = e.set_prop(out["key"], out["value"])

        return prop.to_json()

    def patch(self, rid):
        try:    data = request.get_json()
        except: return {"error": "Not valid JSON"}, 400

        e = Relationship.query.get(rid)
        for key, value in data.iteritems():
            if type(value) in [list, dict]:
                return {"error": "Property values may not be lists or dicts"}, 400

        for key, value in data.iteritems():
            e.set_prop(key, value)

        return e.to_json()

    def delete(self, rid):
        e = Relationship.query.get(rid)
        db.session.delete(e)
        db.session.commit()
        return {"deleted": True, "rid": rid}


class BulkLoader(Resource):
    LOADERS = {
        "json": JSONLoader,
        "csvpair": CSVLoader,
        "osoba": OsobaGraphLoader,
    }

    def post(self):
        print request.form
        print request.files
        loader = self.LOADERS.get(request.form.get("type"))
        if not loader:
            return {"error": "Unknown type", "valid": self.LOADERS.keys()}, 400
        results, status = loader().consume_request(request)
        return results, status
