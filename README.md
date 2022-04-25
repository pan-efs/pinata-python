# pinata-python
[![AUR maintainer](https://img.shields.io/badge/Houba-Hej%2C%20Folks!-brightgreen)]()
![GitHub Workflow Status](https://img.shields.io/github/workflow/status/pan-efs/pinata-python/build)
[![Python 3.8](https://img.shields.io/badge/python-3.8-blue.svg)](https://www.python.org/downloads/release/python-380/)
![GitHub repo size](https://img.shields.io/github/repo-size/pan-efs/pinata-python)
![License](https://img.shields.io/github/license/pan-efs/pinata-python)

> An easy to use and fully-featured Python API for [pinata.cloud.](https://www.pinata.cloud/)

## Installation
Install via PyPi:

`pip install pinata-python==1.0.0`

Install from source:

`pip install git+https://github.com/pan-efs/pinata-python.git`

## Documentation
Read the [official documentation](https://github.com/pan-efs/pinata-python/blob/main/docs/_build/rinoh/pinata-python.pdf) as `PDF` file. Examples can be found as well.

<details>
  <summary>Build docs</summary>
  
<details>
  <summary>HTML</summary>
`~/pinata-python$ sphinx-build -b html docs/source/ docs/build/html`
</details>

<details>
  <summary>PDF</summary>
`~/pinata-python$ sphinx-build -b rinoh docs/source docs/_build/rinoh`
</details>

</details>

## Example

```python
from pinata_python.pinning import Pinning

your_pinata_api_key = ''
your_pinata_api_secret = ''

pinata = Pinning(
      PINATA_API_KEY=your_pinata_api_key,
      PINATA_API_SECRET=your_pinata_api_secret
    )
your_filepath = ''

response = pinata.pin_file_to_ipfs(filepath)

print(response)
```

## Unit Tests

`~/pinata-python$ bash run_tests.sh`

There are some tests which have been skipped. Please refer to [tests folder](https://github.com/pan-efs/pinata-python/tree/main/pinata_python/tests) in order to comprehend why.

> Note: The API has not tested for the professional plan. Yet, it doesn't mean that it doesn't work for it.

## Notes

* The pinata-python API is unofficial. There is no any kind of collaboration between the author and pinata.

* The pinata-python API has been developed for recreational and personal usage reasons. There is no any kind of financial interest.

* The pinata-python API is distributed under MIT licence.

## Contributing

1. For problems, you could kindly open an issue and label it with `bug`.

2. For ideas or improvements, you could kindly open an issue and label it with `enhancement`.

## Star it! :star:

You got it! Feel free to leave a star if you found the package useful or you learned something new at least.
