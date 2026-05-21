# generate_dataset.py
# Generates a sample phishing/legitimate URL dataset for training
# In a real project, replace this with a downloaded Kaggle dataset

import pandas as pd
import os

# Sample phishing URLs (label = 1)
phishing_urls = [
    "http://paypal-secure-login.com/verify/account",
    "http://192.168.1.1/login/bank/update",
    "http://secure-bank-update.tk/confirm?user=123&token=abc",
    "http://login-paypal.com/secure/verify",
    "http://amazon-security-update.net/account/login",
    "http://facebook-login-verify.tk/auth",
    "http://bankofamerica-secure.ml/update/password",
    "http://signin-google-verify.com/login?id=332",
    "http://secure.update-account.info/bank/login",
    "http://192.0.2.1/phishing/login/verify/account",
    "http://paypal-verify-account.co/secure",
    "http://ebay-login-secure.com/signin?confirm=1",
    "http://apple-id-verify-update.ml/account",
    "http://netflix-login-billing.com/verify/card",
    "http://chase-bank-login-secure.tk/update",
    "http://instagram-verify-account.com/login@secure",
    "http://microsoft-account-update.info/signin",
    "http://dropbox-secure-verify.com/password/reset",
    "http://twitter-account-verify.tk/login?secure=true",
    "http://linkedin-secure-login.ml/account/update",
    "http://10.0.0.1/bank/login/secure/verify",
    "http://secure-login-paypal-verify.com/update/now",
    "http://irs-refund-claim.tk/verify/tax",
    "http://fedex-track-delivery.info/login",
    "http://usps-delivery-verify.com/account?id=user1",
    "http://covid19-relief-fund.ml/apply/verify",
    "http://crypto-wallet-secure.tk/login",
    "http://amazon-prize-claim.co/verify/winner",
    "http://zoom-meeting-login.info/account/update",
    "http://whatsapp-verify-account.tk/login",
    "http://gmail-secure-verify.com/account/signin",
    "http://bank-account-verify-update.ml/secure",
    "http://steam-account-login-verify.tk/signin",
    "http://spotify-account-update.info/login?confirm=1",
    "http://support-apple-verify.com/id/login",
    "http://wellsfargo-secure-update.ml/account",
    "http://citibank-login-secure.tk/verify",
    "http://visa-card-update-verify.com/login",
    "http://2checkout-secure-pay.ml/verify/account",
    "http://usbank-online-verify.tk/signin?user=secure",
    "http://suntrust-login-secure.info/account/update",
    "http://regions-bank-verify.com/secure/login",
    "http://bb-t-secure-online.ml/account/verify",
    "http://td-bank-update-secure.tk/signin",
    "http://capitalone-account-verify.com/login",
    "http://barclays-secure-verify.ml/account/update",
    "http://hsbc-online-login-secure.tk/verify",
    "http://santander-account-verify.com/login/update",
    "http://rbc-secure-login-verify.info/account",
    "http://anz-bank-secure-update.ml/login/verify",
]

# Sample legitimate URLs (label = 0)
legitimate_urls = [
    "https://www.google.com",
    "https://www.facebook.com/home",
    "https://www.amazon.com/products",
    "https://www.github.com/user/repo",
    "https://www.stackoverflow.com/questions",
    "https://www.wikipedia.org/wiki/Python",
    "https://www.youtube.com/watch?v=abc123",
    "https://www.twitter.com/username",
    "https://www.linkedin.com/in/username",
    "https://www.microsoft.com/en-us",
    "https://www.apple.com/iphone",
    "https://www.netflix.com/browse",
    "https://www.reddit.com/r/python",
    "https://www.instagram.com/username",
    "https://www.dropbox.com/home",
    "https://www.paypal.com/home",
    "https://www.ebay.com/sch/i.html",
    "https://www.walmart.com/browse",
    "https://www.target.com/c/electronics",
    "https://www.nytimes.com/section/technology",
    "https://www.bbc.com/news",
    "https://www.cnn.com/tech",
    "https://www.coursera.org/courses",
    "https://www.udemy.com/courses",
    "https://www.medium.com/tag/python",
    "https://www.spotify.com/browse",
    "https://www.zoom.us/join",
    "https://www.slack.com/features",
    "https://www.notion.so/workspace",
    "https://www.trello.com/boards",
    "https://www.airbnb.com/rooms",
    "https://www.booking.com/hotels",
    "https://www.tripadvisor.com/Hotels",
    "https://www.yelp.com/search",
    "https://www.imdb.com/chart/top",
    "https://www.twitch.tv/directory",
    "https://www.discord.com/channels",
    "https://www.canva.com/design",
    "https://www.figma.com/files",
    "https://www.behance.net/gallery",
    "https://www.dribbble.com/shots",
    "https://www.shopify.com/store",
    "https://www.squarespace.com/templates",
    "https://www.wix.com/website",
    "https://www.wordpress.com/themes",
    "https://www.heroku.com/apps",
    "https://www.digitalocean.com/products",
    "https://www.cloudflare.com/products",
    "https://www.mongodb.com/atlas",
    "https://www.postgresql.org/docs",
]

def create_sample_dataset():
    """Creates and saves a sample dataset CSV file."""
    urls = phishing_urls + legitimate_urls
    labels = [1] * len(phishing_urls) + [0] * len(legitimate_urls)

    df = pd.DataFrame({'url': urls, 'label': labels})

    # Shuffle the dataset
    df = df.sample(frac=1, random_state=42).reset_index(drop=True)

    # Save to dataset folder
    os.makedirs('dataset', exist_ok=True)
    df.to_csv('dataset/urls.csv', index=False)
    df.to_csv('dataset/malicious_phish.csv', index=False)
    print(f"✅ Sample dataset created: dataset/urls.csv and dataset/malicious_phish.csv ({len(df)} rows)")
    return df


if __name__ == "__main__":
    create_sample_dataset()
