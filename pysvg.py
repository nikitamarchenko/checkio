__author__ = 'nmarchenko'

__author__ = 'nmarchenko'

import pysvg.structure
import pysvg.builders
import pysvg.text

svg_document = pysvg.structure.Svg()

shape_builder = pysvg.builders.ShapeBuilder()

svg_document.addElement(shape_builder.createRect(0, 0,
                                                 "200px", "100px",
                                                 strokewidth = 1,
                                                 stroke = "black",
                                                 fill = "rgb(255, 255, 0)"))

svg_document.addElement(pysvg.text.Text("Hello World", x = 210, y = 110))

print(svg_document.getXML())

svg_document.save("test-pysvg.svg")