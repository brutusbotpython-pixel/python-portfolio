"""E-commerce Product Scraper"""

import pandas as pd
import logging
from datetime import datetime
from typing import Dict
import json

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class EcommerceScraper:
    """Professional web scraper"""
    
    def __init__(self, base_url: str):
        self.base_url = base_url
        self.products = []
    
    def export_to_csv(self, filename: str = 'products.csv'):
        if self.products:
            pd.DataFrame(self.products).to_csv(filename, index=False)
            logger.info(f"Exported to {filename}")
    
    def export_to_json(self, filename: str = 'products.json'):
        if self.products:
            with open(filename, 'w') as f:
                json.dump(self.products, f, indent=2)
            logger.info(f"Exported to {filename}")
    
    def export_to_excel(self, filename: str = 'products.xlsx'):
        if self.products:
            pd.DataFrame(self.products).to_excel(filename, index=False)
            logger.info(f"Exported to {filename}")
    
    def get_statistics(self) -> Dict:
        if not self.products:
            return {}
        df = pd.DataFrame(self.products)
        return {
            'total': len(self.products),
            'avg_price': df['price'].mean(),
            'min_price': df['price'].min(),
            'max_price': df['price'].max()
        }

def demo():
    logger.info("Running demo...")
    scraper = EcommerceScraper("https://example.com")
    scraper.products = [
        {'title': 'Laptop', 'price': 899, 'rating': 4.5},
        {'title': 'Mouse', 'price': 29, 'rating': 4.2},
        {'title': 'Keyboard', 'price': 79, 'rating': 4.7}
    ]
    scraper.export_to_csv('demo.csv')
    scraper.export_to_json('demo.json')
    print(scraper.get_statistics())

if __name__ == "__main__":
    demo()
