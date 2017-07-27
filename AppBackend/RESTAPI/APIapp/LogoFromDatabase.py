# from .models import Map, Logo, MapHasLogo, MapHasTags, Tag
# # from django.core import serializers
# # from rest_framework import serializers
# from serializers import TagSerializer
# from django.forms.models import model_to_dict
import sqlite3


def getMapFromLogo(logo):
    conn = sqlite3.connect('/Users/Hallshit/Documents/KnowledgeVC/AppBackend/RESTAPI/db.sqlite3')
    conn.text_factory = str
    c = conn.cursor()
    c.execute("SELECT * FROM APIapp_logo WHERE company LIKE (?)", [logo])
    print c.fetchall()
    c.execute(
        "SELECT name FROM APIapp_map WHERE APIapp_map.id IN (SELECT mapID_id FROM APIapp_maphaslogo WHERE logoID_id IN (SELECT id FROM APIapp_logo WHERE APIapp_logo.company LIKE (?)))",
        [logo])
    return c.fetchone()[0]



