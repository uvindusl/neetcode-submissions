class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        values = []
        tmp_values = []
        check_values = list(strs)
        for i in range(len(strs)):
            value1 = strs[i]
            if value1 in check_values:
                tmp_values = []
                tmp_values.append(value1)
                check_values.remove(value1)
                for j in range(i+1, len(strs)):
                    value2 = strs[j]
                    if value1 == value2:
                        tmp_values.append(value2)
                        check_values.remove(value1)
                    else:
                        countS, countT = {}, {}

                        if len(value1) == len(value2):
                            for x in range(len(value2)):
                                countS[value1[x]] = 1 + countS.get(value1[x], 0)
                                countT[value2[x]] = 1 + countT.get(value2[x], 0)

                            if countS == countT:
                                tmp_values.append(value2)
                                check_values.remove(value2)

                values.append(tmp_values)
                # tmp_values = []

        return values
