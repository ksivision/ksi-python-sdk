
#docker image rm openapitools/openapi-generator-online
# Start container at port 8888 and save the container id
CID=$(docker run -d -p 8888:8080 openapitools/openapi-generator-online)

# allow for startup
sleep 15

# Get the IP of the running container
GEN_IP=$(docker inspect --format '{{.NetworkSettings.IPAddress}}'  $CID)

# Execute an HTTP request and store the download link
CODE=$(curl -X POST \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
-d '{"openAPIUrl": "http://192.168.76.100/api/openapi.json", "options": {"packageName": "ksi_client_sdk", "packageVersion":"2.0.1"}}' \
'http://localhost:8888/api/gen/clients/python' \
|  jq -r  '.code')

echo "http://localhost:8888/api/gen/download/${CODE}"

# Download the generated zip and redirect to a file
curl -X GET "http://localhost:8888/api/gen/download/${CODE}" \
-H "Accept: application/octet-stream" > result.zip

# Unzip the file
unzip result.zip

# Shutdown the swagger generator image
docker stop $CID && docker rm $CID