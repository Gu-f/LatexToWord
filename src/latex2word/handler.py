from mathml2omml import MathMLHandler, Math


class OMMLMath(Math):
    """
    Top-Level Element
    """

    def to_str(self):
        math_xml_text = super().to_str()
        _START = '<m:oMath>'
        _END = '</m:oMath>'
        xml_text = math_xml_text[len(_START):-len(_END)]
        return '<m:oMath {xmlns}>%s</m:oMath>' % xml_text


class OMMLMathMLHandler(MathMLHandler):
    CONVERSION_MAP = {**MathMLHandler.CONVERSION_MAP, OMMLMath.name: OMMLMath}

    def startElement(self, name, attrs):
        if name in MathMLHandler.IGNORED_ELEMENTS:
            self._in_ignore_elems += 1
            return
        if self._in_ignore_elems > 0 or name in MathMLHandler.SKIPPED_ELEMENTS:
            return
        if name not in OMMLMathMLHandler.CONVERSION_MAP:
            raise NotImplementedError(name + ' is not Implemented')
        self._stack.append(OMMLMathMLHandler.CONVERSION_MAP[name](attrs))
