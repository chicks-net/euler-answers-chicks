#!/usr/bin/perl

use strict;
use warnings;
use Data::Dumper;
use File::Slurp;
#use Math::Prime::Util qw(divisors);
#use Algorithm::Combinatorics qw(variations_with_repetition variations);
#use Time::HiRes qw(gettimeofday tv_interval);

sub sum {
	my $sum = 0;
	map { $sum += $_} @_;
	return $sum;
}

# read arguments/file
die "no arguments\nusage; $0 <triangle file>" unless scalar @ARGV;
my($filename) = @ARGV;
die "no file $filename" unless -f $filename;
my $triangle_raw = read_file($filename);

# parse file
my @lines = split(/\n/,$triangle_raw);
my @triangle;
foreach my $line (@lines) {
	next if $line =~ /^#/;
	next unless length $line;
	my @elements = split(/\s+/,$line);
	unshift(@triangle,[@elements]);
}
#print Dumper(\@triangle);

my $rows = scalar(@triangle) -1;

for (my $r = 0 ; $r < $rows; $r++) {
	my @row = @{$triangle[$r]};
	print "$r -> " . join(',',@row) . "\n";

	my $pairs = (scalar @row) -1;
	for (my $p = 0 ; $p < $pairs; $p++) {
		my $a = $row[$p];
		my $b = $row[$p+1];
		my $bigger = 0;
		if ($a >= $b) {
			#print "[$p] $a is BIGger than $b\n";
			$bigger = $a;
		} else {
			#print "[$p] $b is bigger than $a\n";
			$bigger = $b;
		}
		$triangle[$r+1]->[$p] += $bigger;
	}
}

my $sum = $triangle[$rows]->[0];
print "ANSWER:$sum\n";
