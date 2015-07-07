from osoba.endpoints import *

urls = [
    (EntityCollection, "/entity/"),
    (EntityMember, "/entity/<int:id>")
]
