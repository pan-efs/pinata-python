from dataclasses import dataclass
from typing import ClassVar

from .exceptions.exceptions import AuthenticationError, SetAuthenticationError
from .utils.custom_typing import Headers, Options
from .urls.prefixs import (
    __PINATA_IPFS_GATEWAY__,
    __PINATA_BASE_URL__, 
    __GENERATE_API_KEYS__, 
    __REVOKE_API_KEY__, 
    __PIN_FILE_TO_IPFS__,
    __PIN_JSON_TO_IPFS__,
    __PIN_BY_HASH__,
    __HASH_METADATA__,
    __HASH_PIN_POLICY__,
    __GLOBAL_PIN_POLICY__, 
    __UNPIN__,
    __PIN_JOBS__,
    __QUERY_PINS__,
    __DATA_USAGE__
) 


@dataclass
class Pinata:
    """Pinata Base class.
       
        Attributes:
        
            PINATA_API_KEY (str, Optional): Pinata's api_key.

            PINATA_API_SECRET (str, Optional): Pinata's api_secret.

            PINATA_JWT_TOKEN (str, Optional): Pinata's JWT token.

            AUTH (str, Optional): Authentication method. Default to 'keysecret'. Otherwise, 'jwt'.
        
        Example::
            
            from pinata_python.base import Pinata
            
            # keysecret
            pinata = Pinata(
                            PINATA_API_KEY='<YOUR-API-KEY>', 
                            PINATA_API_SECRET='<YOUR-API-SECRET>'
                        )

            # jwt
            pinata = Pinata(AUTH="jwt", PINATA_JWT_TOKEN='<YOUR-JWT>')

    """

    PINATA_API_KEY: str = None
    PINATA_API_SECRET: str = None
    PINATA_JWT_TOKEN: str = None
    AUTH: str = 'keysecret'

    PINATA_IPFS_GATEWAY: ClassVar[str] = __PINATA_IPFS_GATEWAY__
    PINATA_BASE_URL: ClassVar[str] = __PINATA_BASE_URL__
    GENERATE_API_KEYS: ClassVar[str] = __GENERATE_API_KEYS__
    REVOKE_API_KEY: ClassVar[str] = __REVOKE_API_KEY__
    PIN_FILE_TO_IPFS: ClassVar[str] = __PIN_FILE_TO_IPFS__
    PIN_JSON_TO_IPFS: ClassVar[str] = __PIN_JSON_TO_IPFS__
    PIN_BY_HASH: ClassVar[str] = __PIN_BY_HASH__
    HASH_METADATA: ClassVar[str] = __HASH_METADATA__
    HASH_PIN_POLICY: ClassVar[str] = __HASH_PIN_POLICY__
    GLOBAL_PIN_POLICY: ClassVar[str] = __GLOBAL_PIN_POLICY__
    UNPIN: ClassVar[str] = __UNPIN__
    PIN_JOBS: ClassVar[str] = __PIN_JOBS__
    QUERY_PINS: ClassVar[str] = __QUERY_PINS__
    DATA_USAGE: ClassVar[str] = __DATA_USAGE__

    
    def headers(self) -> Headers:
        """Get request's headers.

        Raises:
            AuthenticationError: If api_key or api_secret have not been provided.

            AuthenticationError: If JWT token has not been provided.
            
            AuthenticationError: No authentication way has been declared.

        Returns:
            Headers: The authentication headers.
        """
        if self.AUTH=='keysecret':
            if self.PINATA_API_KEY and self.PINATA_API_SECRET:
                return {
                    'pinata_api_key': self.PINATA_API_KEY,
                    'pinata_secret_api_key': self.PINATA_API_SECRET
                }
            else:
                raise AuthenticationError(msg='Authentication api_key/api_secret are not provided.')

        elif self.AUTH=='jwt':
            if self.PINATA_JWT_TOKEN:
                return {
                    'Authorization': f'Bearer {self.PINATA_JWT_TOKEN}'
                }
            
            else:
                raise AuthenticationError(msg='Authenication jwt_token is not provided.')

        else:
            raise AuthenticationError()
    

    def set_authentication(self, options: Options=None) -> bool:
        """Set new authentication credentials.

        Args:
            options (Options, optional): The dictionary with keywords 'jwt_token' or
            ('api_key' and 'api_secret'). Defaults to None.

        Raises:
            SetAuthenticationError: If both authentication methods has been defined in the dictionary.

        Returns:
            bool: True. Otherwise, False.
        
        Example::
            
            from pinata_python.base import Pinata

            pinata = Pinata(
                            PINATA_API_KEY='<YOUR-API-KEY>', 
                            PINATA_API_SECRET='<YOUR-API-SECRET>'
                        )
            # OR pinata = Pinata(AUTH="jwt", PINATA_JWT_TOKEN='<YOUR-JWT>')

            options = {'jwt_token': '<YOUR-NEW-JWT>'}
            # OR options = {'api_key': '<YOUR-NEW-API-KEY>', 'api_secret': '<YOUR-NEW-API-SECRET>'

            response = pinata.set_authentication(options=options)
            print(response)
        
        Results::
            
            True

        """
        if options:
            if "jwt_token" in options and "api_key" in options and "api_secret" in options:
                raise SetAuthenticationError(msg='Choose one authentication method. JWT or KEY-SECRET.')

            if "jwt_token" in options:
                self.PINATA_JWT_TOKEN = options["jwt_token"]
                self.AUTH = "jwt"
                return True
            
            if "api_key" in options and "api_secret" in options:
                self.PINATA_API_KEY = options["api_key"]
                self.PINATA_API_SECRET = options["api_secret"]
                self.AUTH = "keysecret"
                return True
        
        return False
        