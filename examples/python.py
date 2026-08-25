#!/usr/bin/env python3
"""Scan a website using the EUComply Scanner REST API."""

import urllib.request
import urllib.parse
import json
import sys

def scan(url):
    api_base = "https://eucomply-scan.mahope-eeb.workers.dev"
    params = urllib.parse.urlencode({"url": url})
    req = urllib.request.Request(f"{api_base}/scan?{params}")
    
    with urllib.request.urlopen(req) as resp:
        return json.loads(resp.read())

if __name__ == "__main__":
    target = sys.argv[1] if len(sys.argv) > 1 else "https://example.com"
    report = scan(target)
    
    print(f"\n🔍 EUComply Scan: {report['url']}")
    print(f"   Score: {report['score']['passed']}/{report['score']['total']} ({report['score']['pct']}%)")
    print(f"   Platform: {report['platform']}\n")
    
    for name, check in report['checks'].items():
        icon = "✅" if check.get('pass') else "⚠️" if check.get('warn') else "❌"
        print(f" {icon} {check['label']}")
    
    print(f"\n{report['disclaimer']}")