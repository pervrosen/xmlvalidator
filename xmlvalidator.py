import streamlit as sf
from lxml.etree import parse, XMLSchema

sf.write("XML validator")
XSDf = sf.file_uploader("XSD file")
XMLf = sf.file_uploader("XML file")

if XMLf!=None and XSDf!=None:
   xml_file = parse(XMLf)
   xml_validator = XMLSchema(parse(XSDf))

   is_valid = xml_validator.validate(xml_file)

   sf.text("Is valid: {}".format(is_valid))

