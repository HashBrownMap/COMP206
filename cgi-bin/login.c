#include<stdio.h>
#include<stdlib.h>
#include<string.h>


int find(char *str){
FILE *memberslog=NULL;
char temp[300];

memberslog=fopen("members.csv", "rt");

if(memberslog == NULL){
	return -1;
}
while(fgets(temp,200,memberslog) != NULL)
{
	if((strstr(temp,str)) != NULL){
		return 1;
	}
}

fclose(memberslog);

}

int main(void){
int finding=0;
char temp[200];
char *string=NULL;
int n=atoi(getenv("CONTENT_LENGTH"));
char *username=NULL;
char *password=NULL;
char *user=NULL;
char *pass=NULL;
char *split="&";
char *splite="=";

if(getenv("CONTENT_LENGTH") != NULL){
if((string=malloc(sizeof(char) * n+1)) != NULL){
	if(((fread(string, sizeof(char), n, stdin))) == n){
		string[n]='\0';
	}
}
}
/*
while((c = getchar ()) != EOF && a<n){
	if(a<200){
		if(c!='+'){
		string[a]=c;
	}
	else{
	string[a]=' ';
	}
	a++;
 	}
 }
*/
//char *line=strdup(string);

username = strtok(string, split);
password = strtok(NULL, split);

//sscanf(username,"user=%s",user);
//sscanf(password,"pass=%s",pass);

strtok_r(username, splite, &user);

strtok_r(password, splite, &pass);


printf("Content-Type:text/html\n\n");
printf("<html>");
printf("<p>");
if(user == NULL){
	printf("user is null");
}
printf("%s\n", user);
printf("%s\n", pass);

printf("</p>");

	if(find(user)== 1){
		if(find(pass) == 1){
		printf("<p>WELCOME TO THE PAGE</p>");
		}
	}

	else if(find(user) == -1){
		printf("<p>MEMBER.CSV DOESNT EXIST</p>");
	}
	else{
		printf("<p>NOT A MEMBER</P>");
	}

printf("</html>");
return 0;
}


