package com.company;

import java.util.HashSet;

/**
 * Created by Lina Yi on 5/19/16.
 */

public class IdenticalStringSets {

    public static void main(String[] args) {
        String[][] test1 = {{"a", "c"}, {"c", "c", "a"}, {"c", "a"}, {"c", "a", "a", "c", "a"}};
        String[][] test2 = {{"a", "b"},{"b", "b", "a"},{"b", "a"}};
        String[][] test3 = {{"a", "b"}, {"a"}, {"b"}};
        String[][] test4 = {};
        System.out.println(allStringSetsIdentical(test1));
        System.out.println(allStringSetsIdentical(test2));
        System.out.println(allStringSetsIdentical(test3));
    }

    /*
    allStringSetsIdentical takes in an array of arrays that contain sets of strings and returns true if all the sets are equivalent
    or false
     */

    public static boolean allStringSetsIdentical(String[][] sets) {
        if (sets.length > 0) {
            HashSet<String> baseSet = addToSet(sets[0]);        

            for (int i = 1; i < sets.length; i++) {
                HashSet<String> newSet = addToSet(sets[i]);
                if (!baseSet.equals(newSet)) {
                    return false;
                }
            }
        }
        return true;
    }

    /*
    addToSet takes in a string array and adds the strings items
    contained within it and adds them to a HashSet
     */
    public static HashSet<String> addToSet(String[] iteratorArray) {
        HashSet<String> iteratorSet = new HashSet<String>();
        for (int i = 0; i < iteratorArray.length; i++) {
            iteratorSet.add(iteratorArray[i]);
        }
        return iteratorSet;
    }
}