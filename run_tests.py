import unittest
import os
from extraction_engine import extract_inspection
from poller import Poller, STATUS_COMPLIANT, STATUS_VIOLATION, STATUS_WARNING

class TestExtraction(unittest.TestCase):
    def test_extract_compliant(self):
        html = """
        <html>
            <body>
                <h1>Burger Joint</h1>
                <p class="address">789 Pine Rd, Star City, IL 60601</p>
                Date: 2025-03-10
                <p>Grade: A</p>
                <ul>
                    <li>Non-Critical: Wall paint chipped</li>
                </ul>
            </body>
        </html>
        """
        report = extract_inspection(html)
        self.assertEqual(report["title"], "Burger Joint")
        self.assertEqual(report["grade"], "A")
        self.assertFalse(report["has_critical_violations"])
    
    def test_extract_critical(self):
        html = """
        <html><body><h1>Golden Dragon</h1><p class="address">123 Main St</p>
        Date: 2025-03-01<p>Grade: C</p>
        <ul><li>Critical: Food temperature abuse</li><li>Non-Critical: Floors not clean</li></ul>
        </body></html>
        """
        report = extract_inspection(html)
        self.assertTrue(report["has_critical_violations"])
        self.assertEqual(report["grade"], "C")
    
    def test_status_critical(self):
        poller = Poller(status_file="test_statuses.json")
        report = {"title":"Test","grade":"C","has_critical_violations":True}
        self.assertEqual(poller.determine_status(report), STATUS_VIOLATION)
    
    def test_status_warning(self):
        poller = Poller(status_file="test_statuses.json")
        report = {"title":"Test","grade":"B","has_critical_violations":False}
        self.assertEqual(poller.determine_status(report), STATUS_WARNING)
    
    def test_status_compliant(self):
        poller = Poller(status_file="test_statuses.json")
        report = {"title":"Test","grade":"A","has_critical_violations":False}
        self.assertEqual(poller.determine_status(report), STATUS_COMPLIANT)
    
    @classmethod
    def tearDownClass(cls):
        if os.path.exists("test_statuses.json"):
            os.remove("test_statuses.json")

if __name__ == "__main__":
    unittest.main()
