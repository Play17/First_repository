#include <stdio.h>
#include <string.h>

int main(){
	char mi[100];
	printf("����������ܵ��ı�:����;��������");
	scanf("%s",&mi);
	int i,add=2;
	for(i=0;i<strlen(mi);i++){
		if(mi[i] >= 'a' && min[i] <= 'z'){
			mi[i] = ((mi[i]-'a')-add)+'a';
		}else if(mi[i] == ';'){
			mi[i] = '\0';
		}
	}
	printf("����:%s",mi);
} 
