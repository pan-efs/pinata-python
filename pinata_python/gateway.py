import requests
from dataclasses import dataclass

from .base import Pinata
from .utils.custom_typing import PinataResponse


@dataclass
class PublicGateway(Pinata):
    """Extended PublicGateway class. Inherits from Pinata. 

    Args:
        Pinata (class): pinata_python.base.Pinata
    """

    def retrieve_content(self, cid: str, save_to: str) -> PinataResponse:
        """See (https://docs.pinata.cloud/retrieving-content).

        Args:
            cid (str): The CID is the content identifier (also known as a hash) for the content you want to retrieve.
            
            save_to (str): The path that you want to save your content to.

        Returns:
            PinataResponse: See utils.custom_typing.py file.
        
        Example::
            
            from pinata_python.gateway import PublicGateway
            
            pinata = PublicGateway(AUTH="jwt", PINATA_JWT_TOKEN='<YOUR-JWT>')

            cid = '<YOUR-CID>'
            save_to = '<YOUR-PATH>'

            response = pinata.retrieve_content(cid, save_to)
            print(response)
        
        Results::
            
            200
            
        """
        _url = f"{self.PINATA_IPFS_GATEWAY}{cid}"
        headers = self.headers()

        response = requests.get(
                        _url,
                        headers=headers
                    )
        
        if response.status_code == 200:
            with open(save_to, 'wb') as file:
                file.write(response.content)
                file.close()
        
        return response.status_code if response.status_code == 200 else {"error": response.status_code, "reason": response.reason, "text": response.text}

