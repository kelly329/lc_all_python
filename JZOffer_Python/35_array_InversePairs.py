class Solution:
	def InversePairs(self, data):
		if not data:
			return 0
		copy = [i for i in data]
		return self.InversePairsCore(data, copy, 0, len(data) - 1) 	% 100000007	
	def InversePairsCore(self, copy, data, start, end):
		if(start >= end):
			copy[start] == data[start]
			return 0
		
		mid = (end + start) // 2
		left = self.InversePairsCore(data, copy, start, mid)
		right = self.InversePairsCore(data, copy, mid + 1, end)
		
		count = 0
		p1 = start
		p2 = mid + 1
		indexCopy = start
		while p1 <= mid and p2 <= end:
			if data[p1] <= data[p2]:
				copy[indexCopy] = data[p1]
				p1 += 1
			else:
				copy[indexCopy] = data[p2]
				count += mid - p1 + 1
				p2 += 1
			indexCopy += 1
		
		while p1 <= mid:
			copy[indexCopy] = data[p1]
			indexCopy += 1
			p1 += 1
		
		while p2 <= end:
			copy[indexCopy] = data[p2]
			indexCopy += 1
			p2 += 1
		return count + left + right
	
s = Solution()
print(s.InversePairs([364,637,341,406,747,995,234,971,571,219,993,407,416,366,315,301,601,650,418,355,460,505,360,965,516,648,727,667,465,849,455,181,486,149,588,233,144,174,557,67,746,550,474,162,268,142,463,221,882,576,604,739,288,569,256,936,275,401,497,82,935,983,583,523,697,478,147,795,380,973,958,115,773,870,259,655,446,863,735,784,3,671,433,630,425,930,64,266,235,187,284,665,874,80,45,848,38,811,267,575]))




		
	    
	
	
	