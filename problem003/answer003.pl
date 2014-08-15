#!/usr/bin/perl

use strict;
use warnings;
use Math::Prime::Util qw(is_prime factor);
use Data::Dumper;

print "prime factors of 13195: " . Dumper(prime_factors(13195));
print "ANSWER:" . biggest_prime_factor(600851475143). "\n";

sub prime_factors {
	my ($n) = @_;

	my @factors = factor($n);
	my @this_prime_factors = map { $_ if is_prime($_) } @factors;

	return \@this_prime_factors;
}

sub biggest_prime_factor {
	my ($n) = @_;
	my $prime_factors = prime_factors($n);
	return $prime_factors->[-1];
}
