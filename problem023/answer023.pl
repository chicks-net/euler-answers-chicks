#!/usr/bin/perl

use strict;
use warnings;
use Data::Dumper;
use Math::Prime::Util qw(divisors);
use Algorithm::Combinatorics qw(variations_with_repetition variations);
use Time::HiRes qw(gettimeofday tv_interval);

sub sum {
	my $sum = 0;
	map { $sum += $_} @_;
	return $sum;
}

sub perfect {
	my ($n) = @_;
my @factors = divisors($n);
	pop @factors; # dump $n
	my $check_sum = sum(@factors);
	print "$n: " . join(',', @factors) . " -> $check_sum\n";

	if ($check_sum == $n) {
		return 1;
	} else {
		return 0;
	}
}

sub deficient {
	my ($n) = @_;

	my @factors = divisors($n);
	pop @factors; # dump $n
	my $check_sum = sum(@factors);
	print "$n: " . join(',', @factors) . " -> $check_sum\n";

	if ($check_sum < $n) {
		return 1;
	} else {
		return 0;
	}
}

sub abundant {
	my ($n) = @_;

	my @factors = divisors($n);
	pop @factors; # dump $n
	my $check_sum = sum(@factors);
#	print "$n: " . join(',', @factors) . " -> $check_sum\n";

	if ($check_sum > $n) {
		return 1;
	} else {
		return 0;
	}
}

my $time0 = [gettimeofday];
my @abundant;
foreach my $a (1..30000) {
	push(@abundant,$a) if abundant($a);
}
#print "Abundant:::: " . Dumper(\@abundant);
my $time1 = [gettimeofday];
my $elapsed = tv_interval($time0, $time1);
print scalar(@abundant) . " abundant numbers found in $elapsed seconds\n";

my $c;
my %summed;
my $addable_handle = variations_with_repetition(\@abundant,2);
while (my $pair = $addable_handle->next) {
	my ($a,$b) = @$pair;
	my $sum = $a + $b;
	unless( defined $summed{$sum} ) {
		$summed{$sum} = "$a+$b";
	}
	$c++;
}
my $time2 = [gettimeofday];
$elapsed = tv_interval($time1, $time2);
print "$c sums calculated for " . scalar(keys %summed) . " resultant sums in $elapsed seconds\n";

sub sum_deficient {
	my ($r) = @_;
	my $min = 2 * $abundant[0];

	if ($r < $min) {
		return 1;
	} else {
		#print "checking $r...\n";
		if (defined $summed{$r}) {
			#print "$r -> " . $summed{$r} . "\n";
			return 0;
		} else {
			return 1;
		} 
		die "should not get here";
	}
}

my $summable_deficient = 0;

foreach my $k (29000..30000) {
	my $deficiency = sum_deficient($k);
	$summable_deficient += $k if $deficiency;
}

die "crosscheck fail" unless $summable_deficient == 0;
print "crosscheck PASSed\n";

foreach my $k (1..29000) {
	my $deficiency = sum_deficient($k);
	$summable_deficient += $k if $deficiency;
}

print "ANSWER:$summable_deficient\n";
