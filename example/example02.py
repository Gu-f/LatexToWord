from docx import Document
from latex2word import LatexToWordElement

"""
`pip install python-docx`  
使用element更加灵活，你可以在你想要的任何地方插入element，只要它支持lxml.etree._Element结构，包括但不限于Word。  
With element, you can insert an element wherever you want, as long as it supports the lxml.etree._Element structure, including but not limited to Word.
"""

# 公式(Latex string)
latex_input = r"x={-b \pm \sqrt{b^2-4ac}\over 2a}"
# 构建latex_element对象 (Build a latex element object)
latex_element = LatexToWordElement(latex_input).element()

# 插入word公式(Create the docx file and insert the element)
doc = Document()
paragraph = doc.add_paragraph()
paragraph._element.append(latex_element)

doc.save('test.docx')
