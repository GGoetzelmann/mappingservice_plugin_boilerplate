#Mapping service is reachable before starting with plugin
GET {{host}}
HTTP 200

GET {{host}}/api/v1/mappingAdministration/types
HTTP 200
[Captures]
mappingType: jsonpath "$[0].id"

#Register with a very small portion of real mapping file info as dummy mapping file
POST {{host}}/api/v1/mappingAdministration/
Content-Type: multipart/form-data; boundary=boundary
[Options] #set all variables you need for further use in this hurl script
variable: id1=0
```
--boundary
Content-Disposition: form-data; name="record"; filename="blob"
Content-Type: application/csv

{"mappingId":"{{id1}}","mappingType": "{{mappingType}}","title":"Boilerplate from CI test","description":"","acl":[]}
--boundary
Content-Disposition: form-data; name="document"; filename="blob"
Content-Type: application/json

{"color_mapping": {"255,0,0": "0,255,0"}}
--boundary--
```
HTTP 201

#Execute Mapping with Thermofisher sample
POST {{host}}/api/v1/mappingExecution/{{id1}}
[MultipartFormData]
document: file,./sample/8bit_vs_16_bit.png;
HTTP 200

#Get registered plugin etag
GET {{host}}/api/v1/mappingAdministration/{{id1}}
HTTP 200
[Captures]
etag: header "ETag"

#Delete registered plugin
DELETE {{host}}/api/v1/mappingAdministration/{{id1}}
If-Match: {{etag}}
HTTP 204
