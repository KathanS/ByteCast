//Create Gamer Processes and Start Game!
#include<bits/stdc++.h>
using namespace std;

vector<pid_t> Gamers(5);

char *args[]={"./Gamer",NULL};

int main()
{
    
    for(int i = 0; i < 5; i++)
    {
        pid_t gamer = fork();
        if(gamer != 0)
        {
            Gamers[i] = gamer;
        }
        else
        {
            execvp(args[0], args);
        }
    }
}