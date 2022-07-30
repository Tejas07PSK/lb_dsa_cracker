class Solution {
    private static void addAtBottom (Stack <Integer> s, int element) {
        if (!(s.isEmpty())) {
            int curr_ele = s.pop();
            addAtBottom(s, element);
            s.push(curr_ele);
        } else { s.push(element); }
    }

    private static void reverseHelper (Stack <Integer> s) {
        if (s.isEmpty()) { return; }
        int element = s.pop();
        reverseHelper(s);
        addAtBottom(s, element);
    }

    static ArrayList <Integer> reverse (Stack <Integer> s) {
        ArrayList <Integer> res = new ArrayList <Integer> ();
        reverseHelper(s);
        while (!(s.isEmpty())) { res.add(0, s.pop()); }
        return res;
    }
}