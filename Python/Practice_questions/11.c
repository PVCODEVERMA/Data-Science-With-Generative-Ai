#include <stdio.h>
int main()
{
    int i = 0;
L:
    printf("%d", i );
    i = i + 2;

    if(i< 21)
    goto L;

    printf("\n\nTATA\n");

    return 0;
}

