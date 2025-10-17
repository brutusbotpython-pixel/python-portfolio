"""Excel Automation Tool"""

import pandas as pd
import logging
from datetime import datetime

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class ExcelAutomation:
    """Excel automation tool"""
    
    def __init__(self):
        logger.info("Excel Automation initialized")
    
    def create_report(self, data, filename: str):
        df = pd.DataFrame(data)
        df.to_excel(filename, index=False)
        logger.info(f"Report created: {filename}")
    
    def generate_demo(self):
        data = [
            {'Product': 'Laptop', 'Qty': 5, 'Price': 999},
            {'Product': 'Mouse', 'Qty': 10, 'Price': 29},
            {'Product': 'Keyboard', 'Qty': 8, 'Price': 79}
        ]
        return pd.DataFrame(data)

def demo():
    logger.info("Running demo...")
    tool = ExcelAutomation()
    df = tool.generate_demo()
    tool.create_report(df, "demo_report.xlsx")
    logger.info("Demo completed")

if __name__ == "__main__":
    demo()
```

---

