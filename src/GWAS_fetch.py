
import requests
import json

BASE_URL = "https://api.platform.opentargets.org/api/v4/graphql"

def fetch_gwas(disease_id: str, size: int = 10, index: int = 0):
    query = """
    query GWASStudiesQuery($diseaseIds: [String!]!, $size: Int!, $index: Int!) {
      studies(diseaseIds: $diseaseIds, page: { size: $size, index: $index }) {
        count
        rows {
          id
          projectId
          traitFromSource
          publicationFirstAuthor
          publicationDate
          publicationJournal
          nSamples
          pubmedId
        }
      }
    }
    """

    variables = {
        "diseaseIds": [disease_id],
        "size": size,
        "index": index
    }

    response = requests.post(
        BASE_URL,
        json={"query": query, "variables": variables}
    )

    return response.json()

print(json.dumps(fetch_gwas("MONDO_0007254"), indent=2))