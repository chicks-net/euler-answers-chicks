#!/usr/bin/perl

use strict;
use warnings;
use Math::Prime::Util qw(primes);

my $primes = primes(2000000);

my $sum = 0;
my $count = 0;

foreach my $n (@$primes) {
	$count++;
	$sum += $n;
}

print "count=$count\n";
print "ANSWER:$sum\n";
