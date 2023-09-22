#include <cstring>
#include <cstdio>
#include <cstdlib>

int main()
{
    const char *s = "Hello, World! ";
    printf("%s\n",s);
    printf("strlen(s) = %d\n", strlen(s));
    int times_to_concatenate;
    scanf("%d", &times_to_concatenate);
    size_t buffer_lenght = strlen(s)*times_to_concatenate +1;
    char *buffer = (char*) malloc(buffer_lenght*sizeof(char));
    buffer[0] = '\0';
    printf("%s\n",s);

    for (int i = 0; i < times_to_concatenate; i++)
    {
        strcat(buffer, s);
    }
    
    printf("%s\n",s);

    free(buffer);
    return 0;
}