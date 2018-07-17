using System;
using WarriorWars.Enum;

namespace WarriorWars
{
    class Program
    {
        static Random rnd = new Random();



        static void Main()
        {
            Warrior goodGuy = new Warrior("Tibi", Faction.GoodGuy);
            Warrior badGuy = new Warrior("Ricsi", Faction.BadGuy);

            while (goodGuy.IsAlive && badGuy.IsAlive)
            {
                if (rnd.Next(0,10) < 5)
                {
                    goodGuy.Attack(badGuy);
                }
                else
                {
                    badGuy.Attack(goodGuy);
                }
            }
            
        }
    }
}
