import java.util.Arrays;

class Solution1 {
	private static int glob_inversions = 0;
	
	private static int countInversions (int [] arr) {
		glob_inversions = 0;
		int [] srt_arr = modMergeSort(arr);
		return (glob_inversions);cd
	}
	
	private static int [] modMergeSort (int [] arr) {
		if (arr.length == 1) { return (arr); }
		if (arr.length == 2) {
			if (arr[0] > arr[1]) {
				swap(arr, 0, 1);
				glob_inversions++;
			}
			return (arr);
		}
		int mid = ((arr.length - 1) / 2);
		int [] L = new int [mid + 1]; int [] R = new int [arr.length - mid - 1];
		for (int k = 0, s = 0; k < arr.length; k++) {
			if (k <= mid) { L[k] = arr[k]; }
			else { R[s] = arr[k]; s++; }
		}
		L = modMergeSort(L); R = modMergeSort(R);
		return (mergeNCount(L, R));
	}
	
	private static void swap (int [] arr, int i, int j) {
		arr[i] ^= arr[j];
		arr[j] ^= arr[i];
		arr[i] ^= arr[j];
	}
	
	/*
		Count smaller elements already filled from the right array.
		Now, since both arrays are seperate their (index + 1) value will
		always give the count of smaller and equal numbers so far till that index.
		If we think a bit we'll see that the count of smaller numbers already filled
		from the right array, is actually the global inversion count because these numbers
		appeared later in the original array and the numbers which came in before are greater or equal.
		Hence, this is nothing but arr[i] > arr[j], where i < j.
	*/
	private static int [] mergeNCount (int [] L, int [] R) {
		int [] arr = new int [L.length + R.length];
		int i = 0, j = 0, k = 0;
		while ((i < L.length) && (j < R.length)) {
			if (L[i] > R[j]) {
				arr[k] = R[j];
				j++;
			} else {
				arr[k] = L[i];
				i++; glob_inversions += j;  // counting here
			}
			k++;
		}
		while (i < L.length) {
			arr[k] = L[i];
			i++; k++; glob_inversions += j; // counting here
		}
		while (j < R.length) {
			arr[k] = R[j];
			j++; k++;
		}
		return (arr);
	}
	
	// driver code to test custom usecase in your system, not online platform
	/*
		public static void main (String [] args) {
			int arr [] = { 1, 20, 6, 4, 5 };
			System.out.println(countInversions(arr));
		}
	*/
}
