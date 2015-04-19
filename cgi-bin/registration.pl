#!/usr/bin/perl
use CGI ':standard';

my $data;
my @raw;
my @lines;
my $key1;
my $name;
my $key2;
my $user;
my $key3;
my $pass;
my $REPLY;
my $link;
my $linke;
my $error;

my $bool="false";
my $file = 'members.csv';
my $boole = "false";
read(STDIN, $data, $ENV{CONTENT_LENGTH});

@raw = split /&/, $data;
##############splits the string##################
($key1, $name) = split /=/, $raw[0];
($key1, $user) = split /=/, $raw[1];
($key1, $pass) = split /=/, $raw[2];
	
	
open(txt, "$file");
@lines = <txt>;
print "Content-Type: text/html \n\n";
####################see if username already exists######################3
foreach $line (@lines){
	chomp($line);
	($a_name,$a_user,$a_pass)=split(/ /,$line,3);
	
	if($a_user eq $user) {
	$bool="true";
	$REPLY="UNSUCCESSFUL";
	$link="<meta http-equiv=\"refresh\" content=\"0;url=http:\/\/www.cs.mcgill.ca/~zchen66/failure.html\"\>";
	}
}
close(txt);
######################writes it in members.csv or else#####################
open(txt,">>members.csv");
if($bool eq "false"){
	print txt "$name $user $pass\n";
	$REPLY="SUCCESS";
	$link="<meta http-equiv=\"refresh\" content=\"0;url=http:\/\/www.cs.mcgill.ca/~zchen66/success.html\"\>";
}
close(txt);

print "<html>\n";
print "<head>\n";
print "<title></title>";
print "</head>\n";
print "<body>";
print "$link\n";
print "</body>";
print "</html>\n";
