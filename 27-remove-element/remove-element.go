func removeElement(nums []int, val int) int {
    start, end := 0, len(nums) - 1
    for start <= end {
        if nums[start] != val { 
            start += 1
        } else {
            nums[start], nums[end] = nums[end], nums[start]
            end -= 1
        }
    }
    return start
}