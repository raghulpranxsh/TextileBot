import requests

TALLY_URL = "http://localhost:9000"

def get_stock_summary():

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

    response = requests.post(TALLY_URL, data=xml_request)

    return response.text
