#!/usr/bin/env bash
# Scan a website via the public REST API
# Requires: curl

URL="${1:-https://example.com}"
API="https://eucomply-scan.mahope-eeb.workers.dev"

echo "🔍 Scanning: $URL"
echo ""

curl -s "${API}/scan?url=${URL}" | python3 -m json.tool 2>/dev/null || curl -s "${API}/scan?url=${URL}"

echo ""
echo "---"
echo "Stats: $(curl -s ${API}/stats)"