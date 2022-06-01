from collections import Counter


def get_domain(email_address: str) -> str:
    """
    Return the domain of an email address.
    """
    return email_address.lower().split('@')[-1]


with open('emails.txt', 'r') as f:
    domain_counts = Counter(get_domain(line.strip()) for line in f for email in line.split() if '@' in line)

