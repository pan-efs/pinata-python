import requests
from dataclasses import dataclass

from .base import Pinata
from .utils.custom_typing import Options, PinataResponse


@dataclass
class Users(Pinata):
    """Extended Users class. Inherits from Pinata. 

    Args:
        Pinata (class): pinata_python.base.Pinata
    """
    
    def generate_keys(
        self,
        key_name: str="default_pinata",
        admin: bool=False,
        pin_list: bool=True,
        user_pinned_data_total: bool=True,
        hash_metadata: bool=True,
        hash_pin_policy: bool=True,
        pin_by_hash: bool=True,
        pin_file_to_ipfs: bool=True,
        pin_json_to_ipfs: bool=True,
        pin_jobs: bool=True,
        unpin: bool=True,
        user_pin_policy: bool=True,
        options: Options=None
    ) -> PinataResponse:

        """See (https://docs.pinata.cloud/user/generate-api-key).

        Args:
            key_name (str, optional): The name of the key. Defaults to "default_pinata".

            admin (bool, optional): Admin permissions. Defaults to False.

            pin_list (bool, optional): API Endpoint Access. Defaults to True.

            user_pinned_data_total (bool, optional): API Endpoint Access. Defaults to True.

            hash_metadata (bool, optional): API Endpoint Access. Defaults to True.

            hash_pin_policy (bool, optional): API Endpoint Access. Defaults to True.

            pin_by_hash (bool, optional): API Endpoint Access. Defaults to True.

            pin_file_to_ipfs (bool, optional): API Endpoint Access. Defaults to True.

            pin_json_to_ipfs (bool, optional): API Endpoint Access. Defaults to True.

            pin_jobs (bool, optional): API Endpoint Access. Defaults to True.

            unpin (bool, optional): API Endpoint Access. Defaults to True.

            user_pin_policy (bool, optional): API Endpoint Access. Defaults to True.
            
            options (Options, optional): The dictionary with keyword max_uses. Defaults to None.

        Returns:
            PinataResponse: See utils.custom_typing.py file.
        
        Example::
            
            from pinata_python.users import Users

            pinata = Users(AUTH="jwt", PINATA_JWT_TOKEN='<YOUR-JWT>')
    
            response = pinata.generate_keys()
            print(response)
        
        Results::

            {
                'JWT': str,
                'pinata_api_key': str,
                'pinata_api_secret': str
            }
        """
        _url = f"{self.PINATA_BASE_URL}{self.GENERATE_API_KEYS}"
        headers = self.headers()
        
        if admin:
            body = {
                    "keyName": key_name,
                    "permissions": {
                        "admin": admin
                }
            }
        else:
            body = {
                    "keyName": key_name,
                    "permissions": {
                        "endpoints": {
                            "data": {
                                "pinList": pin_list,
                                "userPinnedDataTotal": user_pinned_data_total
                            },
                            "pinning": {
                                "hashMetadata": hash_metadata,
                                "hashPinPolicy": hash_pin_policy,
                                "pinByHash": pin_by_hash,
                                "pinFileToIPFS": pin_file_to_ipfs,
                                "pinJSONToIPFS": pin_json_to_ipfs,
                                "pinJobs": pin_jobs,
                                "unpin": unpin,
                                "userPinPolicy": user_pin_policy
                            }
                        }
                    }
                }
        
        if options:
            if "maxUses" in options:
                body["maxUses"] = options["maxUses"]
        
        response = requests.post(
                        _url,
                        json=body,
                        headers=headers
                    )
        
        return response.json() if response.status_code == 200 else {"error": response.status_code, "reason": response.reason, "text": response.text}
    

    def revoke_key(self, apikey: str) -> PinataResponse:
        """See (https://docs.pinata.cloud/user/revoke-api-key).

        Args:
            apikey (str): The key to revoke.

        Returns:
            PinataResponse: See utils.custom_typing.py file.
        
        Example::
            
            from pinata_python.users import Users

            pinata = Users(AUTH="jwt", PINATA_JWT_TOKEN='<YOUR-JWT>')
            
            key = '<YOUR-KEY>'

            response = pinata.revoke_key(key)
            print(response)
        
        Results::
            
            'Revoked'

        """
        _url = f"{self.PINATA_BASE_URL}{self.REVOKE_API_KEY}"
        headers = self.headers()
        body = {
                "apiKey": apikey
            }
        
        response = requests.put(
                    _url,
                    json=body,
                    headers=headers
                )
        
        return response.json() if response.status_code == 200 else {"error": response.status_code, "reason": response.reason, "text": response.text}
