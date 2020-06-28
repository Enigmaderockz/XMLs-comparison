import xml.etree.ElementTree as ET

tree = ET.parse("data.xml")

# this element holds the phonebook entries
container = tree.find("entries")

data = []
for elem in container:
    key = elem.find(".//accinfo/acctname").text
    data.append((key, elem))

data.sort()

# insert the last item from each tuple
container[:] = [item[-1] for item in data]

tree.write("ndata.xml")


<phonebook>
  <entries>
    <entry>
      <accinfo>
        <acctname>68103345678</acctname>
        <number>555-8904</number>
        <basic>
        <basicname>hey</basicname>
        </basic>
      </accinfo>  
    </entry>
    <entry>
      <accinfo>
        <acctname>68103345677</acctname>
        <number>555-5782</number>
      </accinfo>
    </entry>
    <entry>
      <accinfo>
        <acctname>68103345679</acctname>
        <number>555-3642</number>
      </accinfo>
    </entry>
  </entries>
</phonebook>
