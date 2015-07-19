#!/usr/bin/perl

use strict;
use warnings;
use Test::More;
use File::Find;
use Data::Dumper;

my %correct_answers = read_answers('answers.txt');
#print Dumper(\%correct_answers);
ok( (scalar keys %correct_answers) > 0, 'read correct answers');

my @files;
find(\&find_answers,'..');
ok( (scalar @files) > 0, 'found answer files to test');

foreach my $f (sort @files) {
	my ($q,$lang,$hashtag);
	if ($f =~ /(?:^|\/)answer(\d{3})\.(\w+)$/) {
		$q = $1+0;
		$lang = $2;
		if ( defined $correct_answers{$q}->{hashtag} ) {
			$hashtag = $correct_answers{$q}->{hashtag};
		} else {
			$hashtag = '';
		}
	} else {
		fail("$f name parse error");
		next;
	}

	SKIP: {
		if ($hashtag eq 'slow') {
			skip "q$q is slow ($lang)",1;
			next;
		}

		my $out = `$f`;

		if ($out =~ /^ANSWER:(\d+)$/m) {
#			print "got $1 in $f\n";
			cmp_ok($1,'==',$correct_answers{$q}->{answer},"$q $lang correct");
		} else {
			fail("$f did not return answer");
		}
	}
}

done_testing();

sub find_answers {
	return unless -f;
	my $filename = $_;
	return unless $filename =~ /^answer(\d{3})\.(\w+)$/;
	my $fullfilename = $File::Find::name;
	my $q = $1+0;
	my $language = $2;

#	print "$fullfilename $q $2\n";

	unless (defined $correct_answers{$q} and length $correct_answers{$q}->{answer}) {
		fail("no answer for $q");
		return;
	}

	push(@files,$fullfilename);
}

sub read_answers {
	my($file) = @_;
	die "no $file" unless -f $file;

	my $fh;
	open($fh,'<',$file) or die "couldn't open($file): $!";

	my %correct;
	while (my $line = <$fh>) {
		chomp($line);
		my ($q,$a) = split(/\|/,$line);
		my ($answer,$hashtag) = split(/#/,$a);
		my $answer_obj = { answer => $answer };
		$answer_obj->{hashtag} = $hashtag if defined $hashtag;
		$correct{$q} = $answer_obj;
	}
	close($fh);
	return(%correct);
}
