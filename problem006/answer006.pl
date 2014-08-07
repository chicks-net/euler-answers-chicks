#!/usr/bin/perl

use strict;
use warnings;

my $sum_of_squares = 0;
my $unsquared_sum = 0;

foreach my $x (1..100) {
	$unsquared_sum += $x;
	$sum_of_squares += $x ** 2;
}

my $squared_sum = $unsquared_sum ** 2;
my $diff = $squared_sum - $sum_of_squares;
print "ANSWER:$diff\n";
