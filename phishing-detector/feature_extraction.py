# feature_extraction.py
# This module extracts features from a URL for ML classification

import re
import urllib.parse
import tldextract

# List of suspicious words commonly found in phishing URLs
SUSPICIOUS_WORDS = ['login', 'secure', 'verify', 'update', 'bank',
                    'account', 'password', 'confirm', 'paypal', 'signin']

def extract_features(url):
    """
    Extract numerical features from a given URL.
    Returns a dictionary of features.
    """
    features = {}

    # 1. URL Length — phishing URLs tend to be longer
    features['url_length'] = len(url)

    # 2. Number of dots — multiple dots can indicate subdomain abuse
    features['num_dots'] = url.count('.')

    # 3. Number of hyphens — hyphens are common in fake domains
    features['num_hyphens'] = url.count('-')

    # 4. Number of slashes — deep paths can be suspicious
    features['num_slashes'] = url.count('/')

    # 5. Presence of @ symbol — can redirect users to a different host
    features['has_at_symbol'] = 1 if '@' in url else 0

    # 6. Presence of HTTPS — legitimate sites usually use HTTPS
    features['has_https'] = 1 if url.lower().startswith('https') else 0

    # 7. Digit count — IPs or obfuscated domains contain many digits
    features['digit_count'] = sum(c.isdigit() for c in url)

    # 8. Suspicious words — check if any suspicious words appear in URL
    url_lower = url.lower()
    features['has_suspicious_words'] = 1 if any(word in url_lower for word in SUSPICIOUS_WORDS) else 0

    # 9. IP address usage — phishing often uses raw IP instead of domain
    features['has_ip_address'] = 1 if re.search(
        r'(\d{1,3}\.){3}\d{1,3}', url) else 0

    # 10. Domain length — very long domains are often fake
    try:
        extracted = tldextract.extract(url)
        domain = extracted.domain
        features['domain_length'] = len(domain) if domain else 0
    except Exception:
        features['domain_length'] = 0

    # 11. Number of special characters (%, =, ?, &)
    features['num_special_chars'] = sum(url.count(c) for c in ['%', '=', '?', '&'])

    # 12. URL has subdomain
    try:
        extracted = tldextract.extract(url)
        features['has_subdomain'] = 1 if extracted.subdomain else 0
    except Exception:
        features['has_subdomain'] = 0

    return features


def get_feature_names():
    """Returns the list of feature column names in order."""
    return [
        'url_length', 'num_dots', 'num_hyphens', 'num_slashes',
        'has_at_symbol', 'has_https', 'digit_count', 'has_suspicious_words',
        'has_ip_address', 'domain_length', 'num_special_chars', 'has_subdomain'
    ]
