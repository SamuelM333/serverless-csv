from pynamodb.models import Model
from pynamodb.attributes import UnicodeAttribute


class Csv(Model):
    class Meta:
        table_name = 'csv'

    _id = UnicodeAttribute(hash_key=True)
