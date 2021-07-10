class Solution:
	def lengthOfLongestSubstring(self, s: str) -> int:
		characters = set()
		left = right = ans = 0
		length = len(s)
		
		while right < length:
			if s[right] in characters:
				characters.remove(s[left])
				left += 1
			else:
				characters.add(s[right])
				right += 1
				ans = max(ans, right - left)
				#print(str(ans) + "\t" + s[left:right])
		
		return ans

sol= Solution()
print(sol.lengthOfLongestSubstring("abcalsjdlaksdahsdkjhasdkjhddiofvgskjdfg"))