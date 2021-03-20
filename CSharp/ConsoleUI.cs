// Terminal Command : dotnet add package Terminal.Gui


using System;

namespace ConsoleUI
{

    using Terminal.Gui; 

    class MainClass
    {

        static int Main ()
        {

            Application.Init ();

            var n = MessageBox.Query (50, 7,
                "Question", "Do you like console apps?", "Yes", "No");

            return n;

        }

    }

}