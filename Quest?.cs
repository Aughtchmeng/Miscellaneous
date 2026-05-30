using System;

namespace TextRPG
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.Title = "The C# Adventure";

            Console.WriteLine("Welcome to the C# Console Dungeon!");
            Console.Write("Enter your character's name: ");
            string playerName = Console.ReadLine();

            Player player = new Player(playerName);
            Dungeon dungeon = new Dungeon();

            Console.WriteLine($"\nGreetings, {player.Name}! Your adventure begins now...\n");

            while (player.IsAlive && !dungeon.IsCleared)
            {
                dungeon.RunRoom(player);
            }

            if (player.IsAlive)
            {
                Console.WriteLine("\nCongratulations! You have conquered the dungeon and won the game!");
            }
            else
            {
                Console.WriteLine("\nAlas, you have fallen in the dungeon. Game Over.");
            }

            Console.WriteLine("\nPress any key to exit...");
            Console.ReadKey();
        }
    }

    class Player
    {
        public string Name { get; set; }
        public int Health { get; set; } = 100;
        public int AttackPower { get; set; } = 15;
        public int Potions { get; set; } = 3;
        public bool IsAlive => Health > 0;

        public Player(string name)
        {
            Name = name;
        }

        public void TakeDamage(int damage)
        {
            Health -= damage;
            if (Health < 0) Health = 0;
            Console.WriteLine($"{Name} takes {damage} damage! HP: {Health}/100");
        }

        public void Heal()
        {
            if (Potions > 0)
            {
                Health = Math.Min(100, Health + 30);
                Potions--;
                Console.WriteLine($"{Name} used a potion. HP: {Health}/100. Potions left: {Potions}");
            }
            else
            {
                Console.WriteLine("You are out of potions!");
            }
        }
    }

    class Enemy
    {
        public string Name { get; set; }
        public int Health { get; set; }
        public int AttackPower { get; set; }
        public int XpReward { get; set; }
        public bool IsAlive => Health > 0;

        public Enemy(string name, int health, int attack, int xp)
        {
            Name = name;
            Health = health;
            AttackPower = attack;
            XpReward = xp;
        }

        public void TakeDamage(int damage)
        {
            Health -= damage;
            if (Health < 0) Health = 0;
            Console.WriteLine($"You dealt {damage} damage to the {Name}. Enemy HP: {Health}");
        }
    }

    class Dungeon
    {
        private int _currentRoom = 0;
        private int _maxRooms = 4;
        public bool IsCleared => _currentRoom >= _maxRooms;

        public void RunRoom(Player player)
        {
            _currentRoom++;
            Console.WriteLine($"--- Room {_currentRoom} of {_maxRooms} ---");
            
            Enemy enemy = GenerateEnemy();
            Console.WriteLine($"A wild {enemy.Name} appears!");

            while (player.IsAlive && enemy.IsAlive)
            {
                Console.WriteLine("\nChoose an action:");
                Console.WriteLine("1. Attack");
                Console.WriteLine("2. Use Potion");
                Console.WriteLine("3. Run Away");
                Console.Write("> ");
                string choice = Console.ReadLine();

                switch (choice)
                {
                    case "1":
                        enemy.TakeDamage(player.AttackPower);
                        if (enemy.IsAlive)
                        {
                            player.TakeDamage(enemy.AttackPower);
                        }
                        break;
                    case "2":
                        player.Heal();
                        break;
                    case "3":
                        Console.WriteLine("You cowardly run away to the previous room!");
                        _currentRoom--;
                        return;
                    default:
                        Console.WriteLine("Invalid choice. Try again.");
                        break;
                }
            }

            if (enemy.Health <= 0)
            {
                Console.WriteLine($"You defeated the {enemy.Name}!");
                // Reward player
                player.AttackPower += 2;
                Console.WriteLine("Your attack power increased!");
            }
        }

        private Enemy GenerateEnemy()
        {
            Random rnd = new Random();
            int type = rnd.Next(1, 4);

            return type switch
            {
                1 => new Enemy("Goblin", 30, 5, 10),
                2 => new Enemy("Orc", 50, 10, 20),
                3 => new Enemy("Ogre", 80, 15, 30),
                _ => new Enemy("Skeleton", 40, 8, 15),
            };
        }
    }
}
