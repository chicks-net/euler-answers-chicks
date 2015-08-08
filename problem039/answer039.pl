#!/usr/bin/perl

use strict;
use warnings;

my $max_triangles = 0;
my $max_p = 0;
foreach my $p (3..1000) {
#foreach my $p (12,840,1680) {
	my $tri = triangles($p);
	if ( $tri > $max_triangles ) {
		$max_triangles = $tri;
		$max_p = $p;
	}
	print "triangles($p)=$tri     max=$max_p\n" if $tri;
}
print "ANSWER:$max_p\n";

# how many right triangles are there with a given perimeter?
sub triangles {
	my ($perimeter) = @_;

	if ($perimeter < 3) {
		die "bad perimeter $perimeter";
	}

	my $valid_triangles = 0;
	my $maxdim = $perimeter - 2;

	foreach my $a (1 .. $maxdim) {
		foreach my $b (1 .. $maxdim) {
			my $c = $perimeter - $a - $b;
			next if $c < 1;
			next unless ($a+$b+$c) == $perimeter;
			next unless ($a**2 + $b**2 == $c**2);
			#print "\t$a $b $c == $perimeter\n";
			$valid_triangles++;
		}
	}
	
	return $valid_triangles;
}
