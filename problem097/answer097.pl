#!/usr/bin/perl

use strict;
use warnings;
use bignum;

BEGIN { print "this could take a while...\n"; }

my $prime = ( 28433 * (2 ** 7830457) ) + 1;
my $prime_length = length($prime);
print "prime_length=$prime_length\n";

my $answer = substr($prime,-10,10);
print "ANSWER:$answer\n";
