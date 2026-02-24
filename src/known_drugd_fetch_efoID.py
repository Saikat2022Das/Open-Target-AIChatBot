#!/usr/bin/env python3

import requests
import json

BASE_URL = "https://api.platform.opentargets.org/api/v4/graphql"

def fetch_known_drugs_limit(efo_id: str, limit: int = 10):
    query = """
    query KnownDrugsQuery(
      $efoId: String!
      $size: Int
    ) {
      disease(efoId: $efoId) {
        knownDrugs(size: $size) {
          rows {
            phase
            status
            drug {
              id
              name
            }
            target {
              approvedSymbol
            }
            drugType
            mechanismOfAction
          }
        }
      }
    }
    """

    variables = {
        "efoId": efo_id,
        "size": limit
    }

    response = requests.post(
        BASE_URL,
        json={"query": query, "variables": variables}
    )

    if response.status_code != 200:
        raise Exception(f"Query failed: {response.text}")

    data = response.json()

    rows = data["data"]["disease"]["knownDrugs"]["rows"]

    return rows


if __name__ == "__main__":
    efo_id = "MONDO_0007254"
    drugs = fetch_known_drugs_limit(efo_id, limit=10)

    print(f"Retrieved {len(drugs)} drugs")
    print(json.dumps(drugs, indent=2))