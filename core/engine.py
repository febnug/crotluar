from modules import recon, web, smb, lateral, privilege
from core.reporter import Reporter

class Engine:
    def __init__(self):
        self.reporter = Reporter()

    def run_recon(self, target):
        results = recon.run(target)
        self.reporter.add("Recon", results)

    def run_web(self, url):
        results = web.run(url)
        self.reporter.add("Web", results)

    def run_internal(self, target):
        results = smb.run(target)
        self.reporter.add("SMB", results)
        lateral.run(target)

    def run_privilege(self):
        results = privilege.run()
        self.reporter.add("Privilege", results)
