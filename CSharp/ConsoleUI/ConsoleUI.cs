// need Terminal.Gui - Terminal GUI toolkit for .NET
// https://github.com/migueldeicaza/gui.cs
// Terminal Command : dotnet add package Terminal.Gui


using System;

namespace ConsoleUI
{
    using Terminal.Gui; 
    class ConsoleUI
    {
        static void Main ()
        {

            Application.Init();

            var win = new Window ("Hello World - CTRL-Q to quit")
            {
                X = 5,
                Y = 5,
                Width = Dim.Fill (5),
                Height = Dim.Fill (5)
            };
            Application.Top.Add(win);

            Application.Run();

        }
    }
}