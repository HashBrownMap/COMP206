#include<stdio.h>
#include<stdlib.h>
#include<string.h>


int find(char *str, char *string){
FILE *memberslog=NULL;
char temp[300];

memberslog=fopen("members.csv", "rt");

if(memberslog == NULL){
	return -1;
}
while(fgets(temp,200,memberslog) != NULL)
{
	if((strstr(temp,str)) != NULL){
		if((strstr(temp,string)) != NULL){
		return 1;
		}
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

username = strtok(string, split);
password = strtok(NULL, split);

strtok_r(username, splite, &user);
strtok_r(password, splite, &pass);


printf("Content-Type:text/html\n\n");
printf("<html>");


	if(find(user, pass)== 1){

	
	printf("<meta http-equiv=\"refresh\" content=\"0;url=http:\/\/www.cs.mcgill.ca/~zchen66/cgi-bin/feed.py\"\>");
	}
	else if(find(user, pass) == -1){
		printf("<p>MEMBER.CSV DOESNT EXIST</p>");
	}
	else{
	printf("<head><title>redirect</title>");
	printf("<meta http-equiv=\"refresh\" content=\"0;url=http:\/\/www.cs.mcgill.ca/~zchen66/fail.html\"\>");
	printf("</head>");

	}

printf("</html>");
return 0;
}


