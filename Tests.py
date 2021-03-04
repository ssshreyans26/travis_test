import pytest
from creditCardValidator import *



c=Card("4016870202644910", "06","21", "451")
 
def date():
  assert c.is_expired()==True
  
