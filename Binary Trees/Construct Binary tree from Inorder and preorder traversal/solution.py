class Solution
{
    static  HashMap<Integer,Integer>g=new HashMap<>();
    static int index;
    static Node sub(int in[],int pre[],int ins,int ind)
   {
       if(index>=in.length||ins>ind)
         return null;
        int element=pre[index];
        index++;
        int posi=g.get(element);
        Node root=new Node(element);
       root.left=sub(in,pre,ins,posi-1);
       root.right=sub(in,pre,posi+1,ind);
       return root;
       
         
   }
   public static Node buildTree(int in[], int pre[], int n)
   {
       
       g.clear();
       index=0;
       for(int i=0;i<in.length;i++)
       {
           g.put(in[i],i);
          
       }
           
       Node root=sub(in,pre,0,n-1);
       return root;
      
   }
}
