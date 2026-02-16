import requests

def run(url):
    print(f"[Web] Scanning {url}")
    findings = []

    try:
        r = requests.get(url, timeout=5)

        if "X-Frame-Options" not in r.headers:
            findings.append("Missing X-Frame-Options")

        if "Content-Security-Policy" not in r.headers:
            findings.append("Missing CSP")

        if "sql" in r.text.lower():
            findings.append("Possible SQL error exposure")

    except Exception as e:
        findings.append(str(e))

    print(f"[Web] Findings: {findings}")
    return {"findings": findings}
