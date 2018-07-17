using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;


namespace PointsAndLines
{
    class Point
    {
        // public means the variable is used outside of class too
        // private means it is used only inside the clsass
        private int x;
        private int y;
        private int xySum;

        private int z;

        // Properties - prop <tab><tab>
        public int X
        {
            get
            {
                // Get togives back the result
                return x;
            }

            set
            {
                // Set the value of field
                x = value;
            }
        }

        // Property without extra code
        public int Y { get; set; }


        // Function without constructor
        public Point()
        {
            
        }

        // Function with constructor
        public Point(int x, int y)
        {
            // This means the variable inside the class and not insode the function
            // Use it for every time to avoid the variable name duplication
            this.x = x;
            this.y = y;
            this.z = 5;
        }
    }

    class User
    {
        // public means the variable is used outside of class too
        // static means this variable is a static variable which is accessible on Class level
        public static int currentID;


        // constants are used with CAPITAL_LETTER_AND_UNDERLINE
        // const - hardcoded
        // readonly - value is assigned sat runtime through code logic
        public readonly int ID;
        public const int WEIGHT = 177;
        public readonly int HEIGHT;

        public Race race;

        // private means it is used only inside the clsass
        private string username;
        private int password;

        // Properties - prop <tab><tab>
        public string Username
        {
            get
            {
                // Get togives back the result
                return "The username is: " + username;
            }

            set
            {
                // Set the value of field
                if (value.Length >= 4 && value.Length <= 10)
                {
                    username = value;
                }
                else
                {
                    System.Console.WriteLine("The username's length must be 4 and 10 characters");
                }
                
            }
        }

        public string UsernameR
        {
            // Read-only property
            get
            {
                return username;
            }
        }

        public int Password
        {
            // Write only property
            set
            {
                if (value >= 4 && value <= 10)
                {
                    password = value;
                }
                else
                {
                    System.Console.WriteLine("The password is not valid. Please use a number between 4 and 10");
                }


            }
                
        }


        // Function without constructor
        public User()
        {
            currentID++;
            ID = currentID;
        }

        // Function with constructor
        // Constructor short key: ctor <tab><tab>
        public User(string username, Race race)
        {
            currentID++;
            ID = currentID;
            // This means the variable inside the class and not insode the function
            // Use it for every time to avoid the variable name duplication
            this.username = username;
            this.race = race;
            if (this.race == Race.Marsian)
            {
                HEIGHT = 100;
            }
            else if (this.race == Race.Earthling)
            {
                HEIGHT = 180;
            }
        
        }

        public void SayMyName()
        {
            Utilities.ColorfulWriteLine(this.Username, System.ConsoleColor.DarkGreen);
        }
    }
}
