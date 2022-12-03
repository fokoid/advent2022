use strict;
use warnings;
use feature ':5.10';

say "Part 1: " . solution1();
say "Part 2: " . solution2();

sub solution1 {
	open my $file, 'input.txt';
	my $score = 0;

	while (defined(my $line = <$file>)) {
		$score += score(find_mismatched(rtrim($line)));
	}

	close $file;
	return $score;
}

sub find_mismatched {
	my $line = $_[0];
	my $midpoint = (length $line) / 2;
	my %chars = charset(substr $line, 0, $midpoint);

	foreach my $char (split //, (substr $line, $midpoint)) {
		if (exists $chars{$char}) {
			return $char;
		}
	}
}

sub solution2 {
	open my $file, 'input.txt';
	my $score = 0;

	while (defined(my $line1 = <$file>) and defined(my $line2 = <$file>) and defined(my $line3 = <$file>)) {
		$score += score(find_badge($line1, $line2, $line3));
	}

	close $file;
	return $score;
}

sub find_badge {
	my %chars1 = charset($_[0]);
	my %chars2 = charset($_[1]);
	my %chars3 = charset($_[2]);

	my %intersection = %{intersection(\%chars1, \%chars2, \%chars3)};
	foreach (keys %intersection) {
		return $_;
	}
}

sub score {
	my $score = (ord $_[0]) + 1;
	if ($score > 97) {
		$score = $score - ord('a');
	} else {
		$score = $score - ord('A') + 26;
	}
	return $score;
}

# given string returns hashset of characters present
sub charset {
	my %set;
	foreach my $char (split //, rtrim($_[0])) {
		$set{$char} = ();
	}
	return %set;
}

sub rtrim {
	$_[0] =~ s/\s+$//;
	return $_[0];
}

sub intersection {
	# beginners' note: hashes etc must be passed and returned by reference in Perl
	# hence the notation below and where intersection() is called
	my %intersection;
	foreach my $key (keys %{$_[0]}) {
		$intersection{$key} = () if exists $_[1]->{$key} and exists $_[2]->{$key};
	}
	return \%intersection;
}