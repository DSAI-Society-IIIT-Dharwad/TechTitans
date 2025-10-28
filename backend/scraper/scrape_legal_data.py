"""
Web Scraper for Legal Data from Kaanoon.com
Extracts legal content, case details, and relevant information
"""

import requests
from bs4 import BeautifulSoup
import json
import time
from typing import Dict, List
import re
from pathlib import Path


class LegalDataScraper:
    """Scraper for legal documents and case information"""
    
    def __init__(self):
        self.base_url = "https://www.kaanoon.com"
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        self.session = requests.Session()
        self.session.headers.update(self.headers)
    
    def scrape_page(self, url: str) -> Dict:
        """
        Scrape a single legal page
        
        Args:
            url: URL to scrape
            
        Returns:
            Dictionary containing scraped data
        """
        try:
            print(f"Scraping: {url}")
            response = self.session.get(url, timeout=10)
            response.raise_for_status()
            
            soup = BeautifulSoup(response.content, 'lxml')
            
            # Extract title
            title = self.extract_title(soup)
            
            # Extract main content
            content = self.extract_content(soup)
            
            # Extract metadata
            metadata = self.extract_metadata(soup)
            
            # Extract questions and answers
            qa_pairs = self.extract_qa_pairs(soup)
            
            data = {
                'url': url,
                'title': title,
                'content': content,
                'metadata': metadata,
                'qa_pairs': qa_pairs,
                'scraped_at': time.strftime('%Y-%m-%d %H:%M:%S')
            }
            
            return data
            
        except Exception as e:
            print(f"Error scraping {url}: {str(e)}")
            return None
    
    def extract_title(self, soup: BeautifulSoup) -> str:
        """Extract page title"""
        # Try multiple selectors
        title_selectors = [
            ('h1', {}),
            ('title', {}),
            ('h2', {'class': 'entry-title'}),
        ]
        
        for tag, attrs in title_selectors:
            element = soup.find(tag, attrs)
            if element:
                return element.get_text(strip=True)
        
        return "Legal Document"
    
    def extract_content(self, soup: BeautifulSoup) -> str:
        """Extract main content from the page"""
        content_parts = []
        
        # Look for main content areas
        content_selectors = [
            {'class': 'entry-content'},
            {'class': 'post-content'},
            {'class': 'article-content'},
            {'id': 'content'},
            {'class': 'main-content'},
        ]
        
        for selector in content_selectors:
            content_div = soup.find('div', selector)
            if content_div:
                # Extract paragraphs
                paragraphs = content_div.find_all(['p', 'div', 'li'])
                for p in paragraphs:
                    text = p.get_text(strip=True)
                    if text and len(text) > 20:  # Filter out short snippets
                        content_parts.append(text)
                break
        
        # If no content found, try to extract all meaningful text
        if not content_parts:
            for tag in soup.find_all(['p', 'h2', 'h3', 'h4', 'li']):
                text = tag.get_text(strip=True)
                if text and len(text) > 20:
                    content_parts.append(text)
        
        return '\n\n'.join(content_parts)
    
    def extract_metadata(self, soup: BeautifulSoup) -> Dict:
        """Extract metadata from the page"""
        metadata = {}
        
        # Extract meta tags
        meta_tags = soup.find_all('meta')
        for tag in meta_tags:
            if tag.get('name') == 'description':
                metadata['description'] = tag.get('content', '')
            elif tag.get('name') == 'keywords':
                metadata['keywords'] = tag.get('content', '')
        
        # Extract categories/tags
        categories = []
        for cat in soup.find_all(['a'], class_=re.compile(r'(category|tag)')):
            categories.append(cat.get_text(strip=True))
        
        if categories:
            metadata['categories'] = categories
        
        return metadata
    
    def extract_qa_pairs(self, soup: BeautifulSoup) -> List[Dict]:
        """Extract question-answer pairs if available"""
        qa_pairs = []
        
        # Look for FAQ sections
        faq_section = soup.find(['div', 'section'], class_=re.compile(r'(faq|question)', re.I))
        
        if faq_section:
            questions = faq_section.find_all(['h3', 'h4', 'strong'])
            for q in questions:
                question_text = q.get_text(strip=True)
                # Find the answer (next sibling)
                answer_elem = q.find_next(['p', 'div'])
                answer_text = answer_elem.get_text(strip=True) if answer_elem else ""
                
                if question_text and answer_text:
                    qa_pairs.append({
                        'question': question_text,
                        'answer': answer_text
                    })
        
        return qa_pairs
    
    def scrape_multiple_urls(self, urls: List[str]) -> List[Dict]:
        """
        Scrape multiple URLs
        
        Args:
            urls: List of URLs to scrape
            
        Returns:
            List of scraped data dictionaries
        """
        all_data = []
        
        for url in urls:
            data = self.scrape_page(url)
            if data:
                all_data.append(data)
            time.sleep(1)  # Be polite to the server
        
        return all_data
    
    def save_to_json(self, data: List[Dict], filepath: str):
        """Save scraped data to JSON file"""
        Path(filepath).parent.mkdir(parents=True, exist_ok=True)
        
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        
        print(f"Data saved to {filepath}")
    
    def save_to_text(self, data: List[Dict], filepath: str):
        """Save scraped data to plain text file for easy reading"""
        Path(filepath).parent.mkdir(parents=True, exist_ok=True)
        
        with open(filepath, 'w', encoding='utf-8') as f:
            for item in data:
                f.write(f"{'='*80}\n")
                f.write(f"TITLE: {item.get('title', 'N/A')}\n")
                f.write(f"URL: {item.get('url', 'N/A')}\n")
                f.write(f"{'='*80}\n\n")
                f.write(f"{item.get('content', '')}\n\n")
                
                if item.get('qa_pairs'):
                    f.write(f"\n{'='*80}\n")
                    f.write("QUESTIONS & ANSWERS:\n")
                    f.write(f"{'='*80}\n\n")
                    for qa in item['qa_pairs']:
                        f.write(f"Q: {qa['question']}\n")
                        f.write(f"A: {qa['answer']}\n\n")
                
                f.write(f"\n\n")
        
        print(f"Text data saved to {filepath}")


def main():
    """Main scraping function"""
    scraper = LegalDataScraper()
    
    # Comprehensive list of Indian legal topics
    urls = [
        # Property & Inheritance
        "https://www.kaanoon.com/494607/house-registration-after-parents-demise",
        "https://www.kaanoon.com/indian-law/property-inheritance-laws",
        "https://www.kaanoon.com/succession-certificate",
        
        # Criminal Law
        "https://www.kaanoon.com/498a-ipc",
        "https://www.kaanoon.com/section-420-ipc",
        "https://www.kaanoon.com/section-323-ipc",
        
        # Family Law
        "https://www.kaanoon.com/divorce-laws-india",
        "https://www.kaanoon.com/child-custody-laws",
        "https://www.kaanoon.com/marriage-registration",
        
        # Consumer Rights
        "https://www.kaanoon.com/consumer-protection-act",
        "https://www.kaanoon.com/consumer-complaint",
        
        # Employment Law
        "https://www.kaanoon.com/labour-laws-india",
        "https://www.kaanoon.com/employee-rights",
        
        # Constitution
        "https://www.kaanoon.com/fundamental-rights",
        "https://www.kaanoon.com/fundamental-duties",
        "https://www.kaanoon.com/directive-principles",
    ]
    
    # You can add more legal URLs here for a richer knowledge base
    additional_urls = [
        # Add more URLs as needed
    ]
    
    all_urls = urls + additional_urls
    
    print("Starting legal data scraping...")
    print(f"Scraping {len(all_urls)} URL(s)...\n")
    
    # Scrape all URLs
    scraped_data = scraper.scrape_multiple_urls(all_urls)
    
    if scraped_data:
        # Save to JSON
        scraper.save_to_json(scraped_data, 'data/raw/legal_data.json')
        
        # Save to text for easy reading
        scraper.save_to_text(scraped_data, 'data/raw/legal_data.txt')
        
        print(f"\nSuccessfully scraped {len(scraped_data)} page(s)")
        print(f"Data saved in 'data/raw/' directory")
    else:
        print("\n❌ No data was scraped")


if __name__ == "__main__":
    main()

