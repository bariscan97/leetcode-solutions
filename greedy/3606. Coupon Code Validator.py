_pattern = re.compile(r'^[A-Za-z0-9_]*$')

def ok(s: str) -> bool:
    return bool(_pattern.fullmatch(s))

class Solution:
    def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:
        category = ["electronics", "grocery", "pharmacy", "restaurant"]
        code = [[code[i], businessLine[i]]  for i in range(len(code)) if code[i] and ok(code[i]) and isActive[i] and businessLine[i] in category]
        code = sorted(code,  key = lambda x:[category.index(x[1]), x[0]])
        return [i for i,_ in code]