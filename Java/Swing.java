import java.awt.GridLayout;
import javax.swing.*;
import javax.swing.tree.DefaultMutableTreeNode;

public class Swing
{
	public static void main(String[] args)
	{

		// JFrame : initialize a window
		JFrame f = new JFrame("My Java Swing GUI Practice"); 

		// JLabel()
		JLabel l1 = new JLabel("This is a text label.");
		l1.setHorizontalAlignment(JLabel.CENTER);
		f.add(l1);
	
		// JTextField
		JTextField t1 = new JTextField("This is a text field.");
		t1.setHorizontalAlignment(JLabel.CENTER);
		f.add(t1);

		// JButton
		JButton b1 = new JButton("OK");
		f.add(b1);
		
		//JList
		String gui[] = {"Windows Forms", "WPF", "Electron", "React Native", "Java Swing"};
		JList<String> list = new JList(gui);
		f.add(list);
		
		// JTable
		String data[][] =
		{
			{"Python", "aphoristic"},
			{"C++", "hostile"},
			{"Java", "too much talker"}
		};
		String varname[] = {"Name", "Character"};
		JTable table = new JTable(data, varname);
		f.add(table);

		// JTree
		DefaultMutableTreeNode node = new DefaultMutableTreeNode("Java");
		DefaultMutableTreeNode node100 = new DefaultMutableTreeNode("Javax"); node.add(node100);
		DefaultMutableTreeNode node110 = new DefaultMutableTreeNode("Swing"); node100.add(node110);
		DefaultMutableTreeNode node111 = new DefaultMutableTreeNode("JLabel"); node110.add(node111);
		DefaultMutableTreeNode node112 = new DefaultMutableTreeNode("JTextField"); node110.add(node112);
		DefaultMutableTreeNode node113 = new DefaultMutableTreeNode("JButton"); node110.add(node113);
		DefaultMutableTreeNode node200 = new DefaultMutableTreeNode("awt"); node.add(node200);
		DefaultMutableTreeNode node210 = new DefaultMutableTreeNode("GridLayout"); node200.add(node210);	
		JTree tree = new JTree(node);
		f.add(tree);

		// JSpinner
		JSpinner spinner = new JSpinner();
		f.add(spinner);

		// JSlider
		JSlider slider = new JSlider(JSlider.HORIZONTAL);
		f.add(slider);

		// JMenuBar / JMenu
		JMenuBar menuBar = new JMenuBar();
		JMenu fileMenu = new JMenu("File"); menuBar.add(fileMenu);
		JMenu menuItem1 = new JMenu("Open"); fileMenu.add(menuItem1);
		JMenu menuItem2 = new JMenu("Save"); fileMenu.add(menuItem2);
		JMenu menuItem3 = new JMenu("Quit"); fileMenu.add(menuItem3);
		JMenu helpMenu = new JMenu("Help"); menuBar.add(helpMenu);
		JMenu menuItem4 = new JMenu("About"); helpMenu.add(menuItem4);
		f.add(menuBar);
		
		f.setSize(600, 600);
		f.setLayout(new GridLayout(3, 3));
		f.setVisible(true);

	}
}