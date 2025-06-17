import xml.etree.ElementTree as ET

def serialize_to_xml(dictionary, filename):
    """Serialize a Python dictionary to an XML file."""
    try:
        root = ET.Element("data")

        for key, value in dictionary.items():
            child = ET.SubElement(root, key)
            child.text = str(value)  # Convert all values to string for XML

        tree = ET.ElementTree(root)
        tree.write(filename, encoding='utf-8', xml_declaration=True)
    except Exception:
        pass  # Optional: add logging or error reporting

def deserialize_from_xml(filename):
    """Deserialize an XML file back into a Python dictionary."""
    try:
        tree = ET.parse(filename)
        root = tree.getroot()

        result = {}
        for child in root:
            result[child.tag] = child.text

        return result
    except Exception:
        return None  # Fail gracefully

