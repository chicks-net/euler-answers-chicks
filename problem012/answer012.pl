#!/usr/bin/perl

use strict;
use warnings;
use Math::Prime::Util qw(divisors);
use Data::Dumper;


sub count_factors {
	my ($n) = @_;

	my @factors = divisors($n);
#	print "$n: " . join(',', @factors) . "\n";
	my $count = scalar @factors;

	return $count;
}

my $max_divisors = 0;
my $n = 0;
my $triangle = 0;

while ($max_divisors < 502) {
	$n++;
	my $loop_n = $n;
	$triangle = 0;

	while($loop_n) {
		$triangle += $loop_n;
		$loop_n --;
	}

	my $divisors = count_factors($triangle);
	if ($divisors > $max_divisors) {
		$max_divisors = $divisors;
		print "n=$n triangle=$triangle has $max_divisors divisors\n";
	}
}

print "ANSWER:$triangle\n";

__END__
		print "n=" + str(n) + " triangle " + str(triangle) + " has " + str(max_divisors) + " divisors"

