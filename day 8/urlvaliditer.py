import re

def is_valid_url(url):
    
    pattern = r'^(https?|ftp)://[^\s/$.?#].[^\s]*$'

    if re.match(pattern, url):
        return True
    else:
        return False

def main():
    url = input("Enter a URL: ")
    
    if is_valid_url(url):
        print("Valid URL!")
    else:
        print("Invalid URL.")

if __name__ == "__main__":
    main()
