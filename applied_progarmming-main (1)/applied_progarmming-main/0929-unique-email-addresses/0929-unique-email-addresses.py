class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        unique_email = set()

        for email in emails:
            local, domain = email.split("@")

            if '+' in local: 
                local = local[:local.index('+')]    

            local = local.replace('.', '')

            valid_email = local + '@' + domain

            unique_email.add(valid_email)

        return len(unique_email)    