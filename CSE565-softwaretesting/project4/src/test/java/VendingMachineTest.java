import org.junit.Test;
import static org.junit.Assert.*;


public class VendingMachineTest {

    @Test
    public void testDispenseCandyExact() {
        String result = VendingMachine.dispenseItem(20, "candy");
        assertTrue(result.contains("dispensed") || result.contains("candy"));
    }

    @Test
    public void testDispenseCokeExact() {
        String result = VendingMachine.dispenseItem(25, "coke");
        assertTrue(result.contains("Item dispensed") || result.contains("coke"));
    }

    @Test
    public void testDispenseCoffeExact() {
        String result = VendingMachine.dispenseItem(50, "coffee");
        assertTrue(result.contains("Item dispensed and change") || result.contains("coffee"));
    }

    @Test
    public void testNotEnoughForAny() {
        String result = VendingMachine.dispenseItem(10, "candy");
        assertTrue(result.contains("Cannot purchase item."));
    }

    @Test
    public void testEnoughForCandyOnly() {
        VendingMachine vm = new VendingMachine();
        String result = VendingMachine.dispenseItem(22, "coke");
        assertTrue(result.contains("Can purchase candy."));
    }

    @Test
    public void testEnoughForCandyOrCoke() {
        String result = VendingMachine.dispenseItem(38, "coffee");
        assertTrue(result.contains("Can purchase candy or coke."));
    }

}