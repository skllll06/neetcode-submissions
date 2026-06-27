class Solution:

    def encode(self, strs: List[str]) -> str:
        body = ''.join(strs)
        lengths = ','.join(str(len(s)) for s in strs)
        return f'{body}|{len(lengths)}|{lengths}'

    def decode(self, s: str) -> List[str]:
        last_pipe = s.rfind('|')
        lengths_str = s[last_pipe+1:]
        second_pipe = s.rfind('|', 0, last_pipe)
        lengths = [int(x) for x in lengths_str.split(',')] if lengths_str else []
        res, i = [], 0
        for l in lengths:
            res.append(s[i:i+l])
            i += l
        return res