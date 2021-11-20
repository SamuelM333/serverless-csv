from pynamodb.models import Model
from pynamodb.attributes import UnicodeAttribute


class Csv(Model):
    class Meta:
        table_name = 'csv'

    _id = UnicodeAttribute(hash_key=True)
    serial_number = UnicodeAttribute(range_key=True)
    company_name = UnicodeAttribute()
    employee_markme = UnicodeAttribute()
    description = UnicodeAttribute()
    leave = UnicodeAttribute()
