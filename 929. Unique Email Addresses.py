class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        forwarded_addr = set()
        for email in emails:
            names = email.split("@")
            parsed_dot = names[0].replace(".", "")
            parsed_local = parsed_dot.split("+")[0]
            forwarded_addr.add(parsed_local+"@"+names[1])
        return len(forwarded_addr)