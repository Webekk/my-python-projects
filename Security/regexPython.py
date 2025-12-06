import re

sample_text = "email@example.com,email@example.com,email@subdomain.example.com,firstname+lastname@example.com,email@123.123.123.123,email@[123.123.123.123],\"email\"@example.com"


#               username           @     mail       .   com or whatever (require unleast 2 letters)
email_pattern = r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9_.+-]+\.[a-zA-Z]{2,}"
new_words_with_mails = "Contact us at support@example.com or sales@example.org"
emails = re.findall(email_pattern, sample_text)
print(emails)