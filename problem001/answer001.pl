#!/usr/bin/perl

use strict;
use warnings;

my $sum = 0;
for my $n (1..999) {
	if ( ($n % 3) == 0 or ($n % 5) == 0) {
		$sum += $n;
	}
}

print "ANSWER:$sum\n";
