import xml.sax
import latex2mathml.converter
from lxml import etree
from .handler import OMMLMathMLHandler


def _convert(mathml_xml, additional_entities=None):
    """
    Convert MathML text to OMML text
    """
    handler = OMMLMathMLHandler()
    entities = {
        'pi': 0x03c0,
        'ExponentialE': 0x2147,
        'ee': 0x2147,
        'ImaginaryI': 0x2148,
        'ii': 0x2148,
        'gamma': 0x03b3,
        'infin': 0x221e,
        'infty': 0x221e,
    }
    if additional_entities is not None:
        entities.update(additional_entities)
    input_xml = (
            r"""<!DOCTYPE math [ """ +
            ''.join('<!ENTITY %s "&#x%04X;">' % item for item in entities.items()) +
            r""" ]>""" +
            mathml_xml)
    xml.sax.parseString(input_xml, handler)
    return handler.result()


class LatexToWordElement(object):
    def __init__(self, latex: str):
        self.latex = latex
        self._mathml = None
        self._omml = None

    def _build_xmlns(self):
        xmlns = ' '.join([
            'xmlns:m="http://schemas.openxmlformats.org/officeDocument/2006/math"',
            'xmlns:mml="http://www.w3.org/1998/Math/MathML"'
        ])
        return xmlns

    def element(self):
        self._mathml = latex2mathml.converter.convert(self.latex)
        self._omml = _convert(self._mathml).format(xmlns=self._build_xmlns())
        return etree.fromstring(self._omml)

    def add_latex_to_paragraph(self, paragraph):
        paragraph._element.append(self.element())
