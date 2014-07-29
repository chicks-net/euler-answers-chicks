#!/usr/bin/perl -w

use strict;
use warnings;
use Data::Dumper;

# read file
my $fh;
open($fh,"<","words.txt") or die "could not open words.txt: $!";
my $line = <$fh>;
close($fh);
chomp($line);
my @words = split(/,/, $line);

# chacter value map
my %cval;

my $cur = 1;
foreach my $letter ('A'..'Z') {
	$cval{$letter} = $cur;
	$cur++;
}

# calculate triangle numbers
my $max_triangle = 192;
my $cur_triangle = 1;
my $n = 1;
my %triangles = ( 1 => 1 );

while ($cur_triangle < $max_triangle) {
	$n++;
	$cur_triangle = .5 * $n * ($n + 1);
	$triangles{$cur_triangle} = $n;
}

#print Dumper(\%triangles);

# find word values
my $max_value = 0;
my $count = 0;
foreach my $word (@words) {
	$word =~ s/"$//;
	$word =~ s/^"//;
	my $value = 0;
	foreach my $letter ( split(//,$word) ) {
		$value += $cval{$letter};
	}
	$max_value = $value if $value > $max_value;
	next unless defined $triangles{$value};
	#print "$word $value\n";
	$count++;
}
#print "max value = $max_value\n";
print "ANSWER:$count\n";
