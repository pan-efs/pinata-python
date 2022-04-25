import os
import glob
import requests
from dataclasses import dataclass
from typing import Any, Dict

from .base import Pinata
from .utils.custom_typing import Options, PinataResponse


@dataclass
class Pinning(Pinata):
    """Extended Pinning class. Inherits from Pinata. 

    Args:
        Pinata (class): pinata_python.base.Pinata
    """

    def pin_file_to_ipfs(self, filepath: str, extension: str='') -> PinataResponse:
        """See (https://docs.pinata.cloud/api-pinning/pin-file).

        Args:
            filepath (str): The path of the desired file.

            extension (str): The desired file extension, i.e. '.png'. Defaults to '', which means all files.

        Returns:
            PinataResponse: See utils.custom_typing.py file.
        
        Example::
            
            from pinata_python.pinning import Pinning

            pinata = Pinning(AUTH="jwt", PINATA_JWT_TOKEN='<YOUR-JWT>')

            filepath = '<YOUR-FILEPATH>'

            response = pinata.pin_file_to_ipfs(filepath)
            print(response)
        
        Results::
           
           {
                'IpfsHash': str,
                'PinSize': int,
                'Timestamp': str, # ISO 8601 format
           }

        """
        _url = f"{self.PINATA_BASE_URL}{self.PIN_FILE_TO_IPFS}"
        headers = self.headers()
        
        if not os.path.isdir(filepath):
            filename = filepath.split('/')[-1:][0]
            with open(filepath, "rb") as f:
                _binary = f.read()
                files = {"file": (filename, _binary)}
        else:
            _files = glob.glob(f"{filepath}/*{extension}")
            files = [("file", (file, open(file, "rb"))) for file in _files]
        
        response = requests.post(
                        _url,
                        files=files,
                        headers=headers
                    )
        
        return response.json() if response.status_code == 200 else {"error": response.status_code, "reason": response.reason, "text": response.text}
    

    def pin_json_to_ipfs(self, json_struct: Dict[str, Any], options: Options=None) -> PinataResponse:
        """See (https://docs.pinata.cloud/api-pinning/pin-json).

        Args:
            json_struct (Dict[str, Any]): The json file.

            options (Options, optional): The dictionary with keywords 'pinataOptions' and/or 'pinataMetadata'. Defaults to None.

        Returns:
            PinataResponse: See utils.custom_typing.py file.
        
        Example::
            
            from pinata_python.pinning import Pinning

            pinata = Pinning(AUTH="jwt", PINATA_JWT_TOKEN='<YOUR-JWT>')

            player = {'name': 'goku', 'surname': 'son goku'}
            options = {
                'pinataMetadata': {
                    'name': 'player1',
                    'keyvalues': {
                        'power': 10,
                        'stamina': 'high',
                        'skill': 'jumping'
                    }  
                }
            }
        
            response = pinata.pin_json_to_ipfs(player, options)
            print(response)
        
        Results::
            
            {
                'IpfsHash': str,
                'PinSize': int,
                'Timestamp': str, # ISO 8601 format
            }

        """
        _url = f"{self.PINATA_BASE_URL}{self.PIN_JSON_TO_IPFS}"
        headers = self.headers()
        body = {
                "pinataContent": json_struct
            }
        
        if options:
            if "pinataMetadata" in options:
                body["pinataMetadata"] = options["pinataMetadata"]

            if "pinataOptions" in options:
                body["pinataOptions"] = options["pinataOptions"]

        response = requests.post(
                        _url,
                        json=body,
                        headers=headers
                    )
        
        return response.json() if response.status_code == 200 else {"error": response.status_code, "reason": response.reason, "text": response.text}
    

    def pin_by_hash(self, hash_to_pin: str, options: Options=None) -> PinataResponse:
        """See (https://docs.pinata.cloud/api-pinning/pin-by-hash).

        Args:
            hash_to_pin (str): The hash string that you want to pin.

            options (Options, optional): The dictionary with keywords 'pinataOptions' and/or 'pinataMetadata'. Defaults to None.

        Returns:
            PinataResponse: See utils.custom_typing.py file.
        
        Example::
            
            from pinata_python.pinning import Pinning

            pinata = Pinning(AUTH="jwt", PINATA_JWT_TOKEN='<YOUR-JWT>')

            options = {
                       'pinataMetadata': {
                           'name': 'alice',
                           'keyvalues': {
                               'power': 100,
                               'stamina': 'high',
                               'job': 'queen'
                           }  
                       }
                   }
            hashstring = '<YOUR-HASHSTRING>'
               
            response = pinata.pin_by_hash(hashstring, options)
            print(response)
        
        Results::
            
            {
                'id': str,
                'IpfsHash': str,
                'PinSize': int,
                'Timestamp': str, # ISO 8601 format
            }

        """
        _url = f"{self.PINATA_BASE_URL}{self.PIN_BY_HASH}"
        headers = self.headers()
        body = {
                "hashToPin": hash_to_pin
            }
        
        if options:
            if "pinataMetadata" in options:
                body["pinataMetadata"] = options["pinataMetadata"]

            if "pinataOptions" in options:
                body["pinataOptions"] = options["pinataOptions"]
        
        response = requests.post(
                        _url,
                        json=body,
                        headers=headers
                    )
        
        return response.json() if response.status_code == 200 else {"error": response.status_code, "reason": response.reason, "text": response.text}


    def unpin(self, hash_string: str) -> PinataResponse:
        """See (https://docs.pinata.cloud/api-pinning/unpin).

        Args:
            hash_string (str): The hash string that you want to unpin.

        Returns:
            PinataResponse: See utils.custom_typing.py file.
        
        Example::
            
            from pinata_python.pinning import Pinning

            pinata = Pinning(AUTH="jwt", PINATA_JWT_TOKEN='<YOUR-JWT>')

            cid = '<YOUR-CID>'

            response = pinata.unpin(cid)
            print(response)
        
        Results::
            
            200

        """
        _url = f"{self.PINATA_BASE_URL}{self.UNPIN}{hash_string}"
        headers = self.headers()
        headers["Content-Type"] = "application/json"

        response = requests.delete(
                        _url,
                        headers=headers
                    )
        
        return response.status_code if response.status_code == 200 else {"error": response.status_code, "reason": response.reason, "text": response.text}
    

    def hash_metadata(self, ipfs_pin_hash: str, options: Options=None) -> PinataResponse:
        """See (https://docs.pinata.cloud/api-pinning/hash-metadata).

        Args:
            ipfs_pin_hash (str): The hash of the content you with to change the pin policy for.

            options (Options, optional): The dictionary with keywords 'name' and/or 'keyvalues'. Defaults to None.

        Returns:
            PinataResponse: See utils.custom_typing.py file.
        
        Example::
            
            from pinata_python.pinning import Pinning

            pinata = Pinning(AUTH="jwt", PINATA_JWT_TOKEN='<YOUR-JWT>')

            cid = '<YOUR-CID>'
            options = {
                         'name': 'alice',
                         'keyvalues': {
                                'power': 100,
                                'stamina': 'high',
                                'job': 'queen'
                        } 
                    }

            response = pinata.hash_metadata(cid, options)
            print(response)
        
        Results::
            
            200

        """
        _url = f"{self.PINATA_BASE_URL}{self.HASH_METADATA}"
        headers = self.headers()
        body = {
                "ipfsPinHash": ipfs_pin_hash
            }
        
        if options:
            if "name" in options:
                body["name"] = options["name"]
            
            if "keyvalues" in options:
                body["keyvalues"] = options["keyvalues"]
        
        response = requests.put(
                        _url,
                        json=body,
                        headers=headers
                    )
        
        return response.status_code if response.status_code == 200 else {"error": response.status_code, "reason": response.reason, "text": response.text}
    

    def hash_pin_policy(self, ipfs_pin_hash: str, new_pin_policy: Dict[str, Any]) -> PinataResponse:
        """See (https://docs.pinata.cloud/api-pinning/hash-pin-policy).

        Args:
            ipfs_pin_hash (str): The hash of the content you with to change the pin policy for.

            new_pin_policy (Dict[str, Any]): The new pin policy that you want to apply.

        Returns:
            PinataResponse: See utils.custom_typing.py file.
        
        Example::
            
            from pinata_python.pinning import Pinning

            pinata = Pinning(AUTH="jwt", PINATA_JWT_TOKEN='<YOUR-JWT>')

            cid = '<YOUR-CID>'
            new_pin_policy = {
                                'regions': [
                                    {
                                        'id': 'FRA1',
                                        'desiredReplicationCount': 1
                                    }
                                ]
                            }
    
            response = pinata.hash_pin_policy(cid, new_pin_policy)
            print(response)
        
        Results::
            
            200

        """
        _url = f"{self.PINATA_BASE_URL}{self.HASH_PIN_POLICY}"
        headers = self.headers()
        body = {
                "ipfsPinHash": ipfs_pin_hash,
                "newPinPolicy": new_pin_policy
            }
        
        response = requests.put(
                        _url,
                        json=body,
                        headers=headers
                    )
        
        return response.status_code if response.status_code == 200 else {"error": response.status_code, "reason": response.reason, "text": response.text}
    

    def global_pin_policy(self, new_pin_policy: Dict[str, Any], migrate_previous_pins: bool=True) -> PinataResponse:
        """See (https://docs.pinata.cloud/api-pinning/global-pin-policy).

        Args:
            new_pin_policy (Dict[str, Any]): The new pin policy that you want to apply.

            migrate_previous_pins (bool, optional): Migrating your previous pins means that all of your existing content on Pinata
            will be replicated to match your new pin policy. Defaults to True.

        Returns:
            PinataResponse: See utils.custom_typing.py file.
        
        Example::
            
            from pinata_python.pinning import Pinning

            pinata = Pinning(AUTH="jwt", PINATA_JWT_TOKEN='<YOUR-JWT>')

            new_pin_policy = {
                                'regions': [
                                    {
                                        'id': 'FRA1',
                                        'desiredReplicationCount': 1
                                    }
                                ]
                            }
            response = pinata.global_pin_policy(
                                new_pin_policy, 
                                migrate_previous_pins=True
                            )
            print(response)
        
        Results::
            
            200

        """
        _url = f"{self.PINATA_BASE_URL}{self.GLOBAL_PIN_POLICY}"
        headers = self.headers()
        body = {
                "newPinPolicy": new_pin_policy,
                "migratePreviousPins": migrate_previous_pins
            }

        response = requests.put(
                        _url,
                        json=body,
                        headers=headers
                    )
        
        return response.status_code if response.status_code == 200 else {"error": response.status_code, "reason": response.reason, "text": response.text}

    
    def pin_jobs(self, options: Options=None) -> PinataResponse:
        """See (https://docs.pinata.cloud/api-pinning/pin-jobs).

        Args:
            options (Options, optional): The dictionary with the available filters as keywords. Defaults to None.

        Returns:
            PinataResponse: See utils.custom_typing.py file.
        
        Example::
            
            from pinata_python.pinning import Pinning

            pinata = Pinning(AUTH="jwt", PINATA_JWT_TOKEN='<YOUR-JWT>')

            options = {
                        'sort': 'ASC',
                        'status': 'prechecking',
                        'limit': 3
                    }
            response = pinata.pin_jobs(options)
            print(response) # it's empty
        
        Results::
            
            {
                'count': 0, 
                'rows': []
            }

        """
        _url = f"{self.PINATA_BASE_URL}{self.PIN_JOBS}"
        headers = self.headers()
        params = {}
        
        if options:
            if "sort" in options:
                params["sort"] = options["sort"]
            
            if "status" in options:
                params["status"] = options["status"]
            
            if "ipfs_pin_hash" in options:
                params["ipfs_pin_hash"] = options["ipfs_pin_hash"]
            
            if "limit" in options:
                params["limit"] = options["limit"]
            
            if "offset" in options:
                params["offset"] = options["offset"]
        
        response = requests.get(
                        _url,
                        params=params,
                        headers=headers
                    )
        
        return response.json() if response.status_code == 200 else {"error": response.status_code, "reason": response.reason, "text": response.text}