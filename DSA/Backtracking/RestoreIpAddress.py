class Solution:
    def restoreIpAddresses(self, s: str) -> list[str]:
        result = []
        curr = []

        def isValid(value):
            return (len(value) == 1 or value[0] != '0') and int(value) <= 255

        def generateIP(ip):
            if len(curr) == 4:
                if ip == "":
                    result.append(".".join(curr[:]))
                return

            for i in range(len(ip)):
                s1 = ip[:i+1]
                if isValid(s1):
                    s2 = ip[i+1:]
                    curr.append(s1)
                    generateIP(s2)
                    curr.pop()
            
        generateIP(s)
        return result
