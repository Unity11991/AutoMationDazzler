import xml.etree.ElementTree as ET

def updateXML(fileName):
    tree=ET.ElementTree(file=fileName)
    root = tree.getroot()

    for values in root.iter("value"):
        values.text="nn"

        tree=ET.ElementTree(root)

        with open(fileName,"wb") as fileUpdate:
            tree.write(fileUpdate)

if __name__=="__main__":
    updateXML("/etc/hadoop/hdfs-site.xml")
