class Solution(object):
    def constructRectangle(self, area):
        """
        :type area: int
        :rtype: List[int]
        """
        sqr=int(sqrt(area))
        while area%sqr!=0:
            sqr=sqr-1
        return int(area/sqr), sqr