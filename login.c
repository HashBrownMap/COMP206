#include<stdio.h>
#include<stdlib.h>
#include<string.h>


int find(char *str){
FILE *memberslog;
char temp[300];

memberslog=fopen("members.txt", "rt");

if(memberslog == NULL){
	return 0;
}
while(fgets(temp,200,memberslog) != NULL)
{
	if((strstr(temp,str)) != NULL){
		return 1;
	}
}

fclose(memberslog);
return 0;
}

int main(void){
int finding=0;
FILE *memberslog;
char temp[200];
char *string= NULL;
char *data;
int n=atoi(getenv("CONTENT_LENGTH"));
int a = 0;
char c;
int i=0;
char *user;
char *pass;
char *split="&";

if(getenv("CONTENT_LENGTH") != NULL){
if((string=malloc(sizeof(char) * n+1)) != NULL){
	if(((fread(string, sizeof(char), n, stdin))) == n){
		string[n]='\0';
	}
}
}

user = strtok(string, split);
pass = strtok(NULL, split);

printf("Content-Type:text/html\n\n");
printf("<html>");
printf("<p>");

printf("%s\n", user);
printf("%s\n", pass);

printf("</p>");
finding=(find(user));

if(finding == 1){
		printf("<p>WELCOME TO THIS PAGE</p>");
}


	if(finding == 0){
		printf("<p>FUCK NON-MEMBERS</P>");
}

printf("</html>");
return 0;
}


