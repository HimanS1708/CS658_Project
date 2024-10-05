#!/usr/bin/env python

class cPDFiDTriage(cPluginParent):
    onlyValidPDF = False
    name = 'Triage plugin'

    def __init__(self, oPDFiD, options):
        self.options = options
        self.oPDFiD = oPDFiD

    def Score(self):
        for keyword in ('/JS', '/JavaScript', '/AA', '/OpenAction', '/AcroForm', '/JBIG2Decode', '/RichMedia', '/Launch', '/EmbeddedFile', '/XFA', '/Colors > 2^24'):
            if keyword in self.oPDFiD.keywords and self.oPDFiD.keywords[keyword].count > 0:
                return 1.0
        if self.options != '--io':
            for keyword in ('/ObjStm', ):
                if keyword in self.oPDFiD.keywords and self.oPDFiD.keywords[keyword].count > 0:
                    return 0.75
            for keyword in ('/URI', ):
                if keyword in self.oPDFiD.keywords and self.oPDFiD.keywords[keyword].count > 0:
                    return 0.6
            if self.oPDFiD.keywords['obj'].count != self.oPDFiD.keywords['endobj'].count:
                return 0.5
            if self.oPDFiD.keywords['stream'].count != self.oPDFiD.keywords['endstream'].count:
                return 0.5
        return 0.0

    def Instructions(self, score):
        if score == 1.0:
            return 'Sample is likely malicious and requires further analysis'

        if score == 0.75:
            return '/ObjStm detected, analyze sample with pdfid-objstm.bat'

        if score == 0.5:
            return 'Sample is likely not malicious but requires further analysis'

        if score == 0.6:
            return 'Sample is likely not malicious but could contain phishing or payload URL'

        if score == 0.0:
            return 'Sample is likely not malicious, unless you suspect this is used in a targeted/sophisticated attack'

        return ''

AddPlugin(cPDFiDTriage)
