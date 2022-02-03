# NICV
- National Identity Card Validator and Information Exetractor

## Supported NICs
- [x] NIC of Sri Lanka (LK) 🇱🇰

## Usage
```python
from nicv import LK_NIC

my_nic = LK_NIC("123456789v")

print(my_nic.dob()) # output: {'year': '1912', 'month': 'december', 'day': 10}
print(my_nic.gender) # output: male

```