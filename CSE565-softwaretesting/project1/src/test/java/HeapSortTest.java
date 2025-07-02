import static org.junit.Assert.*;
import org.junit.Test;

public class HeapSortTest {

    @Test
    public void testSortWithUnsortedArray() {
        int[] arr = {12, 11, 13, 5, 6, 7};
        int[] expected = {5, 6, 7, 11, 12, 13};
        HeapSort hs = new HeapSort();
        hs.sort(arr);
        assertArrayEquals(expected, arr);
    }

    @Test
    public void testSortWithAlreadySortedArray() {
        int[] arr = {1, 2, 3, 4, 5};
        int[] expected = {1, 2, 3, 4, 5};
        HeapSort hs = new HeapSort();
        hs.sort(arr);
        assertArrayEquals(expected, arr);
    }

    @Test
    public void testSortWithReverseSortedArray() {
        int[] arr = {5, 4, 3, 2, 1};
        int[] expected = {1, 2, 3, 4, 5};
        HeapSort hs = new HeapSort();
        hs.sort(arr);
        assertArrayEquals(expected, arr);
    }

    @Test
    public void testSortWithDuplicates() {
        int[] arr = {4, 1, 3, 4, 2, 1};
        int[] expected = {1, 1, 2, 3, 4, 4};
        HeapSort hs = new HeapSort();
        hs.sort(arr);
        assertArrayEquals(expected, arr);
    }

    @Test
    public void testSortWithSingleElement() {
        int[] arr = {42};
        int[] expected = {42};
        HeapSort hs = new HeapSort();
        hs.sort(arr);
        assertArrayEquals(expected, arr);
    }

    @Test
    public void testSortWithEmptyArray() {
        int[] arr = {};
        int[] expected = {};
        HeapSort hs = new HeapSort();
        hs.sort(arr);
        assertArrayEquals(expected, arr);
    }

    @Test
    public void testSortWithNegativeNumbers() {
        int[] arr = {-3, -1, -7, -4, -5, -2};
        int[] expected = {-7, -5, -4, -3, -2, -1};
        HeapSort hs = new HeapSort();
        hs.sort(arr);
        assertArrayEquals(expected, arr);
    }
}

// We recommend installing an extension to run java tests.