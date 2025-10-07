class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        res = []
        lake = {}
        dryDays = []
        for rain in rains:
            if rain in lake:
                if len(dryDays) > 0 and (lake[rain] < dryDays[0] or lake[rain] < dryDays[-1]):
                    l = 0
                    r = len(dryDays)
                    while l <= r:
                        mid = (l + r) // 2
                        if dryDays[mid] > lake[rain]:
                            r = mid - 1
                        else:
                            l = mid + 1
                    ind = dryDays.pop(l)
                    res[ind] = rain
                    lake[rain] = len(res)
                    res.append(-1)
                else:
                    return []
            elif rain > 0:
                lake[rain] = len(res)
                res.append(-1)
            else:
                dryDays.append(len(res))
                res.append(1)
        return res