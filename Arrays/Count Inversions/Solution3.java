// standard slef implemented BIT (Binary Indexed Tree)/Fenwick Tree class.
class BIT {
	private long [] bit_arr;
	BIT () { bit_arr = new long [100001]; }
	BIT (int size) { bit_arr = new long [size + 1]; }

	public long sum (long i) {
		long s = 0;
		while (i > 0) {
			s += bit_arr[(int)i]; i -= (i & -i);
		}
		return (s);
	}

	public void update (long i, long x) {
		while (i < bit_arr.length) {
			bit_arr[(int)i] += x; i += (i & - i);
		}
	}
}

// BIT solution is only applicable when size of array is <= 10^.
class Solution3 {
	private long max_num; // store the max num found in the inp array.

	public long inversionCount (long [] arr, long n) {
		long nof_inv_pairs = 0;
		long [] tmp_arr;
		// compress array only if it has elements > 10^5 or < 1.
		if (isCompArrReq(arr) == true) { tmp_arr = createCompressedArray(arr); }
        else { setMaxFromArray(arr); tmp_arr = arr; }
		BIT b = new BIT ((int)max_num);
		for (long item : tmp_arr) {
			nof_inv_pairs += (b.sum(max_num) - b.sum(item));
			b.update(item, 1);
		}
		return (nof_inv_pairs);
	}

	private long [] createCompressedArray (long [] arr) {
		long [] cp_arr = Arrays.copyOf(arr, arr.length);
		HashMap <Long, Long> hm = new HashMap <> ();
        setMaxFromArray(arr);
		Arrays.sort(cp_arr);
        long c = 1L;
		for (int j = 0; j < cp_arr.length; j++) {
			if (!(hm.containsKey(cp_arr[j]))) {
				hm.put(cp_arr[j], c); c++;
			}
		}
		for (int k = 0; k < arr.length; k++) {
			cp_arr[k] = hm.get(arr[k]);
		}
		max_num = hm.get(max_num);
		return (cp_arr);
	}
    
	// find max element in the inp array.
    private void setMaxFromArray (long [] arr) {
		max_num = Long.MIN_VALUE;
		for (int i = 0; i < arr.length; i++) {
			if (arr[i] > max_num) { max_num = arr[i]; }
		}
	}

	// function to check if array contains any non standard elements.
	private boolean isCompArrReq (long [] arr) {
		for (int i = 0; i < arr.length; i++) {
			if ((arr[i] > 100000) || (arr[i] < 1)) { return (true); }
		}
		return (false);
	}
}