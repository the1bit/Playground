using System;

// Static class has no constructors
static class Utilities
{
    // Because this is static you have to use the static keyword for functions
    public static void ColorfulWriteLine(string message, ConsoleColor color)
    {
        Console.ForegroundColor = color;
        Console.WriteLine(message);
        Console.ResetColor();
    }
}

