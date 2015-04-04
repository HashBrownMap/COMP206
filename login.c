#include<stdio.h>
#include<stdlib.h>
#include<string.h>

int main(void){
FILE *memberslog;
int find=0;
char temp[200];
char *data=getenv("QUERY_STRING");


memberslog = fopen("members.txt", "rt");
if(memberslog == NULL){
printf("<p> MEMBERS.TXT CANT BE FOUND</P>");
}
printf("<p>%s</p>",data);


while(fgets(temp,200, memberslog) != NULL){
	if((strstr(temp, data)) != NULL){
		printf("<p>WELCOME TO THIS PAGE</p>");
		find =1;
	}
}
fclose(memberslog);

if(find ==0){
	printf("<p>YOU ARE NOT A MEMBER OF THIS PAGE</p>");
}
}


