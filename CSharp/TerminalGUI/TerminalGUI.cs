/*
// Terminal.Gui - Terminal GUI toolkit for .NET
https://github.com/migueldeicaza/gui.cs
Terminal Command for installation : dotnet add package Terminal.Gui

// Reference
https://migueldeicaza.github.io/gui.cs/index.html
https://sirwan.info/archive/2018/05/02/Developing-Console-based-UI-in-C/
https://itnext.io/terminal-console-user-interface-in-net-core-4e978f1225b
https://youtu.be/sVYiDboAe_E
*/


using System;

namespace TerminalGUI
{
    using Terminal.Gui; 
    class TerminalGUI
    {
        static void Main ()
        {

            Application.Init ();
            var top = Application.Top;

            // top.Add (win);

            // Creates a menubar, the item "New" has a help menu.
            var menu = new MenuBar(new MenuBarItem[]
            {
                new MenuBarItem("_File", new MenuItem[]
                {
                    new MenuItem("_Quit", "", () => Application.RequestStop())
                }), // end of file menu
                new MenuBarItem("_Help", new MenuItem[]
                {
                    new MenuItem("_About", "", () 
                    => MessageBox.Query(10, 5, "About", "C# - Terminal GUI Practice\n2021.03.22.", "Ok"))
                }) // end of the help menu
            });

            // Creates the top-level window to show
            // Dynamically computed
            var win = new Window ()
            {
                X = 0,
                Y = 1,
                Width = Dim.Fill (),
                Height = Dim.Fill () - 1
            };

            top.Add(menu, win);
            Application.Run();

        }
    }
}