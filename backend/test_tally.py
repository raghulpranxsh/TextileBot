import requests

url = "http://localhost:9000"

xml_request = """
<ENVELOPE>
 <HEADER>
  <TALLYREQUEST>Export Data</TALLYREQUEST>
 </HEADER>
 <BODY>
  <EXPORTDATA>
   <REQUESTDESC>
    <REPORTNAME>Stock Summary</REPORTNAME>
   </REQUESTDESC>
  </EXPORTDATA>
 </BODY>
</ENVELOPE>
"""

response = requests.post(url, data=xml_request)

print(response.text)
