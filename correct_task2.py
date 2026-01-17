# Write your corrected implementation for Task 2 here.
# Do not modify `task2.py`.

def count_valid_emails(emails):
    """Count valid email addresses in a list.

    Rules:
    - `emails` must be a list; otherwise raise TypeError.
    - Ignore non-string entries (e.g., None, numbers, dicts).
    - Use a conservative regex to validate common email formats:
      local-part@[domain].[tld] (allows subdomains and '+' tagging).
    - Returns an integer count of entries that match the pattern.
    """
    if not isinstance(emails, list):
        raise TypeError("emails must be a list")

    import re
    # Basic, practical email regex (not fully RFC 5322 compliant) that covers common cases
    pattern = re.compile(r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$')

    count = 0
    for e in emails:
        if not isinstance(e, str):
            continue
        e = e.strip()
        if pattern.match(e):
            count += 1

    return count
