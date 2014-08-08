#!/usr/bin/perl

use strict;
use warnings;
use Math::Prime::Util qw(is_prime);

my $count = 0;
my $n = 0;

while ($count < 10001) {
	$n++;

	if (is_prime($n)) {
		$count++;
		#print "$count $n\n";
	}
}

print "ANSWER:$n\n";
