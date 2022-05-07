Problem description: https://practice.geeksforgeeks.org/problems/value-equal-to-index-value1330/1/?page=1&difficulty[]=-2&category[]=Arrays&category[]=Strings&sortBy=submissions#
Time Complexity: o(n)
Space Complexity: o(n)

def valueEqualToIndex(self,arr, n):
		# code here
		ans=[]
		for i in range(n):
		    if i+1==arr[i]:
		        ans.append(arr[i])
		return ans
		    
