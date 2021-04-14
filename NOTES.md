# Notes for OD-Middleware

## service.process(query)
This function is imported and used to create the final result set.
Make sure that the service makes no internet or filesystem queries until and unless this function is run.