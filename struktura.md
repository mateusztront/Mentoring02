1. Domain driven
2. Components driven

FastAPI:

I.
app/
- auth/
  -- models/ (ORM)
    - users.py
  -- routes/
    - login.py
  -- schemas (pydantic)
    - 
  -- utils/
   
- crud/
  - models/ (ORM)
    - users.py
  -- routes/
    - login.py
  -- schemas (pydantic)
    - 
  -- utils/
- admin/
- main.py (runnable)


II.
- models/
  - auth.py
  - admin.py 
  - crud.py
- routes/
- schemas/
main.py


Hasła:
- Depends() i dependency injection
- background tasks
- struktura bardziej złozonego routera (widoku) 
- integracja z ORM
- workery i asynchronicznosc
- testy