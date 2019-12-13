import os

from postgresqleu.util.misc.baseinvoice import BaseInvoice, BaseRefund

class FOSSNorthBase(object):
    logo = os.path.abspath(os.path.join(__file__, "../../media/img/logo-black.png"))
    headertext = """FOSS North Conferences ek.för.
Godkänd för f-skatt
Org.nr. 769631-2821
VAT / MOMS #: SE769631282101
Web: https://www.foss-north.se
"""
    sendertext = """Your contact:
Johan Thelin
Email: info@foss-north.se
"""

    bankinfotext = """Bankgiro: 5063-6299
SWIFT: SWEDSESS
IBAN: SE6180000830481231357656"""

    paymentterms = """Payment terms:
30 dagar / 30 days net"""

class FOSSNorthInvoice(FOSSNorthBase, BaseInvoice):
    pass

class FOSSNorthRefund(FOSSNorthBase, BaseRefund):
    pass


