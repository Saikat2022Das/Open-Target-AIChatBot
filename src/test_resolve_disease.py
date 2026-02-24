#!/usr/bin/env python3

import requests
import json

# Disease name to search
disease_name = "breast cancer"

# GraphQL query for disease search
query_string = """
query searchDisease($queryString: String!) {
  search(queryString: $queryString, entityNames: ["disease"]) {
    hits {
      id
      name
      entity
    }
  }
}
"""

# Variables
variables = {"queryString": disease_name}

# Open Targets GraphQL endpoint
base_url = "https://api.platform.opentargets.org/api/v4/graphql"

# Perform POST request
r = requests.post(base_url, json={"query": query_string, "variables": variables})

print("Status Code:", r.status_code)

# Convert response to dict
api_response = r.json()

# Pretty print full response
print(json.dumps(api_response, indent=2))

# Extract EFO / MONDO ID safely
try:
    hits = api_response["data"]["search"]["hits"]
    
    if hits:
        top_hit = hits[0]
        disease_id = top_hit["id"]
        disease_label = top_hit["name"]
        
        print("\nResolved Disease:")
        print("Name:", disease_label)
        print("ID:", disease_id)
    else:
        print("No disease found.")

except Exception as e:
    print("Error parsing response:", e)