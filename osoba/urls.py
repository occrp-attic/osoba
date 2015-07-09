from osoba.endpoints import *
from osoba.core import api

urls = [
    (Welcome, "/"),
    (EntityCollection, "/entity/"),
    (EntityMember, "/entity/<int:eid>"),
    (RelationshipCollection, "/relationship/"),
    (RelationshipMember, "/relationship/<int:rid>"),
    (BulkLoader, "/bulk/"),
]

for url in urls:
    api.add_resource(*url)
