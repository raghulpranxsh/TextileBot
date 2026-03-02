import requests

url = "http://192.168.64.2:9000"

xml_request = """
<ENVELOPE>
 <HEADER>
  <VERSION>1</VERSION>
  <TALLYREQUEST>Export</TALLYREQUEST>
  <TYPE>Collection</TYPE>
  <ID>StockItems</ID>
 </HEADER>
 <BODY>
  <DESC>
   <STATICVARIABLES>
    <SVEXPORTFORMAT>$$SysName:XML</SVEXPORTFORMAT>
   </STATICVARIABLES>
   <TDL>
    <TDLMESSAGE>
     <COLLECTION NAME="StockItems" ISMODIFY="No">
      <TYPE>Stock Item</TYPE>
      <FETCH>Name,OpeningBalance,ClosingBalance,BaseUnits</FETCH>
     </COLLECTION>
    </TDLMESSAGE>
   </TDL>
  </DESC>
 </BODY>
</ENVELOPE>
"""

response = requests.post(url, data=xml_request, timeout=10)
response.raise_for_status()

print(response.text)
