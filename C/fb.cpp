#include <stdio.h>

unsigned int fibonacci(unsigned int n);

unsigned int fibonacci(unsigned int n)
{
        if (n == 1 || n == 2)
        {
                return 1;
        }
        else
        {
                return fibonacci(n-1) + fibonacci(n-2);
        }
}

int main(void)
{
        unsigned int number, i;

        printf("������һ��������");
        scanf("%u", &number);

        printf("쳲��������е�ǰ %d �������ǣ�", number);
        for (i = 1; i <= number; i++)
        {
                printf("%lu ", fibonacci(i));
        }
        putchar('\n');

        return 0;
}
