import java.awt.GridLayout;
import javax.swing.JCheckBox;
import javax.swing.JFrame;

public class ActionListener {

	public static void main(String[] args) {

		// JFrame : initialize a window
		JFrame f = new JFrame("Peekaboo Machine for My Son"); 

		// JCheckBox
		JCheckBox checkBox1 = new JCheckBox("Peakaboo!");
		checkBox1.setHorizontalAlignment(JCheckBox.CENTER);
		f.add(checkBox1);
		
		f.setSize(300, 600);
		f.setLayout(new GridLayout(1, 2));
		f.setVisible(true);
		
	}

}