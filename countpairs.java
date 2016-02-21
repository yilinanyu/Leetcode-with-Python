package countpairs;
 
public class CountPairs {
    /**
     * countPairs returns the number of pairs of integers in a that add up to x.
     *  Given a = [1,2,3,4] and x = 5, countPairs should return 2. This is because
     *  the sum of [1,4] is 5 and the sum of [2,3] is 5 and those are the only two
     *  pairs that add up to 5.
     */
    static int countPairs(int a[], int x)
    {
       int count = 0;
       for(int i=0; i<a.length; i++) {
           for(int j=0; j<a.length; j++) {
               if (i+j==x) {
                   count ++;
               }
           }
       }
       return count;
   }
}