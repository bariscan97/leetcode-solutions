class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        l2r = sorted([(p, h, d, idx) for idx, (p, h, d) in enumerate(zip(positions, healths, directions))])
        st = []
        for p, h, d, idx in l2r:
            if d == 'R':
                st.append( (idx, h, d) )
            else:
                while st and st[-1][2] == 'R' and d == 'L':
                    last_idx, last_h, last_d = st.pop()
                    if last_h > h:
                        idx, h, d = last_idx, last_h -1, 'R'
                    elif last_h < h:
                        h, d = h - 1, 'L'
                    else:
                        d = '#'                        
                if d != '#':
                    st.append((idx, h, d))

        st.sort()
        return [tmp[1] for tmp in st]
        