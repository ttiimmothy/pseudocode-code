package code

// Merge Sort
func MergeSort(nums []int, low int, high int) {
	if low < high {
		mid := low + (high-low)/2
		MergeSort(nums, low, mid)
		MergeSort(nums, mid+1, high)
		L := make([]int, mid-low+1)
		R := make([]int, high-mid)
		copy(L, nums[low:mid+1])
		copy(R, nums[mid+1:high+1])
		i, j := 0, 0
		k := low
		for i < len(L) && j < len(R) {
			if L[i] <= R[j] {
				nums[k] = L[i]
				i++
			} else {
				nums[k] = R[j]
				j++
			}
			k++
		}
		for i < len(L) {
			nums[k] = L[i]
			i++
			k++
		}
		for j < len(R) {
			nums[k] = R[j]
			j++
			k++
		}
	}
}

// Quick Sort, may cause time limit error
func QuickSort(nums []int, low int, high int) {
	if low < high {
		pivot := partition(nums, low, high)
		QuickSort(nums, low, pivot-1)
		QuickSort(nums, pivot+1, high)
	}
}

func partition(nums []int, low int, high int) int {
	start := low - 1
	pivot := nums[high]
	for i := low; i < high; i++ {
		if nums[i] < pivot {
			start++
			nums[start], nums[i] = nums[i], nums[start]
		}
	}
	nums[start+1], nums[high] = nums[high], nums[start+1]
	return start + 1
}

// Bubble Sort
func BubbleSort(nums []int) {
	n := len(nums)
	for i := 0; i < n-1; i++ {
		swapped := false
		for j := 0; j < n-i-1; j++ {
			if nums[j] > nums[j+1] {
				nums[j], nums[j+1] = nums[j+1], nums[j]
				swapped = true
			}
		}
		if !swapped {
			break
		}
	}
}
