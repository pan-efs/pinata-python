import requests
from dataclasses import dataclass

from .base import Pinata
from .utils.custom_typing import Options, PinataResponse


@ dataclass
class Data(Pinata):
    """Extended Data class. Inherits from Pinata. 

    Args:
        Pinata (class): pinata_python.base.Pinata
    """
    
    def pin_list(self, options: Options=None) -> PinataResponse:
        """See (https://docs.pinata.cloud/data/query-pins).

        Args:
            options (Options, optional): The filters from the available filters and/or metadata querying. Defaults to None.

        Returns:
            PinataResponse: See utils.custom_typing.py file.
        
        Example::
            
            from pinata_python.data import Data

            pinata = Data(AUTH="jwt", PINATA_JWT_TOKEN='<YOUR-JWT>')

            options = {
                        'pinStart': '2022-04-16T00:00:00.000Z',
                        'pinEnd': '2022-04-19T00:00:00.000Z',
                        'status': 'pinned',
                        'pageLimit': 1,
                        'nameContains': 'oleoleole'
                    }
            
            response = pinata.pin_list(options=options)
            print(response) # it's empty
        
        Results::

            {
                'count': 0, 
                'rows': []
            }
        """
        _url = f"{self.PINATA_BASE_URL}{self.QUERY_PINS}"
        headers = self.headers()
        params = {}
        
        if options:
            if "hashContains" in options:
                params["hashContains"] = options["hashContains"]
            
            if "pinStart" in options:
                params["pinStart"] = options["pinStart"]
            
            if "pinEnd" in options:
                params["pinEnd"] = options["pinEnd"]
            
            if "unpinStart" in options:
                params["unpinStart"] = options["unpinStart"]
            
            if "unpinEnd" in options:
                params["unpinEnd"] = options["unpinEnd"]
            
            if "pinSizeMin" in options:
                params["pinSizeMin"] = options["pinSizeMin"]
            
            if "pinSizeMax" in options:
                params["pinSizeMax"] = options["pinSizeMax"]
            
            if "status" in options:
                params["status"] = options["status"]
            
            if "pageLimit" in options:
                params["pageLimit"] = options["pageLimit"]
            
            if "pageOffset" in options:
                params["pageOffset"] = options["pageOffset"]
            
            if "nameContains" in options:
                params["metadata[name]"] = options["nameContains"]
            
            if "keyvalues" in options:
                params["metadata[keyvalues]"] = options["keyvalues"]
        
        response = requests.get(
                        _url,
                        params=params,
                        headers=headers
                    )
        
        return response.json() if response.status_code == 200 else {"error": response.status_code, "reason": response.reason, "text": response.text}


    def user_pinned_data_total(self) -> PinataResponse:
        """See (https://docs.pinata.cloud/data/data-usage).

        Returns:
            PinataResponse: See utils.custom_typing.py file.
        
        Example::
           
           from pinata_python.data import Data

           pinata = Data(AUTH="jwt", PINATA_JWT_TOKEN='<YOUR-JWT>')

           response = pinata.user_pinned_data_total()
           print(response)
        
        Results::
            
            {
                'pin_count': int,
                'pin_size_total': str,
                'pin_size_with_replications_total': str
            }

            
        """
        _url = f"{self.PINATA_BASE_URL}{self.DATA_USAGE}"
        headers = self.headers()

        response = requests.get(
                        _url,
                        headers=headers
                    )
        
        return response.json() if response.status_code == 200 else {"error": response.status_code, "reason": response.reason, "text": response.text}
