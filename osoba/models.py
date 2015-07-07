from osoba.core import db

class Entity(db.Model):
    __tablename__ = "osoba_entities"

    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String, index=True)

class Relationship(db.Model):
    __tablename__ = "osoba_relationships"

    id = db.Column(db.Integer, primary_key=True)
    _from = db.Column(db.Integer)
    to = db.Column(db.Integer)
    type = db.Column(db.String, index=True)

class NodePerson(db.Model):
    __tablename__ = "osoba_node_person"

    id = db.Column(db.Integer, primary_key=True)
    nationality = db.Column(db.String)
    first_name = db.Column(db.String)
    middle_names = db.Column(db.String)
    last_name = db.Column(db.String)

class NodeCompany(db.Model):
    __tablename__ = "osoba_node_company"

    id = db.Column(db.Integer, primary_key=True)
    country = db.Column(db.String)
    incorporated_date = db.Column(db.Date)
    dissolved_date = db.Column(db.Date)
