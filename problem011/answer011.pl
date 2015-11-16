#!/usr/bin/perl

use strict;
use warnings;
use Data::Dumper;

my($fh,$grid);
open($fh,"<",'20-20.txt') or die "could not open 20-20: $!";
while ( my $line = <$fh>) {
	chomp $line;
	my @row = split(/\s+/,$line);
	push(@$grid,\@row);
}
close($fh);

#print Dumper($grid);

my $greatest_product = 0;
my $count = 0;

# check left-right
foreach my $x (0 .. 19) {
	foreach my $y (0 .. 16) {
		my $product = 1;
		$count++;
		foreach my $term_index (0 .. 3) {
			$product *= $grid->[$x]->[$y+$term_index];
		}
		print "lr $x,$y $product\n";
		$greatest_product = $product if $product > $greatest_product;
	}
}

# check up-down
foreach my $x (0 .. 16) {
	foreach my $y (0 .. 19) {
		my $product = 1;
		$count++;
		foreach my $term_index (0 .. 3) {
			$product *= $grid->[$x+$term_index]->[$y];
		}
		print "ud $x,$y $product\n";
		$greatest_product = $product if $product > $greatest_product;
	}
}

# check diaganol forward
foreach my $x (0 .. 16) {
	foreach my $y (0 .. 16) {
		my $product = 1;
		$count++;
		foreach my $term_index (0 .. 3) {
			$product *= $grid->[$x+$term_index]->[$y+$term_index];
		}
		print "diag $x,$y $product\n";
		$greatest_product = $product if $product > $greatest_product;
	}
}

# check diaganol backwards
foreach my $x (0 .. 16) {
	foreach my $y (0 .. 16) {
		my $product = 1;
		$count++;
		foreach my $term_index (0 .. 3) {
			$product *= $grid->[$x-$term_index]->[$y+$term_index];
		}
		print "diag $x,$y $product\n";
		$greatest_product = $product if $product > $greatest_product;
	}
}

print "count=$count\n";
print "ANSWER:$greatest_product\n";
