# Admin Endpoints Guide

This guide provides an overview of the administrative endpoints available in the application, including their routes, methods, and expected payloads.

## Endpoint List

1. **GET /admin/users**
   - Description: Retrieves a list of all users.
   - Authentication: Required

2. **POST /admin/toggle**
   - Description: Toggles a specific feature for administrative purposes.
   - Authentication: Required

3. **DELETE /admin/user/:id**
   - Description: Deletes a user by ID.
   - Authentication: Required

## Usage Example

Below are examples of how to utilize some of the admin endpoints:

```bash
curl -X GET \  
  http://example.com/admin/users \  
  -H 'Authorization: Bearer YOUR_TOKEN_HERE'

curl -X POST \  
  http://example.com/admin/toggle \  
  -H 'Authorization: Bearer YOUR_TOKEN_HERE' \  
  -d '{"feature":"dark_mode"}'
```

## Error Handling

Responses will include an HTTP status code indicating the result of the request, i.e., 200 for successful operations, 401 for unauthorized access, etc.
