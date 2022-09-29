class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        final_output = {}
        for i in emails:
            domain = i.split("@")[-1]
            if "+" in i:
                i =  i.split("+")[0] + "@" + domain
            if "." in i:
                i =  i.replace(".", "") + "@" + domain
            final_output[i] = 1
        return len(final_output)
