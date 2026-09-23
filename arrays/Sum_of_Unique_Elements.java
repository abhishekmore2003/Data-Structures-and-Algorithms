import java.util.*;
import java.util.Arrays;
import java.util.Scanner;
import java.util.Collections;

public class Sum_of_Unique_Elements
{
    public static void main(String[]args)
    {
        int array[] = {0,0,0,0,0};


        HashMap<Integer,Integer> lst = new HashMap<>();

        for (int i=0 ; i<array.length ; i++)
        {
            if(lst.containsKey(array[i]))
            {
                int value = lst.get(array[i]);
                value += 1 ;
                lst.put(array[i],value);
            }
            else
            {
                lst.put(array[i],1);
            }
        }

        int sum = 0;

        for (int i : lst.keySet())
        {
            if (lst.get(i) != 1)
            {
                continue;
            }
            else
            {
                sum += 1;
            }
        }

        System.out.println("Sum = "+sum);



    }

}