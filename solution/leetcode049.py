from typing import List, Dict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sort_strs = ["".join(sorted(str)) for str in strs]
        group_index_dict:Dict[str, List[int]] = dict()
        for i, sort_str in enumerate(sort_strs):
            if group_index_dict.get(sort_str, None) is None:
                group_index_dict[sort_str] = [i]
            else:
                group_index_dict[sort_str].append(i)
        ans = []
        for index_lt in group_index_dict.values():
            ans.append([strs[index] for index in index_lt])
        return ans
        

Solution().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])