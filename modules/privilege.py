import os

def run():
    print("[Privilege] Checking SUID files")
    suid_files = []

    for root, dirs, files in os.walk("/"):
        for file in files:
            path = os.path.join(root, file)
            try:
                if os.stat(path).st_mode & 0o4000:
                    suid_files.append(path)
            except:
                pass

    print(f"[Privilege] Found {len(suid_files)} SUID files")
    return {"suid_files": suid_files[:10]}
