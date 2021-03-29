class TreeNode {
	public long val;	// store value of node as froun in original array.
	public int height;  // store height of current node.
	public int noc;		// store number of children for current node.
	public int occr;	// store number of occurrences of node value, in original array.
	public TreeNode left;	// pointer to left sub tree.
	public TreeNode right;	// pointer to right sub tree.
	public TreeNode () {
		val = 0; height = 0; noc = 0;
		occr = 1; left = null; right = null;
	}
	public TreeNode (long val) { this(); this.val = val; }
	public TreeNode (long val, int height, int noc, int occr, TreeNode left, TreeNode right) {
		this.val = val; this.height = height; this.noc = noc;
		this.occr = occr; this.left = left; this.right = right;
	}
}

class Solution2 {
	private static long nof_inv_pairs; // counter for inversion pairs in array.
	private static int al_ex_flg;	// flag to determine if value already exists in tree, to avoid duplicate entries.
	
	public long inversionCount (long [] arr, long n) {
		nof_inv_pairs = 0;
		TreeNode root = new TreeNode (arr[0]);
		for (int i = 1; i < arr.length; i++) {
			TreeNode node = new TreeNode (arr[i]);
			root = insertIntoAvlTree(root, node);
			al_ex_flg = 0;
		}
		return (nof_inv_pairs);
	}

	private TreeNode insertIntoAvlTree (TreeNode root, TreeNode node) {
		if (node.val > root.val) {
			if (root.right == null) { root.right = node; }
			else { TreeNode nrt = insertIntoAvlTree(root.right, node); root.right = nrt; }
		} else if (node.val < root.val) {
			nof_inv_pairs += (root.occr + ((root.right == null) ? 0 :( root.right.noc + root.right.occr))); // inversion will occur when insertion value is less than current node value, hence count parent node occurences + right sub tree childern will their corresponding occurrences.
			if (root.left == null) { root.left = node; }
			else { TreeNode nlt = insertIntoAvlTree(root.left, node); root.left = nlt; }
		} else {
		    nof_inv_pairs += ((root.right == null) ? 0 :( root.right.noc + root.right.occr)); // special corner case, where duplicate node already has a right subtree.
		    root.occr++; al_ex_flg = 1; // don't increase current node occurrence before
		}
		setNoOfChildren(root); // always update child count for current node.
		if (al_ex_flg != 1) {
			setHeight(root);
			root = rotate(root);
		}
		return (root);
	}

	private TreeNode rotate (TreeNode node) {
		int bf = getBf(node);
		if (bf > 1) {
			bf = getBf(node.left);
			if (bf > 0) { return (LLorRR(node, node.left, 0)); }
			else { return (LRorRL(node, node.left, node.left.right, 0)); }
		} else if (bf < -1) {
			bf = getBf(node.right);
			if (bf < 0) { return (LLorRR(node, node.right, 1)); }
			else { return (LRorRL(node, node.right, node.right.left, 1)); }
		} else { return (node); }
	}

	private int getBf (TreeNode node) {
		return (((node.left == null) ? 0 : (node.left.height + 1)) - ((node.right == null) ? 0 : (node.right.height + 1)));
	}

	private void setHeight (TreeNode node) {
		node.height = Math.max(((node.left == null) ? 0 : (node.left.height + 1)), ((node.right == null) ? 0 : (node.right.height + 1)));
	}
	
	// for this problem while counting number of children for a node, consider their frequency also, as found in the original array.
	private void setNoOfChildren (TreeNode node) {
		node.noc = (((node.left == null) ? 0 : (node.left.noc + node.left.occr)) + ((node.right == null) ? 0 : (node.right.noc + node.right.occr)));
	}

	private TreeNode LLorRR (TreeNode node1, TreeNode node2, int typ) {
		if (typ == 0) {
			node1.left = node2.right;
			node2.right = node1;
		} else {
			node1.right = node2.left;
			node2.left = node1;
		}
		setNoOfChildren(node1); setNoOfChildren(node2);
		setHeight(node1); setHeight(node2);
		return (node2);
	}

	private TreeNode LRorRL (TreeNode node1, TreeNode node2, TreeNode node3, int typ) {
		if (typ == 0) {
			node2.right = node3.left;
			node1.left = node3.right;
			node3.left = node2;
			node3.right = node1;
		} else {
			node2.left = node3.right;
			node1.right = node3.left;
			node3.right = node2;
			node3.left = node1;
		}
		setNoOfChildren(node2); setNoOfChildren(node1); setNoOfChildren(node3);
		setHeight(node2); setHeight(node1); setHeight(node3);
		return (node3);
	}
}