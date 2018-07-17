using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using PointsAndLines;


namespace Classes
{
    class Human
    {
        public int Height;
        public int Weight;

        public Human(int height, int weight)
        {
            Height = height;
            Weight = weight;
        }
    }

    class Program
    {
        static void Main(string[] args)
        {
            /* Points
            Point point = new Point(5, 3);

            Point pointTwo = new Point();

            pointTwo.X = 5;
            pointTwo.Y = 3;

            //System.Console.WriteLine(point.X);
            //System.Console.WriteLine(point.y);

            Human human = new Human(177, 91);

            Console.WriteLine(human.Height);
            */

            /* User */

            User user = new User("Tibi", Race.Earthling);
            
            // ID is usable on class level
            //System.Console.WriteLine(User.currentID);

            User secondUser = new User();
            

            User thirdUser = new User();

            // Use our static class
            user.SayMyName();


            
            // Shortcut for console.writeline: cw <tab><tab>
            Console.WriteLine(user.ID);
            Console.WriteLine(secondUser.ID);
            Console.WriteLine(thirdUser.ID);

            user.Password = 5;
            System.Console.WriteLine(user.UsernameR);

            

            // ID is usable on class level
            System.Console.WriteLine(User.currentID);

            System.Console.ReadKey();
        }
    }
}
