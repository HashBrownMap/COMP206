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
while(!feof(memberslog)){
while(fscanf(memberslog,"%s",temp) == 1)
{
	if((strstr(str,temp)) != NULL){
		return 1;
	}
}
}
fclose(memberslog);
return 0;
}

int main(void){
//int find=0;
char string[200];
char *data;
int n=atoi(getenv("CONTENT_LENGTH"));
int a = 0;
char c;

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
string[a]='\0';

printf("Content-Type:text/html\n\n");
printf("<html>");
//printf("<head>TEST</head>");
//printf("<title>LOGIN RESULT</title>");
//data = getenv("QUERY_STRING");

//if(data == NULL){
//printf("<p> data is non existant</p>");
//}

//printf("<p>%s</p>",data);


	if(find(string) == 1){
		printf("<p>WELCOME TO THIS PAGE</p>");
	}
	else{
		printf("<p>FUCK NON-MEMBERS</P>");
}


printf("</html>");
return 0;
}


