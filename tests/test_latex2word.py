import unittest
import lxml.etree

from latex2word import LatexToWordElement


class TestLatex2Word(unittest.TestCase):
    def test_LatexToWordElement(self):
        element = LatexToWordElement('x={-b \pm \sqrt{b^2-4ac}\over 2a}').element()
        current_omml = b'<m:oMath xmlns:m="http://schemas.openxmlformats.org/officeDocument/2006/math" xmlns:mml="http://www.w3.org/1998/Math/MathML"><m:box><m:e><m:r><m:rPr><m:sty m:val="i"/></m:rPr><m:t>x</m:t></m:r><m:r><m:rPr><m:sty m:val="p"/></m:rPr><m:t>=</m:t></m:r><m:box><m:e><m:f><m:num><m:box><m:e><m:r><m:rPr><m:sty m:val="p"/></m:rPr><m:t>&#8722;</m:t></m:r><m:r><m:rPr><m:sty m:val="i"/></m:rPr><m:t>b</m:t></m:r><m:r><m:rPr><m:sty m:val="i"/></m:rPr><m:t>&#177;</m:t></m:r><m:rad><m:e><m:box><m:e><m:box><m:e><m:sSup><m:e><m:r><m:rPr><m:sty m:val="i"/></m:rPr><m:t>b</m:t></m:r></m:e><m:sup><m:r><m:rPr><m:sty m:val="p"/></m:rPr><m:t>2</m:t></m:r></m:sup></m:sSup><m:r><m:rPr><m:sty m:val="p"/></m:rPr><m:t>&#8722;</m:t></m:r><m:r><m:rPr><m:sty m:val="p"/></m:rPr><m:t>4</m:t></m:r><m:r><m:rPr><m:sty m:val="i"/></m:rPr><m:t>a</m:t></m:r><m:r><m:rPr><m:sty m:val="i"/></m:rPr><m:t>c</m:t></m:r></m:e></m:box></m:e></m:box></m:e></m:rad></m:e></m:box></m:num><m:den><m:box><m:e><m:r><m:rPr><m:sty m:val="p"/></m:rPr><m:t>2</m:t></m:r><m:r><m:rPr><m:sty m:val="i"/></m:rPr><m:t>a</m:t></m:r></m:e></m:box></m:den></m:f></m:e></m:box></m:e></m:box></m:oMath>'
        self.assertEqual(lxml.etree.tostring(element), current_omml)


if __name__ == '__main__':
    unittest.main()
