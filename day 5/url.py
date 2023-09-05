import hashlib

def shorten_url(long_url):
    
    md5_hash = hashlib.md5(long_url.encode()).hexdigest()
    
    
    prefix = "http://short.ly/"
    

    shortened_url = prefix + md5_hash[:6]
    
    return shortened_url

long_url = input("Enter a long URL: ")


shortened_url = shorten_url(long_url)

print("Shortened URL:", shortened_url)
