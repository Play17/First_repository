#include <stdio.h> 
#include <string.h>
#define MAX 100
int main(){
	char min[MAX];
	char mi[MAX];
	int add=2,i;
	printf("¼ÓÃÜ×Ö·û¬¦:");
	scanf("%s",&min);
	for(i=0;i<strlen(min);i++){
		if(min[i] >= 'a' && min[i] <= 'z'){
			min[i] = ((min[i]-'a')+add)%26+'a';
		}else if(min[i]==';'){
			min[i]='\0';
		}
	}
	printf("%s",min); 
}
