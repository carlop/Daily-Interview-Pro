def find_pythagorean_triplets(nums):
    nums2 = nums
    for num in nums:
        nums2 = nums2[1:]
        for num2 in nums2:
            current_triplet = ((num*num) + (num2*num2))
            for num3 in nums:
                if current_triplet == (num3*num3):
                    return True
    return False
